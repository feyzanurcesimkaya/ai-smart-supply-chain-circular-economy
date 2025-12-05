from .models import Shipment, ShipmentSet, EmissionResult

EMISSION_FACTORS = {
    "road": 0.1,
    "sea": 0.015,
    "air": 0.6,
}


def estimate_shipment_emissions(shipment: Shipment) -> float:
    factor = EMISSION_FACTORS.get(shipment.mode, EMISSION_FACTORS["road"])
    return shipment.distance_km * shipment.weight_tons * factor


def estimate_set_emissions(shipment_set: ShipmentSet) -> EmissionResult:
    per_shipment = [estimate_shipment_emissions(s) for s in shipment_set.shipments]
    total = sum(per_shipment)
    return EmissionResult(total_kg_co2e=total, per_shipment_kg_co2e=per_shipment)
