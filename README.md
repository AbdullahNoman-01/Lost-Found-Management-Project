🎒 Campus Lost & Found Management System

A web-based Lost & Found Management System built with Python and Django.
The project is designed to help campus users report lost or found items and make it easier to manage and find those items through a centralized platform.

📌 Project Overview

The Campus Lost & Found Management System provides a simple platform where users can:

🔐 Create an account and authenticate securely (future updated)

📢 Report lost items

📦 Report found items

🔎 Browse lost and found item reports

🏫 Manage campus-related lost and found information

🖼️ Upload and manage item images

🎨 Use static CSS and frontend assets for a better user experience

The main goal is to reduce the difficulty of recovering lost belongings on campus by keeping reports organized in one place.

✨ Main Features

🔐 Authentication (future updated)

User registration and login

User authentication

Protected user-related functionality

🔴 Lost Items

Submit lost item reports

Store item information

Display reported lost items

Support item images/media

🟢 Found Items

Submit found item reports

Store found item information

Display reported found items

Support item images/media

🏫 Main Campus

Central area for the main project pages

Homepage and common project functionality

🖼️ Media Management

Uploaded item images are stored in the media/ directory.

🎨 Static Files

CSS and other frontend assets are organized inside the static/ directory.

Collected static files can be stored in staticfiles/.

🗂️ Project Structure

assignment-8/
│
├── authentication/       # User authentication and account functionality (future updated)
│
├── found_items/          # Found item reporting and management
│
├── lost_items/           # Lost item reporting and management
│
├── main_campus/          # Main pages and campus-related functionality
│
├── media/                # Uploaded item images and media
│
├── static/               # CSS, JavaScript and frontend static assets
│
├── staticfiles/          # Collected static files
│
├── templates/             # Django HTML templates
│
├── manage.py              # Django project management script
│
├── requirements.txt       # Python project dependencies
│
└── .gitignore             # Git ignored files and directories

🛠️ Technology Stack

Technology

Purpose

🐍 Python

Backend programming

🌐 Django

Web framework

🖥️ HTML

Page structure

🎨 CSS

User interface styling

🗄️ SQLite / Database

Data storage

🔐 Django Authentication

User authentication

📁 Django Static & Media

Static files and uploaded images

🔧 Git & GitHub

Version control

⚙️ Installation & Setup

1. Clone the repository

git clone <your-repository-url>
cd assignment-8

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

macOS / Linux:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Apply migrations

python manage.py migrate

6. Create a superuser

python manage.py createsuperuser

Follow the terminal instructions to create the admin account.

7. Run the development server

python manage.py runserver

Then open:

http://127.0.0.1:8000/

🔄 Basic Workflow

             ┌──────────────────┐
             │      User        │
             └────────┬─────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
    ┌─────▼─────┐           ┌─────▼─────┐
    │ Lost Item │           │ Found Item│
    │   Report  │           │   Report  │
    └─────┬─────┘           └─────┬─────┘
          │                       │
          └───────────┬───────────┘
                      │
              ┌───────▼────────┐
              │ Browse Reports  │
              │  & Find Items   │
              └─────────────────┘
📁 Important Django Apps

authentication

Handles user authentication and account-related functionality.

lost_items

Contains the functionality for creating and displaying lost item reports.

found_items

Contains the functionality for creating and displaying found item reports.

main_campus

Contains the main project pages and common campus-related functionality.

🔒 Security

For production deployment, make sure to:

Set DEBUG = False

Configure ALLOWED_HOSTS

Keep the Django SECRET_KEY private

Configure a production database

Configure secure static/media file serving

Never commit passwords, API keys, or secret configuration files

🚀 Future Improvements

Some possible future improvements include:

🤖 AI-powered item search

🔍 Advanced search and filtering

📍 Location-based item matching

🧠 Automatic matching between lost and found reports

📧 Email notifications

🔔 Real-time notifications

📱 Responsive mobile interface

🖼️ AI-based image similarity search

👤 User dashboard

📊 Admin analytics and reporting

🎯 Project Goal

The goal of this project is to create a simple, organized, and user-friendly campus platform where lost and found items can be reported, discovered, and managed efficiently.

👨‍💻 Author

Abdullah Al Noman

Built with ❤️ using Python & Django.

📄 License

This project is created for educational and project-development purposes.
