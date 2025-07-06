# WebApp Starter: Python + React + Docker

This repository is a starter template for building full-stack web applications using **React** (frontend), **Python** (backend), and **Docker** for containerization.

## 📁 Project Structure

```
webapp-starter-python-react/
├── frontend/ # React application
└── backend/ # Python backend application
```

---

## 🚀 Getting Started

### 1. Clone the Template

Use this repository as a GitHub **template**, or clone it directly:

```bash
git clone https://github.com/your-username/webapp-starter-python-react.git
cd webapp-starter-python-react
```


### 2. Add env files

To run the app the first time, create empty _.env_ files in both frontend and backend folders. As you customize ypur app, ypu should add env variables accordingly

### 3. Start with Docker

> [!NOTE]
> Make sure you have Docker and Docker Compose installed.
> Remember to start Docker or Docker Desktop

Then run:

```bash
docker compose up --build
```

This will:

- Build the React frontend.
- Build and run the Python backend.
- Expose both services on their default ports (customizable in docker-compose.yml).

- React app can be tested through this link [http://localhost:3000/](http://localhost:3000/)
- Backend app can tested using CURL from terminal:

```bash
curl -X GET http://localhost:8000/health
```

You should see in terminal

```bash
{"status":"ok"}
```

### 📦 Folder Details

_frontend/_

- Contains the React application.
- Modify as needed using your preferred libraries (e.g., TailwindCSS, Axios, etc.)
  backend/
- Contains the Python backend application.
- Uses FastAPI.
  Ready for API creation and integration with the frontend.

### 🛠️ Customization

- Add dependencies to frontend/package.json or backend/requirements.txt.
- Adjust docker-compose.yml for ports, volumes, and environment variables.

### 📄 License

MIT — feel free to use and modify for your own projects.
