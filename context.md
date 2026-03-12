# context.md — Contexto del Proyecto SistemaCamaras

> **Regla importante:** Este archivo debe actualizarse cada vez que se realice una nueva implementación, ya sea agregar modelos, vistas, formularios, rutas, templates, integraciones externas o cualquier cambio significativo en la arquitectura. No omitir este paso al finalizar una tarea.

---

## Descripción general

Sistema web desarrollado en **Django 6.0.3** con **Python 3.12** para el registro y consulta de cámaras de seguridad en una organización. El sistema permite registrar cámaras con sus datos de identificación de red y pertenencia a empresa, y listarlas en una tabla.

El idioma del proyecto es **español** (locale `es-mx`, zona horaria `America/Mexico_City`).

---

## Estado actual del proyecto

**Versión:** 0.1.0
**Rama principal:** `v1`
**Base de datos:** SQLite (`db.sqlite3`)
**Fecha de inicio:** 2026-03-07

### Funcionalidades implementadas

| Funcionalidad | Estado |
|---|---|
| Modelo `Camara` | Implementado |
| Formulario `CamaraForm` | Implementado |
| Vista: registrar cámara | Implementado |
| Vista: listar cámaras | Implementado |
| Admin Django para `Camara` | Implementado |
| Templates básicos (sin estilos) | Implementado |

---

## Modelo de datos

### `Camara` (`camaras/models.py`)

| Campo | Tipo Django | Descripción |
|---|---|---|
| `id` | `BigAutoField` (PK auto) | Identificador interno |
| `empresa` | `CharField(100)` | Empresa a la que pertenece la cámara |
| `nombre` | `CharField(100)` | Nombre descriptivo de la cámara |
| `modelo` | `CharField(100)` | Modelo del equipo |
| `serie` | `CharField(100)` | Número de serie |
| `ip` | `GenericIPAddressField` | Dirección IP (IPv4 o IPv6) |
| `mac` | `CharField(17)` | Dirección MAC (formato `XX:XX:XX:XX:XX:XX`) |

---

## Estructura de URLs

| URL | View | Nombre | Método |
|---|---|---|---|
| `/admin/` | Django Admin | — | GET/POST |
| `/camaras/` | `lista_camaras` | `lista_camaras` | GET |
| `/camaras/registrar/` | `registrar_camara` | `registrar_camara` | GET, POST |

---

## Flujo principal de datos

```
Usuario
  └─► POST /camaras/registrar/
        └─► CamaraForm.is_valid()
              └─► form.save() → Camara (SQLite)
                    └─► redirect → /camaras/
                          └─► Camara.objects.all() → lista_camaras.html
```

---

## Estructura de archivos relevantes

```
SistemaCamaras/
├── .env                          # SECRET_KEY (no commitear en producción)
├── .python-version               # Python 3.12
├── .venvProyCamara/              # Entorno virtual
├── manage.py
├── pyproject.toml
├── db.sqlite3                    # Base de datos SQLite
├── Proyecto/                     # Configuración del proyecto Django
│   ├── settings.py               # Carga .env, locale es-mx, ALLOWED_HOSTS='*'
│   ├── urls.py                   # Raíz: /admin/ y /camaras/
│   ├── wsgi.py
│   └── asgi.py
└── camaras/                      # App principal
    ├── models.py                 # Modelo Camara
    ├── views.py                  # registrar_camara, lista_camaras
    ├── forms.py                  # CamaraForm (ModelForm)
    ├── urls.py                   # Rutas de la app
    ├── admin.py                  # Registro en Django Admin
    ├── tests.py                  # (vacío — pendiente)
    ├── migrations/
    │   └── 0001_initial.py       # Migración inicial (2026-03-07)
    └── templates/
        ├── lista_camaras.html    # Tabla HTML con todas las cámaras
        └── registrar_camara.html # Formulario de registro
```

---

## Dependencias instaladas

Gestionadas en el entorno virtual `.venvProyCamara/` (Python 3.12):

- `Django 6.0.3`
- `asgiref`
- `sqlparse`
- `python-dotenv` (carga de variables de entorno desde `.env`)

---

## Pendientes / Deuda técnica

- Tests unitarios en `camaras/tests.py` (actualmente vacío)
- Templates sin estilos CSS ni base template compartida
- Sin validación personalizada en el formulario (ej. formato MAC)
- `ALLOWED_HOSTS = ['*']` — ajustar antes de producción
- `DEBUG = True` — cambiar para producción
- El archivo `main.py` en la raíz no tiene uso funcional actualmente

---

## Historial de implementaciones

| Fecha | Descripción |
|---|---|
| 2026-03-07 | Creación inicial del proyecto Django, modelo `Camara`, vistas CRUD básicas, templates HTML simples |
| 2026-03-11 | Generación de `CLAUDE.md` y `context.md` para documentación del proyecto |
