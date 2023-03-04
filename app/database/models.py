from pydantic import BaseModel

class NewTable(BaseModel):
    id: str
    name: str
    description: str
