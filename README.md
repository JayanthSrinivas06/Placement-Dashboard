# Job Readiness Portal

A simple full-stack application for managing student job readiness, including job openings and assessments.

## Tech Stack
- **Backend:** Python (FastAPI), SQLite, SQLAlchemy
- **Frontend:** HTML, CSS (Bootstrap), JavaScript (Fetch API)
- **Deployment:** Render (Backend), Netlify (Frontend)

## Project Structure
- `backend/`: Contains the FastAPI application and database logic.
- `frontend/`: Contains the static HTML files for Admin and Student interfaces.

## How to Run Locally

### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:5000`.

### Frontend
1. Open `frontend/index.html` in your web browser.
2. Use the tabs to switch between Student and Admin login.
3. **Important:** For local testing, ensure the `API_BASE` variable in the script section of HTML files is set to `http://localhost:5000`.

## Deployment (Single Repository)

You can push both `backend` and `frontend` folders to **one GitHub repository**.

### Backend (Render)
1. Create a new Web Service on Render.
2. Connect your GitHub repository.
3. **Important:** In the settings, find **Root Directory** and set it to `backend`.
4. Set the **Build Command** to: `pip install -r requirements.txt`
5. Set the **Start Command** to: `uvicorn main:app --host 0.0.0.0 --port 5000`
6. Copy the deployed URL (e.g., `https://your-app.onrender.com`).

### Frontend (Netlify)
1. Create a new site on Netlify ("Import from Git").
2. Connect the same GitHub repository.
3. **Important:**
   - **Base directory:** `frontend`
   - **Publish directory:** `frontend` (or leave empty if Base directory is set, Netlify usually detects it)
4. **Update API URL:** Before deploying, update the `API_BASE` variable in both `admin.html` and `student.html` to your Render backend URL.

## Note
This is a student assignment project. Passwords are stored in plain text for simplicity. **Do not use this for real production data.**

## Features
- **Admin:** Manage students, jobs, and assessments. Assign assessments to students.
- **Student:** View profile, opt-in/withdraw from jobs, view assigned assessments.
