# 🎒 Campus Lost & Found Management System

A modern web-based **Lost & Found Management System** built with **Python and Django**, designed to help students and campus members report, search, and manage lost and found items through a centralized platform.

🌐 **Live Demo:** https://lost-found-management-project.onrender.com/
💻 **GitHub Repository:** https://github.com/AbdullahNoman-01/Lost-Found-Management-Project

---

## 📌 Project Overview

The **Campus Lost & Found Management System** provides a centralized platform where users can report lost or found belongings and easily browse existing reports.

The system focuses on making the process of reporting and recovering lost items **simple, organized, and user-friendly**.

### Users can:

* 🔐 Create an account and log in
* 👤 Manage their profile
* 📢 Report lost items
* 📦 Report found items
* 🔎 Search and browse reported items
* 🖼️ Upload item images
* 📄 View detailed item information
* ✏️ Update their own reports
* 🗑️ Delete their own reports
* 👥 See who reported an item
* 🏫 Manage campus-related lost and found information

---

## ✨ Key Features

### 🔐 Authentication & User Management

The project includes a complete authentication system for user-based access.

* User registration
* User login
* User logout
* User profile
* User-specific reports
* Authentication-based navigation
* Login-required protection for reporting items

---

### 🔴 Lost Item Management

Users can report belongings they have lost.

Features include:

* Create lost item reports
* Add item name and description
* Select item category
* Add lost date
* Add lost location
* Provide contact information
* Upload item images
* View detailed lost item information
* Search lost item reports
* Update own reports
* Delete own reports

---

### 🟢 Found Item Management

Users can also report items they have found.

Features include:

* Create found item reports
* Add item name and description
* Select item category
* Add found date
* Add found location
* Provide contact information
* Upload item images
* View detailed found item information
* Search found item reports
* Update own reports
* Delete own reports

---

## 🔎 Search & Discovery

The system allows users to search through lost and found reports using relevant information.

Search can be performed using:

* 🔤 Item name
* 📝 Description
* 📍 Location
* 🏷️ Category

This makes it easier for users to discover potentially matching items.

---

## 🤖 AI Search

The project also includes an **AI Search** section prepared for future intelligent search functionality.

The planned concept includes:

* Intelligent item searching
* Lost and found item matching
* AI-assisted discovery
* Potential image similarity matching

> 🚧 AI-powered matching functionality is currently planned for a future update.

---

## 👤 User Profile

Each authenticated user has a profile section where they can manage their account and view their activity.

The profile system provides information about:

* Username
* User information
* Lost reports
* Found reports
* User activity

Users can also manage their own submitted reports.

---

## 🔒 Owner-Based Report Management

Users can only modify reports that they created.

### Report owner can:

* ✏️ Update the report
* 🗑️ Delete the report

Other users can view the report but cannot modify or delete someone else's report.

This provides an additional layer of access control for user-generated content.

---

## 🖼️ Image Upload

Users can upload images while creating lost or found reports.

Images help users identify reported belongings more easily and provide additional visual information about an item.

Django's media handling system is used for uploaded files.

---

## 📱 User Interface

The project includes a responsive and modern interface designed with:

* Bootstrap
* Custom CSS
* Bootstrap Icons
* Responsive navigation
* Responsive cards
* User-friendly forms
* Custom alerts and notifications
* Mobile-friendly layouts

The interface is designed to provide a clean experience across desktop and mobile devices.

---

## 🗂️ Project Structure

```text
Lost-Found-Management-Project/
│
├── about/                  # About section
├── ai_search/              # AI Search functionality
├── authentications/        # Authentication & profile
├── found_items/            # Found item management
├── lost_items/             # Lost item management
├── main_campus/            # Main pages and homepage
│
├── media/                  # Uploaded media files
├── static/                 # CSS, JavaScript and static assets
├── staticfiles/            # Collected static files
├── templates/              # HTML templates
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

| Technology               | Purpose                   |
| ------------------------ | ------------------------- |
| 🐍 Python                | Backend Programming       |
| 🌐 Django                | Web Framework             |
| 🖥️ HTML5                | Page Structure            |
| 🎨 CSS3                  | User Interface            |
| 🧩 Bootstrap             | Responsive UI             |
| 🗄️ Database             | Data Storage              |
| 🖼️ Django Media         | Image Upload & Management |
| 📂 Django Static Files   | Frontend Static Assets    |
| 🔐 Django Authentication | User Authentication       |
| 🔧 Git & GitHub          | Version Control           |
| 🚀 Render                | Deployment                |

---

## 🔄 Application Workflow

```text
                       ┌───────────────────┐
                       │       User        │
                       └─────────┬─────────┘
                                 │
                     ┌───────────┴───────────┐
                     │                       │
              ┌──────▼──────┐         ┌──────▼──────┐
              │  Lost Item  │         │ Found Item  │
              │    Report   │         │    Report   │
              └──────┬──────┘         └──────┬──────┘
                     │                       │
                     └───────────┬───────────┘
                                 │
                         ┌───────▼────────┐
                         │ Browse & Search │
                         │     Reports     │
                         └───────┬────────┘
                                 │
                         ┌───────▼────────┐
                         │ View Item      │
                         │ Details        │
                         └────────────────┘
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AbdullahNoman-01/Lost-Found-Management-Project.git
cd Lost-Found-Management-Project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

The project is deployed using **Render**.

### Live Application

🌐 https://lost-found-management-project.onrender.com/

The deployed application provides access to the main homepage, authentication system, lost item reports, found item reports, search functionality, and user profile features.

---

## 📁 Django Applications

### `lost_items`

Responsible for:

* Lost item reports
* Lost item details
* Lost item search
* Report update
* Report deletion
* Image uploads

### `found_items`

Responsible for:

* Found item reports
* Found item details
* Found item search
* Report update
* Report deletion
* Image uploads

### `authentications`

Responsible for:

* Registration
* Login
* Logout
* User profile
* User-specific activity

### `main_campus`

Responsible for:

* Homepage
* Main navigation
* Campus-related pages
* Common project functionality

### `ai_search`

Prepared for future intelligent search and matching functionality.

### `about`

Contains information about the project and its purpose.

---

## 🔐 Security & Access Control

The application uses Django's authentication and authorization features to protect user-specific functionality.

Examples include:

* Authentication-required report creation
* User-specific report ownership
* Owner-only update access
* Owner-only delete access
* Protected profile functionality

This ensures users cannot modify reports created by other users.

---

## 🚀 Future Improvements

The project can be extended with several advanced features:

* 🤖 AI-powered lost & found matching
* 🧠 Automatic item matching
* 🖼️ AI image similarity search
* 📧 Email notifications
* 🔔 Real-time notifications
* 📍 Improved location-based search
* 🏷️ Advanced category filtering
* 📊 Admin analytics dashboard
* 📱 Progressive Web App (PWA)
* 💬 User-to-user communication
* ✅ Item recovery/claim status
* 🔍 More advanced search filters

---

## 🎯 Project Goal

The main goal of this project is to create a **centralized, secure, and user-friendly Lost & Found platform** that helps campus communities report lost belongings, discover found items, and improve the process of recovering personal belongings.

The system combines **Django backend functionality, authentication, search, image uploads, and responsive UI** into one complete web application.

---

## 👨‍💻 Author

### Abdullah Al Noman

Python & Django Developer

Built with ❤️ using **Python & Django**.

---

## 📄 License

This project is developed for **educational and academic purposes**.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**GitHub:**
https://github.com/AbdullahNoman-01/Lost-Found-Management-Project

**Live Demo:**
https://lost-found-management-project.onrender.com/
