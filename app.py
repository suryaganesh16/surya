"""
Agricultural Organic Farming Advisor
A Flask web application to help farmers replace chemical fertilizers with
organic alternatives and get crop-specific recommendations.
"""

import os
from flask import Flask, render_template, request, session, redirect, url_for
import agricultural_data as data

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "organic-farming-advisor-secret-key")


@app.route("/", methods=["GET"])
def index():
    """Step 1: Collect basic farmer details."""
    return render_template("index.html")


@app.route("/land-details", methods=["POST"])
def land_details():
    """Step 2: Collect land & season details after saving basic info."""
    # Validate and save basic farmer details to session
    farmer = {
        "name": request.form.get("name", "").strip(),
        "phone": request.form.get("phone", "").strip(),
        "village": request.form.get("village", "").strip(),
        "pincode": request.form.get("pincode", "").strip(),
        "area": request.form.get("area", "").strip(),
        "area_unit": request.form.get("area_unit", "acres").strip(),
        "crop": request.form.get("crop", "").strip(),
    }

    errors = {}
    if not farmer["name"]:
        errors["name"] = "Farmer name is required."
    if not farmer["phone"] or not farmer["phone"].isdigit() or len(farmer["phone"]) < 10:
        errors["phone"] = "Enter a valid 10-digit phone number."
    if not farmer["village"]:
        errors["village"] = "Village name is required."
    if not farmer["pincode"] or not farmer["pincode"].isdigit() or len(farmer["pincode"]) != 6:
        errors["pincode"] = "Enter a valid 6-digit pincode."
    if not farmer["area"]:
        errors["area"] = "Land area is required."
    if not farmer["crop"]:
        errors["crop"] = "Crop name is required."

    if errors:
        return render_template("index.html", errors=errors, form=farmer)

    session["farmer"] = farmer
    return render_template(
        "land_details.html",
        soil_types=data.SOIL_TYPES,
        seasons=data.SEASONS,
        water_levels=data.WATER_LEVEL_LABELS,
        farmer=farmer,
    )


@app.route("/fertilizer-select", methods=["POST"])
def fertilizer_select():
    """Step 3: Collect soil/season/water details and show fertilizer selection."""
    farmer = session.get("farmer")
    if not farmer:
        return redirect(url_for("index"))

    land = {
        "soil_type": request.form.get("soil_type", "").strip(),
        "water_level": request.form.get("water_level", "").strip(),
        "season": request.form.get("season", "").strip(),
        "weather": request.form.get("weather", "").strip(),
        "soil_ph": request.form.get("soil_ph", "").strip(),
        "soil_health": request.form.get("soil_health", "").strip(),
    }

    errors = {}
    if not land["soil_type"] or land["soil_type"] not in data.SOIL_TYPES:
        errors["soil_type"] = "Please select a valid soil type."
    if not land["water_level"] or land["water_level"] not in data.WATER_LEVELS:
        errors["water_level"] = "Please select water availability."
    if not land["season"] or land["season"] not in data.SEASONS:
        errors["season"] = "Please select a crop season."
    if not land["weather"]:
        errors["weather"] = "Please describe the weather/climate."

    if errors:
        return render_template(
            "land_details.html",
            errors=errors,
            form=land,
            soil_types=data.SOIL_TYPES,
            seasons=data.SEASONS,
            water_levels=data.WATER_LEVEL_LABELS,
            farmer=farmer,
        )

    session["land"] = land

    # Get crop recommendations for this combination
    soil_crops = data.CROP_RECOMMENDATIONS.get(land["soil_type"], {})
    water_crops = soil_crops.get(land["water_level"], {})
    recommended_crops = water_crops.get(land["season"], [])

    return render_template(
        "fertilizer_select.html",
        farmer=farmer,
        land=land,
        recommended_crops=recommended_crops,
        chemical_fertilizers=data.CHEMICAL_FERTILIZERS,
        water_level_label=data.WATER_LEVEL_LABELS.get(land["water_level"], land["water_level"]),
    )


@app.route("/recommendations", methods=["POST"])
def recommendations():
    """Step 4: Generate organic farming recommendations."""
    farmer = session.get("farmer")
    land = session.get("land")
    if not farmer or not land:
        return redirect(url_for("index"))

    selected_fertilizers = request.form.getlist("fertilizers")
    if not selected_fertilizers:
        # Redirect back if nothing selected
        soil_crops = data.CROP_RECOMMENDATIONS.get(land["soil_type"], {})
        water_crops = soil_crops.get(land["water_level"], {})
        recommended_crops = water_crops.get(land["season"], [])
        return render_template(
            "fertilizer_select.html",
            farmer=farmer,
            land=land,
            recommended_crops=recommended_crops,
            chemical_fertilizers=data.CHEMICAL_FERTILIZERS,
            water_level_label=data.WATER_LEVEL_LABELS.get(land["water_level"], land["water_level"]),
            error="Please select at least one chemical fertilizer to replace.",
        )

    # Build fertilizer replacement info
    fertilizer_recs = []
    for fert in selected_fertilizers:
        if fert in data.FERTILIZER_REPLACEMENTS:
            fertilizer_recs.append(
                {"chemical": fert, "info": data.FERTILIZER_REPLACEMENTS[fert]}
            )

    # Soil health advice
    soil_advice = data.SOIL_HEALTH_ADVICE.get(land["soil_type"], {})

    # Crop suitability recommendations
    soil_crops = data.CROP_RECOMMENDATIONS.get(land["soil_type"], {})
    water_crops = soil_crops.get(land["water_level"], {})
    recommended_crops = water_crops.get(land["season"], [])

    # Crop-specific tips for farmer's chosen crop
    crop_tip_key = next(
        (k for k in data.CROP_SPECIFIC_TIPS if farmer["crop"].lower() in k.lower()),
        None,
    )
    crop_tips = data.CROP_SPECIFIC_TIPS.get(crop_tip_key) if crop_tip_key else None

    # Organic spray recommendations
    organic_sprays = data.ORGANIC_SPRAYS["general"]

    return render_template(
        "recommendations.html",
        farmer=farmer,
        land=land,
        fertilizer_recs=fertilizer_recs,
        soil_advice=soil_advice,
        recommended_crops=recommended_crops,
        crop_tips=crop_tips,
        organic_sprays=organic_sprays,
        water_level_label=data.WATER_LEVEL_LABELS.get(land["water_level"], land["water_level"]),
    )


@app.route("/restart")
def restart():
    """Clear session and restart the form."""
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, host="0.0.0.0", port=5000)
