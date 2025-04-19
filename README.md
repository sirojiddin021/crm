CRM – Django DRF Project
Project Purpose
This project is designed for internal use in a company to manage tasks between managers and employees, and to maintain effective communication with clients.
Managers assign tasks to employees, and each task is directly linked to a client.


Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL

Authentication: JWT-based or DRF Auth

API Docs: Swagger


Project Setup

git clone https://github.com/your-username/crm.git
cd crm
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
