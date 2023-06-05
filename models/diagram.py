from typing import Any
from bson import ObjectId
from pydantic import BaseModel, PrivateAttr
from db import diagrams_collection


class DiagramModel(BaseModel):
    _id: ObjectId | None = PrivateAttr(None)
    name: str
    description: str
    shapes: Any

    _collection = diagrams_collection

    @classmethod
    async def find(cls, **lookup) -> "DiagramModel":
        result = await cls._collection.find_one(lookup)
        model = cls(**result)
        model._id = result["_id"]
        return model

    @classmethod
    async def get_by_id(cls, id: str) -> "DiagramModel":
        return await cls.find(_id=ObjectId(id))

    async def save(self) -> "DiagramModel":
        if self._id is None:
            result = await self._collection.insert_one(
                self.dict()
            )
            self._id = result.inserted_id
        else:
            await self._collection.replace_one(
                {"_id": self._id}, self.dict()
            )
        return self
