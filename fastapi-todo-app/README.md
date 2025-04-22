# FastAPI Todo Application

This project is a simple Todo application built with FastAPI. It allows users to manage their todo items with features to create, read, update, and delete tasks. The application is structured to follow best practices for FastAPI development and is containerized using Docker.

## Project Structure

```
fastapi-todo-app
├── app
│   ├── main.py            # Entry point of the FastAPI application
│   ├── models.py          # Database models using SQLAlchemy
│   ├── routes
│   │   └── todos.py       # Route definitions for managing todos
│   ├── schemas.py         # Pydantic schemas for request and response validation
│   ├── database.py        # Database connection and session management
│   └── __init__.py        # Marks the app directory as a Python package
├── Dockerfile              # Instructions for building the Docker image
├── requirements.txt        # Python dependencies required for the project
├── docker-compose.yml      # Defines services for Docker Compose
└── README.md               # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-todo-app
   ```

2. **Build the Docker image:**
   ```
   docker build -t fastapi-todo-app .
   ```

3. **Run the application using Docker Compose:**
   ```
   docker-compose up
   ```

4. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000`. You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Usage

- **Create a Todo:** Send a POST request to `/todos/` with a JSON body containing the title of the todo.
- **Read Todos:** Send a GET request to `/todos/` to retrieve all todos.
- **Update a Todo:** Send a PUT request to `/todos/{todo_id}` with a JSON body containing the updated title and completed status.
- **Delete a Todo:** Send a DELETE request to `/todos/{todo_id}` to remove a todo.

## Dependencies

The project requires the following Python packages:

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

These dependencies are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.