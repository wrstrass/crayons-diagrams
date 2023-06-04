from models import DiagramModel
from schemas import NameDescriptionSchema, DiagramSchema


class DiagramsService:
    @staticmethod
    async def new(data: NameDescriptionSchema) -> NameDescriptionSchema:
        diagram = DiagramModel(**data.dict())
        await diagram.save()
        return DiagramSchema.from_model(diagram)
