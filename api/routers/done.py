from fastapi import APIRouter

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_done(task_id: int):
    return


@router.delete("/tasks/{task_id}/done", response_model=None)
async def mark_task_undone(task_id: int):
    return
