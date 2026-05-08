# dockers-files-novasysia
Control de Docker para la configuración de soluciónese en Novasysia
# 🧠 NovasysIA Infrastructure - Docker Architecture

Este repositorio contiene la configuración de infraestructura basada en Docker para múltiples servicios utilizados en una arquitectura moderna orientada a microservicios, automatización e integración.

## ⚙️ Servicios incluidos

- 🔹 API Backend (Laravel - Modular)
- 🔹 Frontend / Sites
- 🔹 RabbitMQ (Mensajería orientada a eventos)
- 🔹 n8n (Automatización de flujos)
- 🔹 Moodle (LMS)
- 🔹 Superset (Analítica)
- 🔹 WordPress
- 🔹 Traefik (Reverse Proxy + SSL)

---

## 🏗️ Arquitectura

La arquitectura está basada en contenedores Docker desacoplados:

- Cada servicio corre en su propio contenedor
- Comunicación interna por red Docker
- Exposición externa mediante Traefik (reverse proxy)
- Manejo de dominios y SSL dinámico

---

## 🔁 Flujo general

1. Cliente realiza petición HTTP
2. Traefik enruta hacia el servicio correspondiente
3. API procesa lógica de negocio
4. Eventos se envían a RabbitMQ
5. n8n consume eventos para automatización

---

## 🧰 Tecnologías utilizadas

- Docker & Docker Compose
- Traefik (Reverse Proxy)
- Laravel (Backend API)
- PostgreSQL / MariaDB
- RabbitMQ (Event-driven architecture)
- n8n (Workflow automation)
- Nginx
- Superset (BI)

---

## 🚀 Cómo levantar el entorno (Demo)

```bash
docker-compose up -d
