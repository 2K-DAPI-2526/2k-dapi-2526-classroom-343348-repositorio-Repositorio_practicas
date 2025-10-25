# Repositorio_practicas
Bienvenidos al repositorio de GITHUB para este grupo 2K para el módulo de DAPI. Si perteneces a este grupo, estás en el sitio correcto.

Lo primero que tienes que saber sobre GITHUB es que es un entorno bastante complejo y que puede paracer al principio algo ofuscante, confuso y nublado. Pero veras que en cuanto le cogas el truco, es una herramienta muy útil para progamar y trabajar en la nube de forma individual o en grupo.

!MUCHO ÁNIMO Y A POR ELLO¡

En este repositorio remoto, se irán subiendo las prácticas a las cuáles tendréis acceso desde el momento en que las suba a este repositorio y que tendrán valor del 50% sobre la evaluación.

Cada práctica, se subirá con su número en el repositorio remoto para que os podáis clonar el archivo y trabajar en local.

También estará cada práctica individual subida en CLASSROOM en  formato .ZIP para que podáis trabajar en local y subir las prácticas.

La herramienta GITHUB os va a permitir trabajar en línea y tener acceso a todas las modificaciones que realizéis desde VS CODE o desde cualquier entorno virtual de programación.

Para empezar, deberás abrirte una cuenta en GITHUB accediendo al siguiente enlace:

•	Cuenta de GitHub (gratuita): https://github.com


Tras instalar, configura tu nombre y correo:

 	git config --global user.name "Tu Nombre"
  git config --global user.email "tuemail@ejemplo.com"


Tenéis que tener en cuenta lo siguiente acerca de GITHUB.

Es un repositorio remoto por lo tanto no guarda los cambios si no se le pedís.

Si queremos modificar un archivo en remoto tendremos que primero modificarlo en local y despues subir los cambios al repositorio de nuevo.

Para modificar los cambios desde local, tendremos que utilizar los siguientes comandos:

git init - Se crea el fichero .git e inicia el repositorio. En el caso de que ya esté incializado (Como es el caso), pondrá que se reinicializa y no hará ningún cambio más. (No es importante pero viene bien hacerlo por si acaso)

git status - Devolverá los últimos cambios que hayas hecho en el directorio del archivo que estes trabajando. En el caso de que no se haya realizado ningún cambio, deolverá lo siguiente: "nothing to commit, working tree clean" lo cuál significa que no has hecho ninguna modificación nueva desde que añadiste los últimos cambios en el repositorio.

git add . - Añade todos los cambios de todos los ficheros no guardados (Si no has hecho ningún cambio, te devolverá la frase "nothing to commit", lo cuál significa que no hay ningún cambio nuevo a guardar.

git commit - Confirma todos los cambios de la zona de intercambio temporal, añadiéndolos y creando una nueva versión del proyecto (importante que no dé error ya que a veces puede cruzarse con el archivo remoto que estamos clonando y nos indica de que el repositorio remoto lo está bloqueando con otro archivo. En este caso lo mejor será salir y volver a empezar ya que nuestro archivo estará entrando en conflicto con la nube).

git push (Este nos permitirá subir los cambios al repositorio de GITHUB) - Si no hacemos este último Script, los cambios no se guardarán en el repositorio remoto.

Si tenemos un archivo en el repositorio remoto que queremos traerlo a la zona de intercambio, tendremos que clonar al repositorio local el arhcivo y trabajar desde ahí (ya veremos como).

Para ir desde el local hasta el directorio, usaremos los comandos Git checkout o Git merge

IMPORTANTE: Todas las prácticas se deberán subir al repositorio remoto de prácticas antes de la fecha indicada en CLASSROOM con el número de práctica, nombre y apellidos. Ejemplo: Practica1_Javier_Granda
