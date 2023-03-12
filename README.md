# CRUD Application

## Description

    - This is a simple CRUD app that allows you to create, read, update and delete Notes.
    - The backend is written in Python using FastAPI and Postgres as the database.
    - The frontend is written in HTML, CSS and Javascript and using Bootstrap for styling.
    - Using nginx as a reverse proxy to serve the frontend and backend.
    - Using docker-compose to run the app.
    - The backend port is 8080 and the frontend port is 5050.

## Start

Run the following commands to start the app:

    ```shell
        sudo docker-compose up -d --build
    ```

## Endpoints

    - GET /notes/{user_name}
    - GET /notes/{note_id}
    - POST /add_notes
    - PUT /delete_note/{note_id}
    - DELETE /update_note/{note_id}
