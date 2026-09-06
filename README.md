# 🎒 Campus Lost & Found Management System

A web-based **Lost & Found Management System** built with **Python and Django**.

This project is designed to help campus users report lost and found items and make it easier to manage and discover those items through a centralized platform.

---

## 📌 Project Overview

The **Campus Lost & Found Management System** provides a platform where users can:

- 📢 Report lost items
- 📦 Report found items
- 🔎 Browse lost and found item reports
- 🏫 Manage campus-related lost and found information
- 🖼️ Upload item images
- 🎨 View information through a simple and user-friendly interface

The main goal of this project is to make it easier for students and campus members to report and recover lost belongings.

---

## ✨ Main Features

### 🔴 Lost Items

- Submit lost item reports
- Store item information
- Display reported lost items
- Upload item images
- View lost item details

### 🟢 Found Items

- Submit found item reports
- Store found item information
- Display reported found items
- Upload item images
- View found item details

### 🏫 Main Campus

The `main_campus` app contains the main pages and common functionality of the project.

### 🖼️ Media Management

Uploaded item images are stored inside the `media/` directory.

### 🎨 Static Files

CSS and other frontend static files are organized inside the `static/` directory.

---

## 🗂️ Project Structure

```text
assignment-8/
│
├── authentication/       # Authentication functionality (planned)
│
├── found_items/          # Found item reporting and management
│
├── lost_items/           # Lost item reporting and management
│
├── main_campus/          # Main pages and campus-related functionality
│
├── media/                # Uploaded images and media files
│
├── static/               # CSS and other static assets
│
├── staticfiles/          # Collected static files
│
├── templates/            # Django HTML templates
│
├── manage.py              # Django project management script
│
├── requirements.txt       # Project dependencies
│
└── .gitignore             # Git ignored files
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend Programming |
| 🌐 Django | Web Framework |
| 🖥️ HTML | Page Structure |
| 🎨 CSS | User Interface Styling |
| 🗄️ Database | Data Storage |
| 📁 Django Media | Uploaded Images |
| 📂 Django Static Files | CSS and Frontend Assets |
| 🔧 Git | Version Control |

---

## 🔄 Basic Workflow

```text
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
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd assignment-8
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

### 6. Run the Development Server

```bash
python manage.py runserver
```

Then open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## 📁 Django Apps

### `lost_items`

This app handles lost item reports.

Users can submit information about items they have lost and view available lost item reports.

### `found_items`

This app handles found item reports.

Users can submit information about items they have found and view available found item reports.

### `main_campus`

This app contains the main pages and common functionality of the campus project.

### `authentication`

The authentication system is currently **under development** and is planned for a future version.

---

## 🔐 Authentication Status

Authentication functionality has **not been implemented yet**.

Future authentication features may include:

- User Registration
- User Login
- User Logout
- User Profile
- User-specific Lost Item Reports
- User-specific Found Item Reports

---

## 🚀 Future Improvements

The project can be improved by adding the following features:

- 🔐 User Registration and Login
- 👤 User Profile and Dashboard
- 🔎 Advanced Search
- 🏷️ Category-based Filtering
- 📍 Location-based Search
- 🤖 AI-powered Item Search
- 🧠 Automatic Lost & Found Item Matching
- 🖼️ AI-based Image Similarity Search
- 📧 Email Notifications
- 🔔 Real-time Notifications
- 📱 Fully Responsive Mobile Interface
- 📊 Admin Dashboard and Analytics

---

## 🎯 Project Goal

The main goal of this project is to create a **simple, organized, and user-friendly campus Lost & Found platform** where lost and found items can be reported, viewed, and managed efficiently.

---

## 👨‍💻 Author

**Abdullah Al Noman**

Built with ❤️ using **Python & Django**.

---

## 📄 License

This project is developed for **educational and academic purposes**.
