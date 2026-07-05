"""Test configuration for Resume Screening Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "resume-screening-agent", "category": "Human Resources"}
