# DEVOPS-Projekt: Todo-List CRUD-Service

Dieses Projekt implementiert einen einfachen CRUD-Service für eine Todo-Liste auf Basis von **Python FastAPI**.  
Schwerpunkt liegt auf den DevOps-Aspekten: Containerisierung mit Docker und CI/CD mit GitHub Actions.

## Funktionen / REST-API

Der Service stellt folgende Endpoints bereit:

- `GET /todos` – Liefert alle Todos.  
- `GET /todos/{id}` – Liefert ein einzelnes Todo nach ID.  
- `POST /todos` – Erstellt ein neues Todo.  
- `PATCH /todos/{id}` – Aktualisiert ein bestehendes Todo teilweise.  
- `DELETE /todos/{id}` – Löscht ein Todo.  
- `GET /health` – Einfache Health-Check-Route, um zu prüfen, ob der Service läuft.

## Voraussetzungen

- Docker installiert (Docker Desktop oder Docker Engine).
- Zugriff auf dieses Repository (Code und GitHub Actions Workflows).

## Service lokal mit Docker starten

1. Repository klonen:

   ```bash
   git clone https://github.com/mwalexandra/devops-todo-microservice.git
   cd devops-todo
   ```

2. Docker-Image lokal bauen:

   ```bash
   docker build -t devops-todo .
   ```

3. Container starten:

   ```bash
   docker run -p 8000:8000 devops-todo
   ```

4. Im Browser oder mit `curl` prüfen, ob der Service läuft:

   - Health-Check:  
     `http://localhost:8000/health`  
   - Todos-API (Beispiel):  
     `http://localhost:8000/todos`

## Service aus GitHub Container Registry starten (optional)

Das Image wird automatisch von GitHub Actions gebaut und in die **GitHub Container Registry (GHCR)** gepusht.

1. Docker-Image aus GHCR ziehen (Beispiel, Namen ggf. anpassen):

   ```bash
   docker pull ghcr.io/mwalexandra/devops-todo-microservice:latest
   ```

2. Container starten:

   ```bash
   docker run -p 8000:8000 ghcr.io/mwalexandra/devops-todo-microservice:latest
   ```

3. Erneut `http://localhost:8000/health` aufrufen, um den laufenden Service zu überprüfen.

## CI/CD mit GitHub Actions

- Ein **CI-Workflow** installiert bei jedem Push die Python-Abhängigkeiten und führt Tests aus. 
- Ein weiterer Workflow baut automatisch ein Docker-Image und pusht es in die GitHub Container Registry (`ghcr.io`).
