# Registro de enfermería escolar

Aplicación Flask con acceso local y, opcionalmente, inicio de sesión con Google.

## Despliegue con Gunicorn

Configura el comando de inicio del servidor como:

```sh
gunicorn main:app --bind 0.0.0.0:${PORT:-8080}
```

El módulo `main` expone la aplicación Flask para Gunicorn. Si el proveedor ya
configura `main:app`, no es necesario cambiar ese destino.

## Configurar inicio con Google

1. Instala dependencias: `python -m pip install -r requirements.txt`.
2. En Google Cloud Console, crea credenciales OAuth de tipo **Aplicación web** y configura la pantalla de consentimiento.
3. En las variables de entorno del servidor, define `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` junto con `FLASK_SECRET_KEY`.
4. Registra como URI de redirección autorizada `https://TU-DOMINIO/login/google/callback`. Para desarrollo local, usa `http://localhost:5000/login/google/callback`.
5. En producción, sirve el sitio con HTTPS y configura `HTTPS_ONLY=1`.
6. Vincula una cuenta Google con un usuario existente. Con el usuario conectado al archivo de base de datos correcto, ejecuta:

   ```powershell
   flask --app app vincular-google admin correo@ejemplo.cl
   ```

   Cambia `admin` por el nombre de usuario correspondiente. También se puede asociar un correo desde el formulario de creación de usuarios. El inicio Google solo se habilita cuando están definidas ambas credenciales; solo pueden entrar usuarios activos previamente vinculados.

La base de datos se migra automáticamente al iniciar la aplicación. La vinculación inicial usa el correo verificado de Google y luego se reconoce la cuenta mediante su identificador estable de Google. No se crean usuarios automáticamente ni se asignan permisos por iniciar sesión.
