<<<<<<< Updated upstream
# Enfermería escolar — MVP Flask + SQLite

Aplicación interna para centralizar el registro de atenciones, gestionar los casos en curso y generar constancias del alumno y del profesor desde una única atención.

## Incluye

- Inicio de sesión con contraseñas hasheadas y roles (`admin`, `enfermeria`).
- Directorio y búsqueda de alumnos.
- Registro único de atención en curso y finalizada.
- Lista de atenciones activas y resumen diario/semanal.
- Constancia imprimible para el alumno y constancia administrativa para el profesor. La copia del profesor no incluye detalles clínicos.
- Historial de atenciones.
- Importación CSV inicial y exportación del directorio.
- Auditoría básica de acciones.
- Protección CSRF en formularios, consultas SQL parametrizadas, cookies HttpOnly/SameSite.
- SQLite con claves foráneas, WAL y timeout para escrituras concurrentes.

## Estructura

```text
registro_enfermeria/
├── app.py
├── app/                  # Conserva la carpeta de aplicación del repositorio base
├── instance/             # Se crea automáticamente; NO subir a Git
├── static/
│   └── style.css
├── templates/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación (Windows)

Abre PowerShell en la carpeta del proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:FLASK_SECRET_KEY = py -c "import secrets; print(secrets.token_hex(32))"
flask --app app crear-admin
```

El comando `crear-admin` pide un usuario y una contraseña de al menos 12 caracteres. Guarda la contraseña en un gestor institucional. Luego inicia el servidor LAN:

```powershell
waitress-serve --listen=0.0.0.0:5000 app:app
```

En el computador servidor abre `http://127.0.0.1:5000`. Desde otros computadores de la red, abre `http://IP-DEL-SERVIDOR:5000`.

Para conocer la IP privada del servidor usa `ipconfig`. Configura el firewall para permitir el puerto TCP 5000 solo en la red privada institucional. No publiques el puerto en Internet. Mantén el computador servidor encendido, con acceso restringido y copias de seguridad protegidas.

## Instalación (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
flask --app app crear-admin
waitress-serve --listen=0.0.0.0:5000 app:app
```

## Importación de alumnos

Desde **Alumnos → Importar CSV**, sube un CSV UTF-8 con estos encabezados exactos:

```csv
identificador_escolar,nombre,apellido,curso
A1024,Valentina,Ejemplo,2° Medio A
,Benjamín,Prueba,7° Básico B
```

El identificador escolar puede quedar vacío. Se omiten filas incompletas y los identificadores duplicados. Exportar alumnos crea un archivo CSV con encabezados `identificador_escolar,nombre,apellido,curso,activo`.

La importación/exportación de este MVP es un formato propio y **no es una integración directa con Kimche**. Antes de intercambiar datos con Kimche, confirmar con el colegio y el proveedor que existe un método autorizado, qué campos pueden exportarse y cuál es la base legal para hacerlo.

## Pruebas manuales de aceptación

1. Iniciar sesión como administrador.
2. Crear un usuario de enfermería desde el menú Usuarios.
3. Registrar o importar un alumno.
4. Crear una atención; debe iniciar directamente como “En atención” después de confirmar el registro.
5. Abrir la atención, completar acciones e indicaciones y guardar.
6. Abrir ambas constancias; imprimir o guardar como PDF.
7. Finalizar la atención; debe quedar en el historial y mostrar la hora de salida.
8. Cerrar sesión y verificar que el panel redirige al inicio de sesión.

## Limitaciones importantes antes de usar datos reales

Este es un MVP técnico, no un producto clínico validado. Antes de almacenar datos reales de menores, el colegio debe aprobar el flujo, los campos, la retención, los roles, las copias de seguridad y las medidas de privacidad. El despliegue de ejemplo usa HTTP dentro de la LAN: no lo expongas a redes públicas; para uso institucional real, usa HTTPS, controles de acceso de red, gestión segura de secretos y pruebas de seguridad. La constancia del alumno contiene información de atención; entrega solo al destinatario correcto.

SQLite es razonable para una aplicación interna con un único proceso servidor y pocos usuarios concurrentes. No compartas el archivo SQLite directamente por una carpeta de red: todos los equipos deben usar la aplicación Flask a través del navegador. Si la concurrencia de escritura crece, evalúa PostgreSQL.

## Kimche

No hay sincronización automática incluida. Este MVP permite cargar y descargar el directorio en CSV genérico, no garantiza compatibilidad con los formatos de Kimche. No importar información clínica desde el sistema del colegio sin autorización expresa.
=======
# Registro de enfermería escolar

## Nombre y descripción

**Registro de Enfermería Escolar** es una aplicación web desarrollada con Flask para digitalizar y organizar la atención de salud dentro de un establecimiento educativo.

Permite mantener un registro de alumnos, crear atenciones médicas o de enfermería, administrar una cola de espera, actualizar estados y resultados, consultar el historial y generar constancias o exportaciones CSV. El objetivo es reemplazar registros manuales dispersos por un sistema centralizado, fácil de consultar y de usar.

## Tecnologías utilizadas

- **Python 3**: lenguaje principal y lógica de servidor.
- **Flask**: servidor web, sesiones, rutas, formularios y renderizado.
- **SQLite**: base de datos local relacional.
- **Jinja2**: plantillas dinámicas HTML.
- **HTML y CSS**: estructura y presentación de la interfaz.
- **JavaScript**: comportamiento de la interfaz web.
- **Werkzeug**: generación y comprobación de contraseñas y utilidades HTTP.
- **Authlib**: inicio de sesión mediante Google OAuth 2.0.
- **Requests**: biblioteca HTTP disponible en la aplicación.
- **Gunicorn**: servidor WSGI para producción Linux.
- **Git y GitHub**: control de versiones y alojamiento del código.
- **Visual Studio Code**: entorno de desarrollo utilizado por el equipo.

Todas las dependencias declaradas se encuentran en [`requirements.txt`](/home/colegiocsl/registro_enfermeria/requirements.txt).

## Instalación local

### Requisitos

- Python 3.10 o superior.
- Git.
- Entorno compatible con terminal.
- Navegador web moderno.

### 1. Descargar el proyecto

```bash
git clone https://github.com/dalarcons76/registro_enfermeria.git
cd registro_enfermeria
```

También puede descargarse el repositorio como ZIP y abrirse la carpeta resultante en Visual Studio Code.

### 2. Crear y activar un entorno virtual

**Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Copie `.env.example` como `.env` y configure los valores necesarios:

```bash
cp .env.example .env
```

En Windows puede copiarse manualmente desde el Explorador o con PowerShell:

```powershell
Copy-Item .env.example .env
```

Variables disponibles:

| Variable | Descripción |
|---|---|
| `FLASK_SECRET_KEY` | Clave utilizada para firmar las sesiones. Debe ser aleatoria y larga en producción. |
| `ENFERMERIA_DATABASE` | Ruta opcional del archivo SQLite. Si no se define, se usa `instance/enfermeria.sqlite3`. |
| `PORT` | Puerto del servidor local. El valor predeterminado es `5000`. |
| `HTTPS_ONLY` | Use `1` cuando el sitio sea servido exclusivamente por HTTPS. |
| `GOOGLE_CLIENT_ID` | Identificador OAuth de Google para habilitar inicio de sesión con Google. |
| `GOOGLE_CLIENT_SECRET` | Secreto OAuth de Google. |
| `ADMIN_INICIAL_USUARIO` | Usuario opcional del administrador inicial creado mediante el comando CLI. |
| `ADMIN_INICIAL_PASSWORD` | Contraseña opcional del administrador inicial; debe tener al menos 12 caracteres. |

Genere una clave secreta con:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

No publique `.env`, contraseñas ni credenciales OAuth en el repositorio.

### 5. Ejecutar la aplicación

```bash
python app.py
```

Abra en el navegador:

```text
http://127.0.0.1:5000
```

La aplicación crea automáticamente las tablas SQLite y aplica las columnas nuevas al iniciar una solicitud.

Si no existe un administrador al iniciar, la aplicación crea el usuario `admin` con una contraseña predeterminada definida en `app.py`. Por seguridad, cambie o desactive esa configuración antes de usar el sistema en producción.

## Despliegue

### Despliegue con Gunicorn

El punto de entrada para Gunicorn es `main:app`:

```bash
gunicorn main:app --bind 0.0.0.0:${PORT:-8080}
```

Ejemplo con variables de entorno:

```bash
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
export HTTPS_ONLY=1
export ENFERMERIA_DATABASE="/ruta/segura/enfermeria.sqlite3"
gunicorn main:app --bind 0.0.0.0:8080
```

En proveedores compatibles con comandos de inicio, configure:

```text
gunicorn main:app --bind 0.0.0.0:$PORT
```

El despliegue debe utilizar HTTPS y un volumen persistente para el archivo SQLite. Antes de iniciar la aplicación se deben configurar `FLASK_SECRET_KEY` y la ruta persistente de `ENFERMERIA_DATABASE`.

### Administrador inicial mediante Flask CLI

Con las variables `ADMIN_INICIAL_USUARIO` y `ADMIN_INICIAL_PASSWORD` configuradas:

```bash
flask --app app crear-admin
```

Este comando crea el administrador solo si aún no existe ningún usuario con rol `admin`.

### Inicio de sesión con Google

1. Cree credenciales OAuth de tipo **Aplicación web** en Google Cloud Console.
2. Configure `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET`.
3. Agregue como URI de redirección:
   - Desarrollo: `http://localhost:5000/login/google/callback`
   - Producción: `https://TU-DOMINIO/login/google/callback`
4. Active HTTPS configurando `HTTPS_ONLY=1`.
5. Vincule una cuenta existente con:

```bash
flask --app app vincular-google USUARIO CORREO@EJEMPLO.CL
```

El inicio con Google no crea usuarios automáticamente. Solo puede iniciar sesión una cuenta que haya sido creada y vinculada por un administrador.

## Rutas del proyecto

Todas las rutas requieren autenticación, salvo el inicio de sesión y su callback.

| Ruta | Métodos | Funcionalidad |
|---|---|---|
| `/login` | `GET`, `POST` | Inicio de sesión local con usuario y contraseña. |
| `/login/google` | `GET` | Redirige al proveedor Google para autenticar. |
| `/login/google/callback` | `GET` | Recibe la respuesta OAuth y inicia la sesión vinculada. |
| `/logout` | `POST` | Cierra la sesión y registra la acción en la auditoría. |
| `/` | `GET` | Muestra el panel con contadores diarios y la cola de atenciones. |
| `/alumnos` | `GET`, `POST` | Busca y registra alumnos. |
| `/atenciones/nueva` | `GET`, `POST` | Crea una atención y la añade a la cola de espera. |
| `/atenciones/<id>` | `GET`, `POST` | Inicia, guarda o finaliza una atención y muestra su detalle. |
| `/atenciones` | `GET` | Consulta el historial y permite buscar atenciones. |
| `/atenciones/<id>/constancia/<tipo>` | `GET` | Genera una constancia para `alumno` o `profesor`. |
| `/exportar/alumnos.csv` | `GET` | Descarga el listado de alumnos en formato CSV. |
| `/importar/alumnos` | `GET`, `POST` | Importa alumnos desde un CSV con las columnas `nombre`, `apellido`, `curso` e, opcionalmente, `identificador_escolar`. |
| `/admin/crear-usuario` | `GET`, `POST` | Permite a un administrador crear usuarios locales y vincular correos Google. |

Los formularios incluyen token CSRF. Las rutas están protegidas por sesión y el sistema bloquea el acceso a usuarios inactivos.

## Estructura del repositorio

```text
registro_enfermeria/
├── app.py                  # Aplicación Flask principal, rutas, seguridad y base de datos
├── main.py                 # Punto de entrada compatible con Gunicorn
├── requirements.txt        # Dependencias Python
├── .env.example            # Ejemplo de configuración mediante variables de entorno
├── .gitignore              # Archivos y carpetas excluidos de Git
├── instance/
│   └── enfermeria.sqlite3  # Base SQLite local predeterminada
├── app/
│   ├── __init__.py         # Carga compatible desde el módulo app
│   ├── routes.py           # Módulo reservado/compatibilidad de rutas
│   ├── models.py           # Módulo reservado de modelos
│   ├── database.py         # Módulo reservado de persistencia
│   ├── services.py         # Módulo reservado de servicios
│   └── config.py           # Módulo reservado de configuración
├── templates/
│   └── pages/
│       ├── base.html       # Diseño general compartido
│       ├── login.html
│       ├── dashboard.html
│       ├── students.html
│       ├── visit_form.html
│       ├── visit_detail.html
│       ├── history.html
│       ├── receipt.html
│       ├── import.html
│       ├── create_user.html
│       └── error.html
└── static/
    ├── css/
    │   └── global.css      # Estilos globales
    └── js/
        └── global.js       # Comportamientos JavaScript globales
```

La lógica MVP está implementada principalmente en `app.py`. La carpeta `app/` conserva la organización modular original y expone la aplicación desde `app/__init__.py` para mantener compatibilidad con entradas como `main:app`.

## Base de datos

Por defecto se utiliza el archivo SQLite `instance/enfermeria.sqlite3`. La ubicación puede cambiarse mediante `ENFERMERIA_DATABASE`. Las tablas se crean o actualizan automáticamente al iniciar la aplicación.

### `users`

Almacena las cuentas autorizadas:

- `id`, `username`, `password_hash`
- `role`: `admin` o `enfermeria`
- `active`: indica si la cuenta está habilitada
- `created_at`
- `google_email` y `google_sub`: identidad vinculada de Google

### `students`

Contiene los alumnos registrados:

- `id`, `school_id`, `first_name`, `last_name`, `course`
- `active`
- `created_at`

`school_id` es único cuando está informado. Se mantienen índices por nombre y curso.

### `visits`

Contiene las atenciones escolares:

- Alumno asociado mediante `student_id`
- Fecha de llegada y salida
- Motivo, síntomas, acciones realizadas, resultado y notas
- Estado: `espera`, `atencion` o `finalizada`
- Usuario creador y usuario que realizó la última actualización
- Fechas de creación y actualización

Se mantienen índices por estado, fecha y alumno para acelerar consultas.

### `audit_log`

Registra acciones relevantes del sistema:

- Usuario que realizó la acción
- Acción y entidad afectada
- Identificador de la entidad
- Fecha y detalle

Las auditorías permiten rastrear inicios de sesión, cierres, altas, modificaciones, importaciones y exportaciones.

## Funcionalidades principales

- Inicio de sesión local con contraseñas cifradas.
- Inicio de sesión opcional con cuentas Google verificadas.
- Roles de administrador y personal de enfermería.
- Alta y búsqueda de alumnos.
- Identificador escolar opcional y único.
- Importación masiva de alumnos desde CSV.
- Exportación del listado de alumnos a CSV.
- Registro de atenciones con motivo, síntomas, acciones, resultado y notas.
- Cola diaria organizada por estado de atención.
- Flujo de atención: espera → atención → finalizada.
- Historial con búsqueda por alumno, curso o motivo.
- Constancias imprimibles para alumnos o profesores.
- Panel con contadores diarios de atenciones.
- Registro de auditoría de operaciones importantes.
- Protección CSRF, sesiones con atributos HTTPOnly/SameSite y soporte para HTTPS.

## Integrantes

- Diego Alarcon
- Sebastián Delgado
- Sebastián Bustos
- Tomás Rodriguez
>>>>>>> Stashed changes
