from fastapi import FastAPI
from .schemas import Task
from .sender import send_task

app = FastAPI()


@app.get("/")
async def index():
    print("index")
    return {"Hello": "World"}


@app.post("/add_task")
async def add_task(task: Task):
    print("add_task")
    await send_task(task)
    return task
