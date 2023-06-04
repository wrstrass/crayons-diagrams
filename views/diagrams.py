from fastapi import APIRouter
from schemas import NameDescriptionSchema
from services import DiagramsService


router = APIRouter(prefix="/diagrams")


@router.post("/")
async def new_diagram(data: NameDescriptionSchema):
    return await DiagramsService.new(data)
