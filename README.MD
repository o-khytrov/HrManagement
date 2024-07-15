# 🏢 HR Management System

## Getting started

- Clone the repository 📥

```bash
git clone git@github.com:o-khytrov/HrManagement.git 
```

- Change directory into the project 📂 and create a virtual environment 🌐

```bash
python -m venv venv 
```

- Activate the virtual environment ⚡

    - Linux:
      ```bash
      source myenv/bin/activate 
      ```
    - Windows
       ```bash
        source venv\Scripts\activate 
        ```

- Install dependencies 📦

```bash
pip install -r requirements.txt 
```

- Change directory into the hr_management directory 📂

```bash
cd hr_management 
```

- Set up the database in Docker 🐳

```bash
docker compose up -d 
```

- Apply database migrations 🛠️

```bash
python.exe .\manage.py migrate  
```

-Populate the database with initial data 🌱

```bash
 python .\manage.py populate_employees
```

-Run the application 🚀

```bash
 python .\manage.py runserver
```

- In browser open  http://127.0.0.1:8000/ url

## Creating a Superuser in Django

### To create an admin (superuser) account, follow these steps:

- Run the createsuperuser command 👤

```bash
python manage.py createsuperuser
```

Follow the prompts to enter your username, email, and password 🔑

- You will be prompted to enter a username.
- Enter an email address.
- Enter and confirm your password.
- Access the Django admin interface 🛡️

Open your browser and go to: http://127.0.0.1:8000/admin/

Log in with the superuser credentials you just created.

Feel free to reach out if you encounter any issues or have questions! Happy coding! 💻✨