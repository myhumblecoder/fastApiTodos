from fastapi import FastAPI
from app.routes import todos
from app.database import init_db

init_db()

app = FastAPI()

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Todo App!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)