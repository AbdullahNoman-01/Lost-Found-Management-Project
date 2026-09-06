# Lost & Found Management System

A Django-based web application for reporting, searching, and managing lost and found items. The platform helps people share item information, browse reports, and reconnect belongings with their owners.

## Features

- Submit lost-item reports with descriptions, dates, locations, contact information, categories, and images
- Submit found-item reports with the same details
- Browse separate lost-item and found-item listings
- Search reports by item name, description, location, or category
- Sort reports by item name or report date
- View full item details
- Update or delete existing reports
- Upload and serve item images during development
- Responsive interface styled with Bootstrap and custom CSS

## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL through `DATABASE_URL` (configured with `dj-database-url`)
- **Frontend:** Django Templates, Bootstrap 5, Bootstrap Icons, custom CSS and JavaScript
- **Forms:** Django Crispy Forms with the Bootstrap 5 template pack
- **Image handling:** Pillow

## Project Structure

```text
.
├── authentication/      # Authentication app
├── found_items/         # Found-item models, forms, views, templates, and styles
├── lost_items/          # Lost-item models, forms, views, templates, and styles
├── main_campus/         # Django project settings, URLs, WSGI, and ASGI
├── media/               # Uploaded media files
├── static/              # Source static assets
├── staticfiles/         # Collected static files
├── templates/           # Shared templates
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- PostgreSQL
- Git

## Installation and Setup

1. Clone the repository and enter the project directory:

   ```bash
   git clone <repository-url>
   cd Lost-Found-Management-Project
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root. Set `DATABASE_URL` to your PostgreSQL connection string:

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/lost_found_db
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. (Optional) Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Main URLs

| Purpose | URL |
| --- | --- |
| Home page | `/` |
| Report a lost item | `/lost_items/form/` |
| Browse lost items | `/lost_items/views/` |
| Report a found item | `/found_items/form/` |
| Browse found items | `/found_items/view/` |
| Django admin | `/admin/` |

Each item listing also provides links to view, update, and delete an individual report.

## Development Commands

Run Django's system checks:

```bash
python manage.py check
```

Run the test suite:

```bash
python manage.py test
```

Collect static files for deployment:

```bash
python manage.py collectstatic
```

## Environment and Deployment Notes

- Keep `.env` and all credentials out of version control.
- Set a strong production `SECRET_KEY` and turn `DEBUG` off before deployment.
- Configure `ALLOWED_HOSTS` for the production domain.
- Use a production-ready PostgreSQL database and web server.
- Configure persistent storage for uploaded files under `MEDIA_ROOT`.
- Configure a web server or object storage to serve collected static files.

## License

This project is intended for educational and community use. Add a project-specific license before distributing it as open-source software.
