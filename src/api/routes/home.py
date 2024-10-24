from fastapi import APIRouter, Request
from src.api.authentication import login_required

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
@login_required
async def my_informations(request: Request):
    return {'user': request.current_user}



