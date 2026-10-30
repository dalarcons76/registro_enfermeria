# Nombre y descripción completa del proyecto
Registro de enfermeria escolar

Consiste en digitalizar y automatizar el registro de alumnos para que el ingresado sea de facil busqueda y ademas de facil acceso a sus registros. 

## Despliegue con Gunicorn

Configura el comando de inicio del servidor como:

```sh
gunicorn main:app --bind 0.0.0.0:${PORT:-8080}
```

El módulo `main` expone la aplicación Flask para Gunicorn. Si el proveedor ya
configura `main:app`, no es necesario cambiar ese destino.

## Configurar inicio con Google
=======
la aplicación puede ser utilizada por un admin. 

# Tecnologias utilizadas 
Python:	Lenguaje principal para implementar la lógica del sistema.
Flask:	   Framework que administra el servidor web, las rutas y las solicitudes de los usuarios.
SQLite:	Base de datos relacional para almacenar la información de la aplicación.
HTML: 	   Estructura de las páginas web y formularios.
CSS:	   Diseño visual y presentación de la interfaz.
Jinja2:	Generación dinámica de páginas HTML mediante plantillas de Flask.
Authlib:	Biblioteca relacionada con la autenticación e integración con    proveedores de identidad, según la configuración habilitada.
Requests	Biblioteca para realizar solicitudes HTTP desde Python.
Gunicorn:	Servidor WSGI para ejecutar la aplicación en un entorno de     despliegue compatible.
Git y GitHub:	Control de versiones y alojamiento del código fuente.
Visual Studio Code:	Editor utilizado para revisar y modificar el código.

# Instalación y ejecución del proyecto
El proyecto está desarrollado con Flask y puede ejecutarse localmente en Windows, Linux u otro sistema compatible con Python. Para utilizarlo desde varios computadores, debe ejecutarse en un equipo servidor accesible desde la red del colegio. 
GitHub+1

3.1. Requisitos previos
- Python instalado.
- Git, si se desea descargar el repositorio directamente.
- Visual Studio Code u otro editor de código.
- Terminal o consola de comandos.
- Acceso a Internet para instalar las dependencias.
3.2. Descargar el proyecto
Si se utiliza Git, ejecutar:
git clone https://github.com/dalarcons76/registro_enfermeria.git
cd registro_enfermeria


Si ya se descargó el repositorio como archivo ZIP, basta con descomprimirlo y abrir la carpeta en Visual Studio Code.
3.3. Crear un entorno virtual
En Windows, abrir la terminal dentro de la carpeta del proyecto y ejecutar:
python -m venv .venv
.venv\Scripts\Activate.ps1


En Linux, ejecutar:
python3 -m venv .venv
source .venv/bin/activate


El entorno virtual permite instalar las bibliotecas del proyecto sin mezclarlas con las de otros proyectos de Python.
3.4. Instalar las dependencias
Con el entorno virtual activado, ejecutar:
python -m pip install -r requirements.txt


Este comando instala las bibliotecas declaradas por el proyecto.
3.5. Configurar las variables de entorno
El repositorio incluye un archivo .env.example que sirve como referencia para la configuración. Deben revisarse sus variables y definir los valores necesarios en el entorno donde se ejecutará la aplicación. 
GitHub


Entre las variables relevantes se encuentran:
Variable	Propósito
FLASK_SECRET_KEY	Clave secreta para proteger las sesiones de Flask.
ENFERMERIA_DATABASE	Permite definir una ubicación personalizada para la base de datos SQLite.
GOOGLE_CLIENT_ID	Identificador OAuth de Google, si se habilita ese método de acceso.
GOOGLE_CLIENT_SECRET	Secreto OAuth de Google, si se habilita ese método de acceso.
HTTPS_ONLY	Permite exigir HTTPS mediante la configuración correspondiente.

Las credenciales reales deben mantenerse fuera del repositorio público. En particular, no se deben subir contraseñas ni secretos de Google a GitHub.
3.6. Inicializar y ejecutar la aplicación
La aplicación inicializa la base de datos al atender solicitudes. También dispone de un comando de Flask para crear el administrador inicial cuando se han configurado las credenciales de inicialización requeridas. 
GitHub


Para iniciar el servidor de desarrollo:
python app.py


Después, abrir el navegador en:

Dirección local

http://127.0.0.1:5000

# Rutas del proyecto y sus funcionalidades
