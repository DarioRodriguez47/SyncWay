# SyncWave

SyncWave es una aplicación web fullstack para streaming y gestión de música, desarrollada con Angular (frontend) y Flask (backend), usando PostgreSQL como base de datos y Docker para facilitar la instalación.

## Requisitos
- Node.js >= 18
- Python >= 3.11
- Docker y Docker Compose
- Git

## Instalación rápida

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/estevan-j/SyncWave.git
   cd SyncWave/MonoliticVersion
   ```

2. **Levanta la base de datos y backend con Docker:**
   ```bash
   docker-compose up --build
   ```
   Esto crea y configura la base de datos PostgreSQL y el backend Flask.

3. **Instala dependencias del frontend:**
   ```bash
   cd fronted
   npm install
   ```

4. **Levanta el frontend Angular:**
   ```bash
   npm run dev
   ```
   El frontend estará disponible en `http://localhost:4200`.

## Estructura del proyecto
- `backend/` - Código fuente del backend Flask
- `fronted/` - Código fuente del frontend Angular
- `database/` - Scripts de inicialización y migración de la base de datos
- `docker-compose.yml` - Orquestación de servicios con Docker
- `public/logo.png` - Logo principal de la app

## Variables de entorno
Puedes configurar variables en un archivo `.env` en la raíz de `backend/`:
```
DATABASE_URL=postgresql://syncwave:syncwave@db:5432/syncwave
SECRET_KEY=tu_clave_secreta
FLASK_DEBUG=True
```

## Inicialización de la base de datos
Los scripts en `database/init/` se ejecutan automáticamente al levantar Docker. Si necesitas resetear la base de datos:
```bash
docker-compose down -v
docker-compose up --build
```

## Migraciones y datos de ejemplo
- `database/init/01-init-database.sql` - Crea tablas y extensiones
- `database/init/02-seed-data.sql` - Inserta datos de ejemplo (usuarios, canciones, favoritos)

## Notas para desarrolladores
- El backend corre en el puerto 5000 (`http://localhost:5000`)
- El frontend corre en el puerto 4200 (`http://localhost:4200`)
- El archivo `requirements.txt` en `backend/` contiene las dependencias de Python
- El archivo `package.json` en `fronted/` contiene las dependencias de Node

## Preguntas frecuentes
- Si tienes problemas con Docker, asegúrate de que los puertos 5432 y 5000 estén libres.
- Si el frontend no carga el logo, verifica que `fronted/public/logo.png` exista.
- Para desarrollo local sin Docker, puedes usar SQLite cambiando la variable `DATABASE_URL`.

## Licencia
MIT

---

¿Dudas o problemas? Abre un issue en el repositorio o contacta al autor.

# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)