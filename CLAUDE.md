# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django 6.0.3 web application for registering and listing security cameras. The project is in Spanish (locale `es-mx`, timezone `America/Mexico_City`).

## Environment Setup

Python 3.12 is required (see `.python-version`). The virtual environment is `.venvProyCamara/`.

```bash
source .venvProyCamara/bin/activate
```

The `.env` file must exist at the project root with `SECRET_KEY` set (see `.env` for the current dev key).

## Common Commands

```bash
# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create new migrations after model changes
python manage.py makemigrations

# Run all tests
python manage.py test

# Run tests for the camaras app only
python manage.py test camaras

# Create admin superuser
python manage.py createsuperuser
```

## Architecture

```
Proyecto/        # Django project config (settings, root urls, wsgi/asgi)
camaras/         # Single app — all camera logic lives here
  models.py      # Camara model: empresa, nombre, modelo, serie, ip, mac
  views.py       # Function-based views: registrar_camara, lista_camaras
  forms.py       # CamaraForm (ModelForm for Camara)
  urls.py        # Mounted at /camaras/ in Proyecto/urls.py
  admin.py       # Camara registered in Django admin
  templates/     # registrar_camara.html, lista_camaras.html
  migrations/    # 0001_initial.py exists
```

**URL routes:**
- `GET/POST /camaras/registrar/` — register a new camera
- `GET /camaras/` — list all cameras
- `/admin/` — Django admin panel

**Data flow:** `CamaraForm` (ModelForm) → `registrar_camara` view saves to SQLite via the `Camara` model → redirects to `lista_camaras`.

Templates use no base template or static files yet — they are bare HTML with inline Django template tags.
