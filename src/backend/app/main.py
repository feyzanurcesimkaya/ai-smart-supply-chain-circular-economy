from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import ShipmentSet, EmissionResult, ScenarioComparisonRequest, ScenarioComparisonResult
from .calculator import estimate_set_emissions

app = FastAPI(
    title="AI-Powered Smart Supply Chain API",
    description="Prototype API for estimating logistics emissions and comparing scenarios.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}


@app.post("/shipments/estimate-emissions", response_model=EmissionResult, tags=["emissions"])
def estimate_emissions(payload: ShipmentSet):
    return estimate_set_emissions(payload)


@app.post("/scenarios/compare", response_model=ScenarioComparisonResult, tags=["emissions"])
def compare_scenarios(payload: ScenarioComparisonRequest):
    baseline_res = estimate_set_emissions(payload.baseline)
    improved_res = estimate_set_emissions(payload.improved)

    improvement = baseline_res.total_kg_co2e - improved_res.total_kg_co2e
    percent = 0.0
    if baseline_res.total_kg_co2e > 0:
        percent = improvement / baseline_res.total_kg_co2e * 100.0

    return ScenarioComparisonResult(
        baseline_total_kg_co2e=baseline_res.total_kg_co2e,
        improved_total_kg_co2e=improved_res.total_kg_co2e,
        improvement_kg_co2e=improvement,
        improvement_percent=percent,
    )
