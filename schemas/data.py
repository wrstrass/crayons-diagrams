from pydantic import BaseModel


class NameDescriptionSchema(BaseModel):
    name: str
    description: str
