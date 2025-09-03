# ISES Field Operations App

This repository contains the initial backend scaffold for the ISES field operations management system. The application is built with FastAPI and will include modules for authentication, route planning, failed visit alerts, vehicle management, and reporting.

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn backend.main:app --reload
```

These endpoints are currently available:

- `GET /health` – basic health check
- `POST /login` – placeholder for authentication
- `POST /routes` – placeholder for route generation
