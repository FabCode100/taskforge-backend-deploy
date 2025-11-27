from pydantic import BaseModel

class ExecuteRequest(BaseModel):
    message: str

class ExecuteResponse(BaseModel):
    agent_id: str
    response: str
