from pydantic import BaseModel
from models import DiagramModel


class DiagramSchema(BaseModel):
    id: str
    name: str
    description: str

    @classmethod
    def from_model(cls, diagram: DiagramModel) -> "DiagramSchema":
        return DiagramSchema(
            id=str(diagram._id),
            name=diagram.name,
            description=diagram.description,
        )
