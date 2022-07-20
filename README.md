#Biblos 2.5 

###Casos de prueba automatizados con python y selenium.

Dentro de la carpeta testCases se encuentran los casos de prueba los cuales estaran nomenclados de la siguiente manera:

+ _id-nombreAccionArealizar-contenido(paginas/content/etc)-estadoDelContenido.py_

Esto ayudara al correcto orden de los casos de prueba y a una mejor organizacion de estos.

###Consideraciones a tomar en cuenta:


* Se debe crear un perfil especifico en el navegador (chrome, explorer, etc) para ejecutar las pruebas automaticas, de esta manera se evitara algun conflicto durante la ejecucion de casos, ya que el perfil predeterminado de Chrome puede contener extensiones, marcadores, historial de navegación, etc., y es posible que no se cargue correctamente.
* El archivo config.json guardara los datos de conexion y perfil de usuario a utilizar en el navegador web.

