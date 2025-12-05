# AI-Powered Smart Supply Chain & Circular Economy Platform

This repository contains the **documentation and prototype implementation** for an
AI-powered platform that helps industrial companies:

- Measure and monitor **carbon footprint** across their supply chains
- Optimize **logistics routes** for lower emissions and cost
- Integrate **circular economy** practices (recycling, reuse, waste reduction)
- Report in a transparent, **CBAM and EU Green Deal–aligned** way

The project was originally prepared as a concept for an innovation / internship project
and is now structured as a professional GitHub portfolio repository.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── SYSTEM_DESIGN.md
│   └── ROADMAP.md
├── diagrams/
│   └── README.md
├── screenshots/
│   └── README.md
└── src/
    ├── backend/
    │   ├── requirements.txt
    │   └── app/
    │       ├── __init__.py
    │       ├── models.py
    │       ├── calculator.py
    │       └── main.py
    └── frontend/
        ├── index.html
        └── README.md
```

## Running the Prototype

### Backend

```bash
cd src/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

Open `src/frontend/index.html` in your browser after starting the backend.
