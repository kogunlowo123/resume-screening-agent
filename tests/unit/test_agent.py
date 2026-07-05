"""Resume Screening Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_parse_resume():
    """Test Parse a resume into structured candidate profile data."""
    tools = AgentTools()
    result = await tools.parse_resume(resume_file="test", format="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_match_requirements():
    """Test Match candidate profile against job requirements."""
    tools = AgentTools()
    result = await tools.match_requirements(candidate_profile="test", job_requirements="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_score_candidate():
    """Test Score a candidate on fit, experience, and skill alignment."""
    tools = AgentTools()
    result = await tools.score_candidate(candidate_id="test", job_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_skill_gaps():
    """Test Identify skill gaps between candidate profile and job requirements."""
    tools = AgentTools()
    result = await tools.detect_skill_gaps(candidate_profile="test", job_requirements="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.resume_screening_agent_agent import ResumeScreeningAgentAgent
    agent = ResumeScreeningAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
