# Usamos la imagen oficial de Python 3.13 (versión slim para que no pese tanto)
FROM python:3.13-slim

# Evita que se generen archivos .pyc y fuerza que los logs salgan directo a la consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos dependencias del sistema esenciales para compilación y PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiamos los requerimientos
COPY requirements.txt .

# Instalamos las dependencias
# Nota: Algunas librerías de IA podrían necesitar actualizar pip en Python 3.13
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos el código del microservicio
COPY . .

# El puerto donde corre tu app (FastAPI suele usar el 8000)
EXPOSE 8000

# Comando para arrancar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]