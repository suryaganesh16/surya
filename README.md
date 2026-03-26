# 🌱 Organic Farming Advisor

A web application that helps farmers replace chemical fertilizers with organic
alternatives, recommends suitable crops for their land, and provides soil-health
guidance based on ancient and modern organic farming practices.

---

## Features

| Step | What it does |
|------|-------------|
| **1 – Farmer Details** | Collects name, phone, village, pincode, crop, and land area |
| **2 – Land & Season** | Captures soil type, water availability, crop season, weather, and optional soil pH / health issues |
| **3 – Fertilizer Choice** | Displays crops suitable for the land; farmer selects which chemical fertilizers to replace |
| **4 – Recommendations** | Full organic report: fertilizer replacements, soil amendments, biofertilizers, pH management, crop schedule, and organic sprays |

### Highlights

* **8 chemical fertilizers** mapped to organic alternatives (Urea → Vermicompost / Neem Cake, DAP → Bone Meal / Rock Phosphate, MOP → Wood Ash, etc.)
* **7 soil types** with tailored organic amendments and biofertilizer recommendations
* **Crop suitability matrix** across 7 soil types × 3 water levels × 3 seasons (Kharif / Rabi / Zaid)
* **Organic pest / disease sprays** (Neem oil, Jeevamrut, Trichoderma, etc.) to replace pesticides
* Printable recommendation report

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the development server
python app.py
```

Open http://localhost:5000 in your browser.

---

## Project Structure

```
surya/
├── app.py                      # Flask application & routes
├── agricultural_data.py        # Knowledge base (fertilizers, crops, soil advice)
├── requirements.txt
├── tests.py                    # Pytest test suite
├── templates/
│   ├── base.html
│   ├── index.html              # Step 1: Farmer details
│   ├── land_details.html       # Step 2: Land & season
│   ├── fertilizer_select.html  # Step 3: Choose fertilizers to replace
│   └── recommendations.html   # Step 4: Full organic report
└── static/
    └── style.css
```

---

## Running Tests

```bash
pip install pytest
pytest tests.py -v
```

---

## Organic Fertilizer Replacements Covered

| Chemical Fertilizer | Key Organic Alternatives |
|---------------------|--------------------------|
| Urea | Vermicompost, Neem Cake, Green Manure |
| DAP | Bone Meal, Rock Phosphate, Fish Meal |
| MOP | Wood Ash, Banana Peel Compost, Seaweed Extract |
| SSP | Bone Meal, Compost + Rock Phosphate |
| NPK | Vermicompost + Neem Cake + Wood Ash blend, Biofertilizer consortium |
| Zinc Sulphate | Zinc-enriched Vermicompost |
| Ammonium Sulphate | Green Manure + Gypsum |
| CAN | Jeevamrut, Fish Amino Acid |

---

## Acknowledgements

Built with [Flask](https://flask.palletsprojects.com/) · Promotes traditional organic and ancient Indian farming methods.
