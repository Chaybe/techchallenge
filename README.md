# TechChallenge

This project consists of a **Django backend** and an **Angular frontend**.  
Below are the instructions to set up and run both environments.

---

## Prerequisites

Make sure you have the following tools installed on your machine:

- **Docker** and **Docker Compose** (to run the backend)
- **Node.js** (version 16 or higher) and **npm** (to run the frontend)
- **Python** (version 3.11 or higher)

---

## Backend

The backend is implemented in Django and uses Celery for asynchronous tasks.

### Setup and Run with Docker

1. Make sure Docker and Docker Compose are installed.
2. In the root directory of the project, run the following command to start the services:
   ```sh
   docker-compose up --build
   ```
3. The backend will be available at `http://localhost:8000`.

### Running Celery

1. Ensure Redis is running (already configured in `docker-compose.yml`).
2. Start Celery:
   ```sh
   celery -A techchallenge worker --loglevel=info
   ```

---

## Frontend

The frontend is implemented in Angular.

### Setup and Run

1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   ng serve
   ```
   or
   ```sh
   npm start
   ```
4. The frontend will be available at `http://localhost:4200`.

---

## Project Structure

- **Backend**: Located in the `techchallenge` and `calc` directories.
- **Frontend**: Located in the `frontend` directory.

---

## Notes

- Make sure both the backend and the frontend are running simultaneously for the application to work properly.
- For more information about Angular CLI, visit the [Angular CLI Overview and Command Reference](https://angular.io/cli).

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/8b80e27e-a1f5-499c-b063-c0e0a2a5f439" width="700" />
</p>

## Usage

- Enter numbers in the fields (int or float)
- Confirm the process by clicking the button
- After a few seconds (`sleep(3)`), the project will display the average, median, and process status


---
## EXTRA
UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A


Enjoy!
