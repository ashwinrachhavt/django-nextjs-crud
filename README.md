# Proyecto CRUD con Django y Next.js

Este proyecto es una aplicación CRUD que utiliza **Django** como backend y **Next.js** como frontend. Permite crear, leer, actualizar y eliminar tareas.

## Backend (Django)

1. **Configuración del entorno virtual:**

   - Crea un entorno virtual llamado "venv":
     ```
     python -m venv venv
     ```

2. **Instalación de paquetes necesarios:**

   - Instala Django y djangorestframework:
     ```
     pip install django djangorestframework
     ```

3. **Inicialización del proyecto Django:**

   - Crea un nuevo proyecto llamado "taskapi":
     ```
     django-admin startproject taskapi .
     ```

4. **Creación de la aplicación "tasks":**

   - Crea una aplicación llamada "tasks":
     ```
     python manage.py startapp tasks
     ```

5. **Habilitación de CORS:**

   - Instala el paquete `django-cors-headers` para habilitar CORS:
     ```
     pip install django-cors-headers
     ```

6. **Creación y migración del modelo:**

   - Crea el modelo de datos para las tareas:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

7. **Ejecución del servidor:**
   - Inicia el servidor de desarrollo:
     ```
     python manage.py runserver
     ```

## Frontend (Next.js)

1. **Configuración del entorno de desarrollo:**

   - Asegúrate de tener Node.js y npm instalados.
   - Navega al directorio del frontend.

2. **Instalación de dependencias:**

   - Instala las dependencias de Next.js:
     ```
     pnpm install
     ```

3. **Ejecución del servidor de desarrollo:**
   - Inicia el servidor de desarrollo de Next.js:
     ```
     pnpm run dev
     ```

¡Listo! Ahora tienes una aplicación CRUD funcional con Django y Next.js. ¡Diviértete desarrollando! 🚀
