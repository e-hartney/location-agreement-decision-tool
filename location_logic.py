from dataclasses import dataclass
from typing import List

@dataclass
class LocationAssessmentResult:
    inform_legal: bool
    legal_reasons: List[str]  
    clearance_tasks: List[str]
    production_tasks: List[str]
    contract_riders: List[str]

def assess_location_request(
    key_location: bool,
    location_outside_main_filming_country: bool,
    owner_type: str,
    public_access: bool,
    residential_area: bool,
    visible_artwork_or_brands: bool,
    unusual_personal_data_risk: bool,
    unaccompanied_minors_present: bool,
    non_routine_structural_changes: bool,
    pyrotechnics: bool,
    drones: bool,
    animals: bool,
    extreme_stunts: bool,
    crowd_scene: bool,
    limited_parking: bool,
) -> LocationAssessmentResult:
    inform_legal = False
    legal_reasons = []
    clearance_tasks = []
    production_tasks = []
    contract_riders = []

    # Inform legal team
    if key_location:
        inform_legal = True
        legal_reasons.append("key location")  
        # legal will need to allocate resources
   
    if location_outside_main_filming_country:
        inform_legal = True
        legal_reasons.append("location outside main filming country") 
        
    if owner_type == "charity" or owner_type == "other":
        inform_legal = True
        legal_reasons.append("owner is charity or non-standard entity")

    if unusual_personal_data_risk:
        inform_legal = True
        legal_reasons.append("unusual personal data risk")  
        # Legal may need to provide further policy framework and/or privacy notices/consents

    if unaccompanied_minors_present:
        inform_legal = True
        legal_reasons.append("unaccompanied minors likely to be present")  
        # Legal may need to provide further policy framework and/or parental consent forms
    
    if non_routine_structural_changes:
        inform_legal = True
        legal_reasons.append("non-routine structural changes required")

    # Inform other teams
    if visible_artwork_or_brands:
        clearance_tasks.append("artworks / brands visible at location")

    if public_access:
        production_tasks.append("public access / notice to public required")

    if residential_area:
        production_tasks.append("residential area / notices to residents required")

    if limited_parking:
        production_tasks.append("limited parking / plan required")

    if drones:
        production_tasks.append("drone use / check logistics and permissions")
        # drones included in standard contract template

    if animals:
        production_tasks.append("animal use / plan logistics on property")
        # animals included in standard contract template

    # Riders to include in contract
    if pyrotechnics: 
        contract_riders.append("pyrotechnics rider")

    if extreme_stunts: 
        contract_riders.append("extreme stunts rider")

    if crowd_scene: 
        contract_riders.append("crowd rider")
    
    return LocationAssessmentResult(
        inform_legal = inform_legal,
        legal_reasons = legal_reasons,
        clearance_tasks = clearance_tasks,
        production_tasks = production_tasks,
        contract_riders = contract_riders,
    )   
