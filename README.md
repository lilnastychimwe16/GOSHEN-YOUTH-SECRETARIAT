# Secretariat Desk Web Application

A web-based platform for church secretaries to manage and track financial records, including Freewill Offerings, Zonal Obligations, and District Obligations.

## Features

- User Authentication System
- Freewill Offerings Management
- Zonal Obligations Tracking
- District Obligations Management
- Dashboard with Financial Overview

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `secretariat_desk/` - Main project directory
- `core/` - Core application for authentication and base functionality
- `offerings/` - Freewill offerings management
- `obligations/` - Zonal and district obligations management
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images) 