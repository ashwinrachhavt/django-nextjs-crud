# CRUD Project with Django and Next.js

This project is a CRUD application that uses **Django** as the backend and **Next.js** as the frontend. It allows you to create, read, update, and delete tasks.

![basic](https://github.com/lace04/django-nextjs-crud/assets/73793929/5b05cca3-1cfd-41cf-b054-c99b0ecb055d)

# 💻 Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white) 
![Next JS](https://img.shields.io/badge/Next-black?style=flat&logo=next.js&logoColor=white) 
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white) 
![ShadCN](https://img.shields.io/badge/ShadCN-%2338B2AC.svg?style=flat&logo=shadcn&logoColor=white)
![Django Ninja](https://img.shields.io/badge/Django%20Ninja-%23092E20.svg?style=flat&logo=django&logoColor=white)

## Backend (Django)

1. **Virtual Environment Setup:**

   - Create a virtual environment named "venv":
     ```
     python -m venv venv
     ```

2. **Install Required Packages:**

   - Install Django and Django Ninja:
     ```
     pip install django django-ninja
     ```

3. **Initialize Django Project:**

   - Create a new project named "taskapi":
     ```
     django-admin startproject taskapi .
     ```

4. **Create the "tasks" App:**

   - Create an app named "tasks":
     ```
     python manage.py startapp tasks
     ```

5. **Enable CORS:**

   - Install the `django-cors-headers` package to enable CORS:
     ```
     pip install django-cors-headers
     ```

6. **Create and Migrate the Model:**

   - Create the data model for tasks:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

7. **Run the Server:**
   - Start the development server:
     ```
     python manage.py runserver
     ```

## Frontend (Next.js)

1. **Development Environment Setup:**

   - Ensure you have Node.js and npm installed.
   - Navigate to the frontend directory.

2. **Install Dependencies:**

   - Install Next.js and ShadCN dependencies:
     ```
     npx create-next-app@latest
     npx shadcn
     ```

3. **Run the Development Server:**
   - Start the Next.js development server:
     ```
     pnpm run dev
     ```

That's it! You now have a functional CRUD application with Django and Next.js using ShadCN for the frontend and Django Ninja for the backend. Have fun developing! 🚀
