from fastapi import APIRouter
from schemas import NameDescriptionSchema
from services import DiagramsService


router = APIRouter(prefix="/diagrams")


@router.post("/")
async def new_diagram(data: NameDescriptionSchema):
    return await DiagramsService.new(data)

@router.get("/{diagram_oid}/")
async def get_diagram(diagram_oid: str):
    return await DiagramsService.get(diagram_oid)

@router.get("/{diagram_oid}/shapes")
async def get_diagram_shapes(diagram_oid: str):
    return await DiagramsService.get_shapes(diagram_oid)
