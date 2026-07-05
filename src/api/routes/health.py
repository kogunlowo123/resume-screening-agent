"""Resume Screening Agent - Health Check Routes."""

import time
from fastapi import APIRouter
from src.config import get_settings

router = APIRouter(tags=["Health"])
settings = get_settings()
_start_time = time.time()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "agent": settings.app_name,
        "version": "1.0.0",
        "uptime_seconds": round(time.time() - _start_time, 2),
        "features": ['resume_parsing', 'requirement_matching', 'candidate_scoring', 'skill_gap_analysis', 'bias_mitigation'],
    }
