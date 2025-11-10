# Brigadas - Proyecto Django (skeleton)

Proyecto base generado para realizar la aplicación de gestión de ayudas.

## Estructura
- `brigadas/` - configuración del proyecto
- `core/` - app principal (modelos, admin, API, vistas simples)
- `templates/` - plantillas básicas (Bootstrap)
- `db.sqlite3` - base de datos (no incluida)

## Requisitos
- Python 3.10+
- pip, virtualenv

## Instalación rápida
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accede a `http://127.0.0.1:8000/` y al admin en `/admin/`.

## Despliegue sugerido
Para un despliegue sencillo con SQLite usar **PythonAnywhere** (ideal para prototipos).
