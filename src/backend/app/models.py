from pydantic import BaseModel, Field
from typing import Literal, List

ModeType = Literal["road", "air", "sea"]


class Shipment(BaseModel):
    origin_country: str = Field(...)
    destination_country: str = Field(...)
    distance_km: float = Field(..., ge=0)
    weight_tons: float = Field(..., ge=0)
    mode: ModeType
    scenario: str = Field("baseline")


class ShipmentSet(BaseModel):
    shipments: List[Shipment]


class EmissionResult(BaseModel):
    total_kg_co2e: float
    per_shipment_kg_co2e: List[float]


class ScenarioComparisonRequest(BaseModel):
    baseline: ShipmentSet
    improved: ShipmentSet


class ScenarioComparisonResult(BaseModel):
    baseline_total_kg_co2e: float
    improved_total_kg_co2e: float
    improvement_kg_co2e: float
    improvement_percent: float
