"""Resume Screening Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class CandidateProfile(BaseModel):
    """CandidateProfile for Resume Screening Agent."""
    name: str
    email: str
    skills: list[str]
    experience_years: float
    education: list[dict]
    work_history: list[dict]


class ScreeningResult(BaseModel):
    """ScreeningResult for Resume Screening Agent."""
    candidate_id: str
    overall_score: float
    requirement_match_pct: float
    skill_gaps: list[str]
    recommendation: str

