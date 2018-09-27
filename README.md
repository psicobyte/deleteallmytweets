deleteallmytweets
=====


## ADVERTENCIA

**¡Este programa borrará todos tus tweets!**


## Descripción

*deleteallmytweets* es un programa que permite borrar todas las entradas de una cuenta de twitter desde la línea de órdenes.


## Uso

Esta versión de *deleteallmytweets* usa python 2 (básicamente porque he canibalizado el código de un programa anterior) pero en la rama principal de este proyecto está la versión para Python 3.

Al ejecutar el programa, muestra una advertencia avisando de que borrará todos los tweets de la cuenta y pide confirmación. Si se escribe la palabra BORRAR (en mayúsculas) comenzará el proceso. Cualquier otro texto abortará el borrado.

El proceso de borrado puede tardar varias horas, dependiendo del número de tweets de la cuenta (a un ritmo aproximado de dos o tres tweets por segundo).

Por cada tweet borrado, *deleteallmytweets* mostrará um mensaje similar a este:

OK:  445971115773792257

Si el tweet no puede ser borrado por alguna razón (normalmente porque ya ha sido borrado anteriormente con otra aplicación), mostrará un mensaje como este:
 
ERROR:  445971115773792257

*deleteallmytweets* usa la librería [Tweepy](http://www.tweepy.org/) para acceder a la API de Twitter.

*deleteallmytweets* necesita una api key de twitter. Se trata de un conjunto de cuatro claves (dos de aplicación y dos de usaurio) que se obtienen al dar de alta una aplicación aquí: [https://dev.twitter.com/apps/new](https://dev.twitter.com/apps/new)


## El fichero tweets.csv

Dado que Twitter sólo permite acceder a los IDs de las últimas 3000 entradas, *deleteallmytweets* utiliza el archivo tweets.csv contenido en el "Archivo de Tweets" que se puede obtener de la propia página de Twitter (ver más abajo).

*deleteallmytweets* extrae las ID de los tweets a borrar de ese archivo.

Estando logueado en tu cuenta de Twitter, abrir el menú de "Perfil y configuración" (pulsanado sobre tu pequeño retrato a la derecha.

Seleccionar la opción "Configuración y Privacidad".

En esa ventana, junto a la opción "Tu archivo de Tweets", pulsar el botón "Solicita tu archivo".

Pasado cierto tiempo, recibirás un aviso para descargr tu archivo de tweets.

Este archivo es un fichero comprimido que contiene, entre otras cosas, el archivo "tweets.csv". Ese archivo debe extraerse en el mismo directorio de la aplicación *deleteallmytweets* (no es necesario extraer ningún otro).

*Naturalmente, es posible editar ese archivo manualmente para, por ejemplo, eliminar de él los tweets que no se deseen borrar.*


## apitw.ini

*deleteallmytweets* usa un archivo INI para almacenar las contraseñas e la API de twitter.

Por orden de preferencia, buscará el archivo en

* /home/USER/apitw.ini
* /home/USER/.apitw
* apitw.ini

Primero se buscará el archivo en "/home/USER/apitw.ini". Si no lo encuentra ahí, lo buscará en "/home/USER/.apitw" y, si tampoco está ahí, lo buscará en el directorio de la propia aplicación con el nombre de "apitw.ini".

Este archivo contiene las claves del usuario (se pueden obtener de [https://dev.twitter.com/apps/new](https://dev.twitter.com/apps/new)).

* consumer_key: API key de Twitter
* consumer_key_secret: API secret de Twitter
* access_token: Access token de Twitter
* access_token_secret: Access token secret de Twitter


