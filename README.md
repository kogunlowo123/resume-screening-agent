# Resume Screening Agent

[![CI](https://github.com/kogunlowo123/resume-screening-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/resume-screening-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI-powered resume screening agent that parses resumes, extracts structured candidate profiles, scores against job requirements, detects skill gaps, and ranks applicants for recruiter review with bias-mitigation controls.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `parse_resume` | Parse a resume into structured candidate profile data |
| `match_requirements` | Match candidate profile against job requirements |
| `score_candidate` | Score a candidate on fit, experience, and skill alignment |
| `detect_skill_gaps` | Identify skill gaps between candidate profile and job requirements |
| `rank_candidates` | Rank a pool of candidates for a position |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/screening/parse` | Parse resume |
| `POST` | `/api/v1/screening/match` | Match requirements |
| `POST` | `/api/v1/screening/score` | Score candidate |
| `POST` | `/api/v1/screening/gaps` | Detect skill gaps |
| `POST` | `/api/v1/screening/rank` | Rank candidates |

## Features

- Resume Parsing
- Requirement Matching
- Candidate Scoring
- Skill Gap Analysis
- Bias Mitigation

## Integrations

- Greenhouse
- Lever
- Workday
- Icims
- Linkedin Recruiter

## Architecture

```
resume-screening-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── resume_screening_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ATS + NLP + Resume Parser**

---

Built as part of the Enterprise AI Agent Platform.
