from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class PaperCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=300)
    authors: List[str]
    category: str
    paper_source: str
    abstract: str
    key_insights: List[str]
    methods: str
    results: str
    tags: List[str] = []
    pdf_url: Optional[str] = None


class PaperResponse(PaperCreate):
    id: str
    created_at: datetime
    updated_at: datetime
