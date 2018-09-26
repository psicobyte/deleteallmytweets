#!/usr/bin/python
#coding: utf-8

# CopyRight 2018 Allan Psicobyte (psicobyte@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import ConfigParser
import csv
import tweepy


def main(argv):

    config = open_config()

    file_csv = 'tweets.csv'

    response = raw_input('Este programa borrará TODOS sus tweets. Escriba BORRAR para hacerlo, cualquier otra cosa para cancelar: ')

    if response == 'BORRAR':
        print 'Borrando:'
        batch_delete_tweets(config,file_csv)
    else:
        print 'Operación cancelada. No se borrará nada'

def open_config():
    """Busca y abre un archivo INI para extraer las contraseñas y la configuración
    Por orden de preferencia, busca el archivo en /home/USER/apitw.ini, en /home/USER/.apitw y en apitw.ini
    """ 

    home_dir_ini_file = os.path.join(os.path.expanduser("~"),"apitw.ini")
    home_dir_ini_hidden_file = os.path.join(os.path.expanduser("~"),".apitw")
    my_dir_ini_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),"apitw.ini")

    if os.path.isfile(home_dir_ini_file):
        configfile = home_dir_ini_file
    elif os.path.isfile(home_dir_ini_hidden_file):
        configfile = home_dir_ini_hidden_file
    elif os.path.isfile(my_dir_ini_file):
        configfile = my_dir_ini_file
    else:
        show_error("Falta archivo INI")
        sys.exit()

    config = ConfigParser.ConfigParser()

    config.read(configfile)

    return config


def login_api(config):
    """Se loguea en twitter mediante OAuth con las claves extraídas del archivo de configuración"""

    try:
        consumer_key= config.get("Keys", "consumer_key")
        consumer_key_secret= config.get("Keys", "consumer_key_secret")
        access_token= config.get("Keys", "access_token")
        access_token_secret= config.get("Keys", "access_token_secret")
    except:
        show_error("faltan datos de clave en CONFIG, LECHES")
        sys.exit()

    auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    if api.verify_credentials():
        return api
    else:
        show_error("error de autorizacion")
        sys.exit()


def batch_delete_tweets(config,file_csv):

    api = login_api(config)

    with open(file_csv, 'r') as csvfile:

        reader = csv.DictReader(csvfile)

        deleted = 0
	undeleted = 0

        for row in reader:

            try:
                api.destroy_status(row['tweet_id'])
                deleted += 1
                print "OK: ", row['tweet_id']
            except tweepy.error.TweepError:
                undeleted += 1
                print "ERROR: ", row['tweet_id']

    print "Proceso finalizado."
    print deleted, " tweets borrados."
    print undeleted, " tweets no han podido ser borrados."


def show_error(error):
    """Muestra los errores, o los mostrará cuando esta función esté hecha"""
    
    print error

if __name__ == "__main__":
    main(sys.argv[1:])
