from fastapi import APIRouter
from pydantic import BaseModel
from ..services.ai_service import simple_search

router = APIRouter(prefix="/api/ai", tags=["ai"])

class QueryIn(BaseModel):
    query: str

class QueryOut(BaseModel):
    answer: str
    source: str | None = None

@router.post("/query", response_model=QueryOut)
def query_ai(q: QueryIn):
    answer = simple_search(q.query)
    return {"answer": answer, "source": None}
