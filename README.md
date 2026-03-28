# ☕ Proyecto Le Petit Café - Guía de Ejecución

Este proyecto es un sistema de autenticación e integración de datos desarrollado con **Flask**, **Auth0** y **MySQL (XAMPP)** para el taller de Ingeniería de Sistemas.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado:
1. **Python 3.x**
2. **XAMPP** (Con los módulos Apache y MySQL activos).
3. Una cuenta en **Auth0** con un "Regular Web Application" configurado.

---

## 🚀 Pasos para ejecutar el proyecto

Sigue estos comandos en la terminal de VS Code en el orden exacto:

### 1. Preparar la Base de Datos (XAMPP)
* Abre el **XAMPP Control Panel**.
* Inicia **Apache** y **MySQL**.
* Crea una base de datos llamada `le_petit_cafe`.
* Importa o crea la tabla `cliente` con las columnas: `id`, `nombre`, `correo`, `tipo_documento`, `numero_documento` y `password`.

### 2. Activar el Entorno Virtual
Este paso carga todas las librerías necesarias (**Flask**, **Authlib**, **SQLAlchemy**).
```bash 
pip install -r requirements.txt

.venv\Scripts\activate

python app.py