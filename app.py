# app.py

import streamlit as st
from location_logic import assess_location_request

st.title("Location Agreement Decision Tool")

st.subheader("Location type")
key_location = st.checkbox("Key location (i.e. must be that specific location)")
location_outside_main_filming_country = st.checkbox("Location is outside of main filming country")

owner_type = st.selectbox(
    "Owner type",
    ["private individual", "private company", "public authority", "charity", "other"],
)

st.subheader("Location characteristics")
public_access = st.checkbox("Location will be open to public during filming")
residential_area = st.checkbox("Location is in or near a residential area")
visible_artwork_or_brands = st.checkbox("Artwork or branding visible during filming")
unusual_personal_data_risk = st.checkbox("Risk of exposure to personal data (e.g. location is a working hospital)")
unaccompanied_minors_present = st.checkbox("Unaccompanied minors likely to be present (e.g. location is a working school)")
limited_parking = st.checkbox("Limited parking facilities")

st.subheader("Filming requirements")
non_routine_structural_changes = st.checkbox("Non-routine structural changes required")
pyrotechnics = st.checkbox("Pyrotechnics to be used")
drones = st.checkbox("Drones to be used")
animals = st.checkbox("Animals to be used")
extreme_stunts = st.checkbox("Extreme stunts to be carried out")
crowd_scene = st.checkbox("Crowd scene required")


if st.button("Assess"):
    result = assess_location_request(
    key_location = key_location,
    location_outside_main_filming_country = location_outside_main_filming_country,
    owner_type = owner_type,
    public_access = public_access,
    residential_area =  residential_area,
    visible_artwork_or_brands = visible_artwork_or_brands,
    unusual_personal_data_risk = unusual_personal_data_risk,
    unaccompanied_minors_present = unaccompanied_minors_present,
    non_routine_structural_changes = non_routine_structural_changes,
    pyrotechnics = pyrotechnics,
    drones = drones,
    animals = animals,
    extreme_stunts = extreme_stunts,
    crowd_scene = crowd_scene,
    limited_parking = limited_parking,
)

    if result.inform_legal:
        st.subheader("Contact legal for:")
        for r in result.legal_reasons:
           st.write(f"- {r}")

    if result.clearance_tasks or result.production_tasks:
        st.subheader("Inform the following teams:")

        if result.clearance_tasks:
            st.write("**Clearances:**")
            for r in result.clearance_tasks:
                st.write(f"- {r}")

        if result.production_tasks:
            st.write("**Production:**")
            for r in result.production_tasks:
                st.write(f"- {r}")

    if result.contract_riders:
        st.subheader("Include the following contract riders:")
        for r in result.contract_riders:
           st.write(f"- {r}")
    
    if (len(result.legal_reasons) == 0 and len(result.clearance_tasks) == 0 and len(result.production_tasks) ==0 and len(result.contract_riders) ==0:
        st.write("Proceed with template agreement - contact legal with any queries")

