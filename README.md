# 🖥️ Portafolio Backend

Backend de la plataforma de portafolios para programadores, construida con Django y Django REST Framework.

---

## 🎯 Objetivo

Permitir a desarrolladores crear, personalizar y compartir su portafolio profesional mediante una URL única:

```
[https://portafolio.maria/](https://portafolio.maria/)
[https://portafolio.pedro/](https://portafolio.pedro/)
```

---

## 🛠 Tecnologías

- Django 4+
- Django REST Framework
- PostgreSQL
- Pipenv
- Despliegue en AWS (Free Tier)

---

## 🚀 Características Principales

- Registro y autenticación de usuarios.
- CRUD de perfiles y proyectos.
- Vista pública del portafolio.
- Subdominios personalizados por usuario.
- Panel de administración para usuarios y staff.

---

## 📂 Estructura del Proyecto

```
portafolio-backend/
├── apps/
│   ├── users/
│   └── portfolios/
├── portafolio\_backend/
│   └── settings/
├── manage.py
├── Pipfile
└── requirements.txt
````

---

## ⚙️ Requisitos

- Python 3.11+
- Pip (gestor de paquetes)
- Virtualenv o Pipenv (opcional pero recomendado)
- PostgreSQL (configurado en `settings.py`, o puedes usar SQLite para pruebas locales)

---

## 🚧 Configuración Inicial

1. **Clona el repositorio**:

```bash
git clone https://github.com/tu_usuario/portafolio-backend.git
cd portafolio-backend
````

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Aplica las migraciones a la base de datos**:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crea un superusuario** para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

6. **Inicia el servidor de desarrollo**:

```bash
python manage.py runserver
```

7. **Accede a la aplicación en**:

```
http://127.0.0.1:8000/
```

---

## 📝 Notas

* Configura tu base de datos en `settings.py` si quieres usar PostgreSQL u otra base de datos.
* Para pruebas rápidas puedes usar la base de datos SQLite por defecto.
* Recomendamos usar un entorno virtual para evitar conflictos con otras instalaciones de Python.

---

## 🤝 Contribuciones

* Por favor, usa branches siguiendo la metodología **Gitflow** y pull requests para contribuir.
* Puedes abrir issues o colaborar en tareas desde GitHub Projects.

---

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia **MIT**.

---

¡Gracias por colaborar!

---
