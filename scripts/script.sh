#!/bin/bash
set -e

# Create virtual environment with uv
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install fastapi sqlalchemy pytest pytest-cov ruff pyre-check uvicorn

# Create project directory structure
mkdir -p src/domain/{entities,value_objects,services}
mkdir -p src/application/{dtos,interfaces,use_cases}
mkdir -p src/infrastructure/{persistence/models,persistence/repositories,services}
mkdir -p src/api/routes
mkdir -p tests/{domain,application,infrastructure,api}

# Initialize database
python -c "from src.infrastructure.persistence.database import init_db; init_db()"