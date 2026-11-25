# Registro de Enfermería Escolar

## Nombre y descripción del proyecto

**Registro de Enfermería Escolar** es una aplicación web desarrollada con Flask para digitalizar y organizar la atención de alumnos en la enfermería del establecimiento.

Permite registrar estudiantes, crear atenciones, mantener una cola de espera, iniciar y finalizar consultas, guardar observaciones clínicas administrativas y consultar el historial. La interfaz está diseñada para facilitar el uso dentro del colegio y mantener una búsqueda rápida de los registros.

Este proyecto es un MVP. No incluye sincronización automática con sistemas externos ni garantiza compatibilidad con los formatos de Kimche. No se debe importar información clínica desde el sistema del colegio sin autorización expresa.

## Tecnologías utilizadas

- **Python:** lógica de la aplicación.
- **Flask:** servidor web, rutas, sesiones y renderizado de vistas.
- **SQLite:** base de datos local.
- **Jinja2:** plantillas HTML dinámicas.
- **HTML, CSS y JavaScript:** interfaz de usuario.
- **Werkzeug:** generación y comprobación de contraseñas.
- **Authlib:** inicio de sesión opcional con Google OAuth.
- **Gunicorn:** servidor WSGI para despliegue.
- **Git y GitHub:** control de versiones y alojamiento del código.
- **Visual Studio Code:** edición y desarrollo.

## Instalación y ejecución local

### Requisitos

- Python 3.10 o superior.
- Git.
- Acceso a una terminal.

### Instalación

```bash
git clone https://github.com/dalarcons76/registro_enfermeria.git
cd registro_enfermeria
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Configuración

Copia `.env.example` y ajusta las variables necesarias en el entorno de ejecución:

```bash
FLASK_SECRET_KEY=CLAVE_ALEATORIA_LARGA
ENFERMERIA_DATABASE=/ruta/al/enfermeria.sqlite3
HTTPS_ONLY=0
PORT=5000
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
```

Genera una clave segura con:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Variables principales:

| Variable | Uso |
|---|---|
| `FLASK_SECRET_KEY` | Protege las sesiones de Flask. Debe mantenerse estable y fuera del repositorio. |
| `ENFERMERIA_DATABASE` | Ruta opcional de la base SQLite. Por defecto usa `instance/enfermeria.sqlite3`. |
| `HTTPS_ONLY` | Usa `1` en producción HTTPS para proteger la cookie de sesión. |
| `PORT` | Puerto del servidor local; el valor predeterminado es `5000`. |
| `GOOGLE_CLIENT_ID` | ID OAuth de Google. Opcional. |
| `GOOGLE_CLIENT_SECRET` | Secreto OAuth de Google. Opcional y confidencial. |

No publiques contraseñas, secretos OAuth ni archivos de la base de datos.

### Ejecutar en desarrollo

```bash
python app.py
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000).

Al iniciar por primera vez se crea automáticamente la base de datos. También se crea el usuario administrador predeterminado `admin` con la contraseña `Admin2026!Password`. Esta cuenta es para configuración inicial y debe cambiarse o reemplazarse inmediatamente en un entorno real.

## Inicio de sesión con Google

El inicio con Google es opcional y solo se habilita si están configurados `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET`.

1. Crea credenciales OAuth de tipo **Aplicación web** en Google Cloud Console.
2. Define las variables OAuth en el entorno.
3. Agrega como URI autorizada:
   - Desarrollo: `http://localhost:5000/login/google/callback`
   - Producción: `https://TU-DOMINIO/login/google/callback`
4. Vincula una cuenta Google a un usuario activo existente:

```bash
flask --app app vincular-google USUARIO CORREO@EJEMPLO.CL
```

El sistema no crea usuarios automáticamente desde Google. La cuenta debe haber sido autorizada y vinculada previamente por un administrador.

## Despliegue

Para ejecutar con Gunicorn:

```bash
gunicorn main:app --bind 0.0.0.0:${PORT:-8080}
```

Ejemplo para un entorno Unix:

```bash
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
export HTTPS_ONLY=1
gunicorn main:app --bind 0.0.0.0:8080
```

En producción se recomienda usar HTTPS, una ruta persistente para SQLite y una clave secreta definida permanentemente en las variables de entorno del servicio.

## Rutas del proyecto

Todas las rutas, excepto el inicio de sesión y los enlaces de autenticación, requieren una sesión activa.

| Método | Ruta | Funcionalidad |
|---|---|---|
| `GET`, `POST` | `/login` | Iniciar sesión con usuario y contraseña. |
| `GET` | `/login/google` | Iniciar autenticación OAuth con Google. |
| `GET` | `/login/google/callback` | Recibir la respuesta de Google y crear la sesión. |
| `POST` | `/logout` | Cerrar la sesión actual. |
| `GET` | `/` | Mostrar el panel diario y la cola de atenciones. |
| `GET`, `POST` | `/alumnos` | Listar, buscar y registrar alumnos. |
| `GET`, `POST` | `/atenciones/nueva` | Crear una atención y añadirla a la cola. |
| `GET`, `POST` | `/atenciones/<id>` | Ver o actualizar una atención: iniciar, guardar o finalizar. |
| `GET` | `/atenciones` | Consultar y buscar el historial de atenciones. |
| `GET` | `/atenciones/<id>/constancia/<tipo>` | Generar una constancia para `alumno` o `profesor`. |
| `GET` | `/exportar/alumnos.csv` | Descargar el listado activo de alumnos en CSV. |
| `GET`, `POST` | `/importar/alumnos` | Importar alumnos desde un CSV genérico. |
| `GET`, `POST` | `/admin/crear-usuario` | Crear usuarios; disponible solo para administradores. |

## Importación y exportación CSV

La importación usa las siguientes columnas:

```csv
identificador_escolar,nombre,apellido,curso
```

Las columnas obligatorias son `nombre`, `apellido` y `curso`. `identificador_escolar` es opcional. Las filas incompletas y los identificadores duplicados se omiten. No existe sincronización automática con otros sistemas.

## Estructura del proyecto

```text
registro_enfermeria/
├── app.py                 # Fábrica de la aplicación, rutas y acceso a datos
├── main.py                # Punto de entrada compatible con Gunicorn
├── requirements.txt       # Dependencias de Python
├── .env.example           # Ejemplo de variables de entorno
├── .gitignore             # Archivos excluidos del repositorio
├── README.md              # Documentación del proyecto
├── instance/              # Base SQLite local y archivos propios del entorno
├── app/                   # Módulo auxiliar de compatibilidad
├── static/
│   ├── css/               # Hojas de estilo
│   ├── js/                # JavaScript
│   └── images/            # Recursos gráficos
└── templates/
    ├── pages/             # Vistas HTML
    └── components/        # Componentes reutilizables
```

La configuración principal y las rutas viven en `app.py`. `main.py` expone la aplicación como `app` para plataformas de despliegue y Gunicorn.

## Base de datos

La aplicación usa SQLite y crea o migra las tablas automáticamente al recibir solicitudes.

### `users`

Usuarios autorizados del sistema:

- `id`: identificador interno.
- `username`: nombre de usuario único.
- `password_hash`: contraseña protegida mediante hash.
- `role`: `admin` o `enfermeria`.
- `active`: indica si la cuenta está activa.
- `google_email` y `google_sub`: datos opcionales para vincular una cuenta Google.

### `students`

Información básica de alumnos:

- `id`: identificador interno.
- `school_id`: identificador escolar único.
- `first_name`, `last_name` y `course`.
- `active`: indica si el alumno está activo.
- `created_at`: fecha de creación.

### `visits`

Atenciones y su estado:

- `student_id`: alumno atendido.
- `created_at`, `arrived_at` y `departed_at`: tiempos de registro y salida.
- `reason`, `symptoms`, `actions_taken`, `outcome` y `notes`: datos de la consulta.
- `status`: `espera`, `atencion` o `finalizada`.
- `created_by` y `updated_by`: usuarios responsables.

### `audit_log`

Registro de acciones relevantes:

- usuario que realizó la acción;
- tipo de acción;
- entidad modificada;
- identificador del registro;
- fecha y detalle breve.

Las claves foráneas están habilitadas y existen índices para búsquedas por nombre, curso, estado y fechas.

## Funcionalidades principales

- Inicio de sesión con usuario y contraseña.
- Inicio de sesión opcional mediante Google OAuth.
- Separación de roles administrativo y de enfermería.
- Protección de formularios con token CSRF.
- Registro y búsqueda de alumnos.
- Creación de atenciones asociadas a un alumno.
- Cola de atenciones con estados de espera y atención.
- Registro de síntomas, acciones, resultados y notas.
- Finalización de atenciones con hora de salida.
- Historial y búsqueda de atenciones.
- Generación de constancias para alumno o profesor.
- Importación y exportación de alumnos en CSV.
- Registro de auditoría de acciones importantes.
- Inicialización y migración automática de SQLite.

## Integrantes

- Diego Alarcon
- Sebastian Delgado
- Sebastian Bustos
- Tomas Rodrigues
- Copilot
- ChatGPT