from fastapi import APIRouter, HTTPException
from ..agents.registry import AGENTS
from ..core.gemini_client import run_gemini
from ..schemas.execute import ExecuteRequest, ExecuteResponse

router = APIRouter(prefix="/agents", tags=["agents"])

@router.get("/")
def list_agents():
    return list(AGENTS.values())

@router.post("/{agent_id}/execute", response_model=ExecuteResponse)
def execute(agent_id: str, payload: ExecuteRequest):
    if agent_id not in AGENTS:
        raise HTTPException(status_code=404, detail="Agente não encontrado.")

    agent = AGENTS[agent_id]
    prompt = f"{agent['prompt_base']}\n\nUsuário pediu: {payload.message}"

    response = run_gemini(prompt)

    return ExecuteResponse(
        agent_id=agent_id,
        response=response
    )
