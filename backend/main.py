# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Todo, TodoCreate, TodoUpdate

app = FastAPI()

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (replace with a database in production)
todos: dict[int, Todo] = {}
next_id = 1

@app.get("/todos", response_model=list[Todo])
def list_todos():
    """Get all todos"""
    return list(todos.values())

@app.post("/todos", response_model=Todo)
def create_todo(todo_data: TodoCreate):
    """Create a new todo"""
    global next_id

    todo = Todo(
        id=next_id,
        title=todo_data.title,
        completed=todo_data.completed
    )
    todos[next_id] = todo
    next_id += 1

    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """Get a specific todo"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_data: TodoUpdate):
    """Update a todo"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo = todos[todo_id]

    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    return todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    """Delete a todo"""
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    del todos[todo_id]
