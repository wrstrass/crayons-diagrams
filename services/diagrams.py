from models import DiagramModel
from schemas import NameDescriptionSchema, DiagramSchema


class DiagramsService:
    @staticmethod
    async def new(data: NameDescriptionSchema) -> DiagramSchema:
        diagram = DiagramModel(**data.dict())
        await diagram.save()
        return DiagramSchema.from_model(diagram)

    @staticmethod
    async def get(oid: str) -> DiagramSchema:
        diagram = await DiagramModel.get_by_id(oid)
        return DiagramSchema.from_model(diagram)

    @staticmethod
    async def get_shapes(oid: str) -> DiagramSchema:
        diagram = await DiagramModel.get_by_id(oid)
        return diagram.shapes
