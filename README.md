# 🖥️ Portafolio Backend (Dockerizado)

Backend de la plataforma de portafolios para programadores, construida con Django y Django REST Framework, preparada para ejecutarse con Docker.

---

## 🎯 Objetivo

Permitir a desarrolladores crear, personalizar y compartir su portafolio profesional mediante una URL única:

```
https://portafolio.maria/
https://portafolio.pedro/
```

---

## 🛠 Tecnologías

* Django 4+
* Django REST Framework
* PostgreSQL
* Docker y Docker Compose
* Pipenv (opcional para desarrollo local)
* Despliegue en AWS (Free Tier)

---

## 🚀 Características Principales

* Registro y autenticación de usuarios.
* CRUD de perfiles y proyectos.
* Vista pública del portafolio.
* Subdominios personalizados por usuario.
* Panel de administración para usuarios y staff.
* Configuración modular de settings para entornos dev/prod.

---

## 📂 Estructura del Proyecto

```
portafolio-backend/
├── apps/
│   ├── users/
│   └── portfolios/
├── portafolio_backend/
│   └── settings/
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ⚙️ Requisitos

* Docker
* Docker Compose

---

## 🚧 Configuración Inicial (Modo Local)

1. **Crea y activa un entorno virtual** (opcional pero recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

3. **Crea un archivo `.env` con las variables necesarias** (versión local mínima):

```env
DJANGO_SECRET_KEY=tu_clave_secreta_aqui
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

4. **Aplica las migraciones a la base de datos**:

```bash
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

## 🐳 Configuración y Uso con Docker

1. **Clona el repositorio**:

```bash
git clone https://github.com/tu_usuario/portafolio-backend.git
cd portafolio-backend
```

2. **Crea el archivo `.env` para variables de entorno** (ejemplo mínimo):

```env
POSTGRES_DB=portafolio
POSTGRES_USER=portafolio
POSTGRES_PASSWORD=portafolio
DJANGO_SECRET_KEY=tu_clave_secreta_aqui
DJANGO_DEBUG=True
```

3. **Construye y levanta los contenedores con Docker Compose**:

```bash
docker-compose up --build
```

4. **(Opcional) Crea un superusuario**:

```bash
docker-compose exec web python manage.py createsuperuser
```

5. **Accede a la aplicación en**:

```
http://localhost:8000/
```

---

## 📝 Notas

* El contenedor `web` expone el puerto 8000 para acceso local.
* La base de datos PostgreSQL se levanta en el contenedor `db`.
* La configuración de Django está modularizada en `settings/dev.py` y `settings/prod.py` para distintos entornos.
* Ajusta las variables de entorno en `.env` según tu entorno de producción o desarrollo.
* Para desarrollo local, puedes usar volúmenes para que los cambios en el código se reflejen sin reconstruir la imagen.

---

## 🤝 Contribuciones

* Usa branches con metodología **Gitflow** y pull requests para contribuir.
* Abre issues para reportar errores o sugerir mejoras.
* Colabora en GitHub Projects para seguimiento de tareas.

---

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia **MIT**.

---

¡Gracias por colaborar!

---
