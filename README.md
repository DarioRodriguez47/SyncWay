SyncWave
SyncWave es una plataforma de reproducción de música que permite a los usuarios escuchar, gestionar playlists y explorar canciones. El proyecto está disponible en dos versiones: Monolítica y Microservicios.

Características principales
Reproductor de música con interfaz web moderna
Gestión de usuarios y autenticación
Creación y administración de playlists
Visualización de dashboards y métricas (monitoring)
Arquitectura escalable con microservicios y gateway
Integración con Docker para despliegue sencillo
Estructura del proyecto
MonoliticVersion/: Implementación monolítica con backend y frontend integrados.
MicroserviceVersion/: Implementación basada en microservicios (usuarios, música, gateway, monitoring, frontend).
Instalación rápida
Clona el repositorio:

Despliega con Docker (microservicios):

Accede a la aplicación web en tu navegador en http://localhost:4200 (o el puerto configurado).

Tecnologías utilizadas
Angular (Frontend)
Python (Flask, Backend)
Nginx (Gateway)
Docker & Docker Compose
Prometheus & Grafana (Monitoring)
Contribuir
¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT.
