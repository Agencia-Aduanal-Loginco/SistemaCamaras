# SistemaCamaras

Sistema de control de mantenimientos de camaras de seguridad, desarrollado con Django 6.0.

## Tecnologías

- **Backend:** Django 6.0, Python 3.12
- **Base de datos:** SQLite (desarrollo) / PostgreSQL (producción)
- **Reconocimiento facial:** OpenCV, face_recognition *(próximamente)*
- **Frontend:** Tailwind CSS *(próximamente)*
- **Autenticación:** JWT *(próximamente)*

## Estructura del proyecto

```
SistemaCamaras/
├── Proyecto/          # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── camaras/           # App de gestión de cámaras
│   ├── models.py      # Modelo Camara (empresa, nombre, modelo, serie, IP, MAC)
│   ├── views.py       # Vistas: registro y listado de cámaras
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── manage.py
├── requirements.txt
└── .env               # Variables de entorno (SECRET_KEY)
```

## Requisitos previos

- Python 3.12+
- pip

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd SistemaCamaras
```

2. Crear y activar entorno virtual:

```bash
python -m venv .venvProyCamara
source .venvProyCamara/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:

Crear un archivo `.env` en la raíz del proyecto:

```
SECRET_KEY=tu-clave-secreta
```

5. Aplicar migraciones:

```bash
python manage.py migrate
```

6. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

## Uso

- **Registrar cámara:** `/camaras/registrar/`
- **Listar cámaras:** `/camaras/`

## Licencia

Este proyecto es de uso privado.