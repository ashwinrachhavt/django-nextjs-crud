from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Task

api = NinjaAPI()

class TaskSchema(Schema):
    id: int
    title: str
    description: str = None
    done: bool
    created_at: str
    updated_at: str

@api.get("/tasks", response=list[TaskSchema])
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks

@api.post("/tasks", response=TaskSchema)
def create_task(request, task: TaskSchema):
    task = Task.objects.create(**task.dict())
    return task

@api.get("/tasks/{task_id}", response=TaskSchema)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    return task

@api.put("/tasks/{task_id}", response=TaskSchema)
def update_task(request, task_id: int, data: TaskSchema):
    task = get_object_or_404(Task, id=task_id)
    for attr, value in data.dict().items():
        setattr(task, attr, value)
    task.save()
    return task

@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"success": True}

@api.post("/tasks/{task_id}/done")
def toggle_task_done(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return {"status": "Task done" if task.done else "Task undone"}
