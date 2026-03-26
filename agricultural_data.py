"""
Agricultural knowledge base for organic farming recommendations.
Contains data about crops, soils, fertilizers, and regional farming practices.
"""

# Chemical fertilizer to organic alternatives mapping
FERTILIZER_REPLACEMENTS = {
    "Urea": {
        "description": "Urea is a high-nitrogen synthetic fertilizer widely used to boost vegetative growth.",
        "organic_alternatives": [
            {
                "name": "Vermicompost",
                "application": "Apply 2–4 tonnes/acre before sowing or as top dressing.",
                "benefits": "Provides slow-release nitrogen, improves soil structure and microbial activity.",
                "preparation": "Prepared from decomposed organic matter using earthworms (Eisenia fetida).",
            },
            {
                "name": "Neem Cake",
                "application": "Apply 100–150 kg/acre, mix into soil before planting.",
                "benefits": "Nitrogen source + natural pest/nematode repellent.",
                "preparation": "By-product of cold-pressed neem oil extraction.",
            },
            {
                "name": "Green Manure (Dhaincha / Sunhemp)",
                "application": "Sow, allow to grow 45–60 days, then incorporate into soil.",
                "benefits": "Fixes atmospheric nitrogen (60–100 kg N/ha), adds organic matter.",
                "preparation": "Grow leguminous crops and plough them in before flowering.",
            },
            {
                "name": "Farmyard Manure (FYM)",
                "application": "Apply 5–10 tonnes/acre, 3–4 weeks before sowing.",
                "benefits": "All-round nutrient supply with nitrogen, phosphorus, and potassium.",
                "preparation": "Decomposed cattle dung, urine, and crop residues.",
            },
        ],
    },
    "DAP (Diammonium Phosphate)": {
        "description": "DAP supplies both nitrogen and phosphorus; essential for root and early crop development.",
        "organic_alternatives": [
            {
                "name": "Bone Meal",
                "application": "Apply 100–200 kg/acre before planting, mix well into soil.",
                "benefits": "Rich in phosphorus (15–20%) and calcium; promotes root development.",
                "preparation": "Ground steamed animal bones, available as powder or granules.",
            },
            {
                "name": "Rock Phosphate",
                "application": "Apply 200–250 kg/acre at least 30 days before sowing.",
                "benefits": "Slow-release phosphorus source; improves phosphorus availability in acidic soils.",
                "preparation": "Naturally mined phosphate rock, used directly or composted.",
            },
            {
                "name": "Vermicompost",
                "application": "Apply 2–4 tonnes/acre as basal dressing.",
                "benefits": "Provides phosphorus along with nitrogen, potassium, and micronutrients.",
                "preparation": "Earthworm-processed organic waste.",
            },
            {
                "name": "Fish Meal",
                "application": "Apply 100–150 kg/acre before planting.",
                "benefits": "High in nitrogen and phosphorus; promotes vigorous seedling growth.",
                "preparation": "Dried and ground fish by-products.",
            },
        ],
    },
    "MOP (Muriate of Potash)": {
        "description": "MOP is the main potassium fertilizer; supports fruit quality, disease resistance, and water uptake.",
        "organic_alternatives": [
            {
                "name": "Wood Ash",
                "application": "Apply 200–300 kg/acre, incorporate into soil before planting.",
                "benefits": "Rich in potassium (5–10%) and calcium; raises soil pH in acidic soils.",
                "preparation": "Ash from burning wood; avoid ash from treated or painted wood.",
            },
            {
                "name": "Banana Peel Compost",
                "application": "Dry and grind banana peels; apply 50–100 kg/acre.",
                "benefits": "High in potassium; also contains phosphorus and magnesium.",
                "preparation": "Dry banana peels, powder, and compost or apply directly.",
            },
            {
                "name": "Compost with Crop Residues",
                "application": "Apply 3–5 tonnes/acre as basal dressing.",
                "benefits": "Broad-spectrum nutrient supply including potassium.",
                "preparation": "Compost crop residues (paddy straw, sugarcane trash) for 60–90 days.",
            },
            {
                "name": "Seaweed Extract",
                "application": "Spray 2–3 ml/litre of water at 15-day intervals.",
                "benefits": "Rich in potassium, micronutrients, and plant growth hormones.",
                "preparation": "Fermented or extracted from marine seaweed species.",
            },
        ],
    },
    "SSP (Single Super Phosphate)": {
        "description": "SSP provides phosphorus and sulphur for root development and protein synthesis.",
        "organic_alternatives": [
            {
                "name": "Bone Meal",
                "application": "Apply 100–200 kg/acre before planting.",
                "benefits": "Natural phosphorus (15–20%) and calcium; improves root growth.",
                "preparation": "Ground steamed animal bones.",
            },
            {
                "name": "Compost + Rock Phosphate Mix",
                "application": "Mix 2 tonnes compost with 100 kg rock phosphate; apply per acre.",
                "benefits": "Slow-release phosphorus; the organic acids in compost enhance rock phosphate availability.",
                "preparation": "Mix compost with rock phosphate and cure for 30 days.",
            },
        ],
    },
    "NPK (Mixed Fertilizer)": {
        "description": "NPK fertilizers provide nitrogen, phosphorus, and potassium together for balanced crop nutrition.",
        "organic_alternatives": [
            {
                "name": "Vermicompost + Neem Cake + Wood Ash Blend",
                "application": "Mix 2 tonnes vermicompost + 100 kg neem cake + 100 kg wood ash per acre as basal dressing.",
                "benefits": "Balanced NPK with additional micronutrients; improves soil health.",
                "preparation": "Mix all three ingredients and apply 2–3 weeks before sowing.",
            },
            {
                "name": "Compost (FYM / Vermicompost)",
                "application": "Apply 5–8 tonnes/acre before planting.",
                "benefits": "Complete nutrient package with N, P, K and micronutrients.",
                "preparation": "Well-decomposed farmyard manure or vermicompost.",
            },
            {
                "name": "Biofertilizers Consortium (Rhizobium + PSB + KSB)",
                "application": "Seed treatment: 250 ml of each biofertilizer per 10 kg seed. Soil application: 2 kg each per acre.",
                "benefits": "Nitrogen fixation (Rhizobium), phosphorus solubilization (PSB), potassium solubilization (KSB).",
                "preparation": "Available as commercial biofertilizer cultures; store at 4–10°C.",
            },
        ],
    },
    "Zinc Sulphate": {
        "description": "Zinc sulphate corrects zinc deficiency; critical for enzyme activity and grain development.",
        "organic_alternatives": [
            {
                "name": "Vermicompost (High Zinc Variety)",
                "application": "Apply 3–4 tonnes/acre with zinc-rich organic amendments.",
                "benefits": "Naturally contains zinc; improves zinc availability over time.",
                "preparation": "Vermicompost enriched with zinc-rich plant material like maize cobs.",
            },
            {
                "name": "Zinc-Enriched Compost",
                "application": "Apply 2–3 tonnes/acre; foliar spray of 0.5% zinc sulphate if deficiency is severe.",
                "benefits": "Slowly releases zinc as organic matter decomposes.",
                "preparation": "Compost prepared with zinc-accumulating plants (e.g., sunflower residues).",
            },
        ],
    },
    "Ammonium Sulphate": {
        "description": "Ammonium sulphate provides nitrogen and sulphur; suitable for alkaline soils.",
        "organic_alternatives": [
            {
                "name": "Green Manure + Gypsum",
                "application": "Incorporate green manure at 40–50 days, add 100–150 kg gypsum/acre.",
                "benefits": "Nitrogen from green manure; sulphur from gypsum (a natural mineral).",
                "preparation": "Sow dhaincha/sunhemp, incorporate before sowing main crop.",
            },
            {
                "name": "Farmyard Manure (FYM)",
                "application": "Apply 8–10 tonnes/acre at least 3 weeks before planting.",
                "benefits": "Broad nitrogen supply; improves soil organic matter.",
                "preparation": "Well-decomposed cattle manure.",
            },
        ],
    },
    "Calcium Ammonium Nitrate (CAN)": {
        "description": "CAN provides quickly available nitrogen and calcium; used as top dressing.",
        "organic_alternatives": [
            {
                "name": "Liquid Vermicompost / Jeevamrut",
                "application": "Apply 200–400 litres/acre as soil drench at 15-day intervals.",
                "benefits": "Quick-acting liquid nitrogen with beneficial microbes; calcium from eggshell additions.",
                "preparation": "Dilute vermicompost leachate 1:10 with water; or prepare jeevamrut from dung + urine + jaggery + flour.",
            },
            {
                "name": "Fish Amino Acid (FAA)",
                "application": "Dilute 1:500 in water, spray or drench at 10-day intervals.",
                "benefits": "Rapidly available amino-nitrogen; improves protein synthesis.",
                "preparation": "Fermented fish waste with jaggery for 30 days.",
            },
        ],
    },
}

# Crop recommendations by soil type, water availability, and season
CROP_RECOMMENDATIONS = {
    "Clay": {
        "high_water": {
            "Kharif": ["Paddy (Rice)", "Sugarcane", "Jute", "Taro"],
            "Rabi": ["Wheat", "Barley", "Mustard"],
            "Zaid": ["Watermelon", "Cucumber", "Bottle Gourd"],
        },
        "medium_water": {
            "Kharif": ["Paddy", "Maize", "Soybean"],
            "Rabi": ["Wheat", "Gram (Chickpea)", "Mustard"],
            "Zaid": ["Cucumber", "Tomato", "Bitter Gourd"],
        },
        "low_water": {
            "Kharif": ["Cotton", "Sorghum (Jowar)"],
            "Rabi": ["Gram (Chickpea)", "Lentil (Masoor)", "Barley"],
            "Zaid": ["Moong Bean"],
        },
    },
    "Sandy": {
        "high_water": {
            "Kharif": ["Groundnut", "Watermelon", "Sweet Potato"],
            "Rabi": ["Potato", "Carrot", "Radish"],
            "Zaid": ["Watermelon", "Muskmelon"],
        },
        "medium_water": {
            "Kharif": ["Groundnut", "Pearl Millet (Bajra)", "Sesame"],
            "Rabi": ["Mustard", "Potato", "Carrot"],
            "Zaid": ["Muskmelon", "Pumpkin"],
        },
        "low_water": {
            "Kharif": ["Pearl Millet (Bajra)", "Sesame", "Moth Bean"],
            "Rabi": ["Mustard", "Coriander"],
            "Zaid": ["Cluster Bean (Guar)"],
        },
    },
    "Loamy": {
        "high_water": {
            "Kharif": ["Paddy", "Sugarcane", "Banana", "Maize"],
            "Rabi": ["Wheat", "Potato", "Mustard", "Peas"],
            "Zaid": ["Vegetables (All types)", "Watermelon"],
        },
        "medium_water": {
            "Kharif": ["Maize", "Cotton", "Soybean", "Sunflower"],
            "Rabi": ["Wheat", "Gram", "Sunflower", "Peas"],
            "Zaid": ["Vegetables", "Sunflower"],
        },
        "low_water": {
            "Kharif": ["Cotton", "Sorghum", "Pulses"],
            "Rabi": ["Gram", "Lentil", "Mustard"],
            "Zaid": ["Cluster Bean"],
        },
    },
    "Black (Regur)": {
        "high_water": {
            "Kharif": ["Cotton", "Sugarcane", "Soybean"],
            "Rabi": ["Wheat", "Gram (Chickpea)", "Safflower"],
            "Zaid": ["Vegetables"],
        },
        "medium_water": {
            "Kharif": ["Cotton", "Soybean", "Sunflower"],
            "Rabi": ["Wheat", "Gram", "Linseed"],
            "Zaid": ["Vegetables"],
        },
        "low_water": {
            "Kharif": ["Sorghum (Jowar)", "Cotton", "Groundnut"],
            "Rabi": ["Gram", "Safflower", "Linseed"],
            "Zaid": ["Cluster Bean"],
        },
    },
    "Red": {
        "high_water": {
            "Kharif": ["Groundnut", "Paddy", "Finger Millet (Ragi)"],
            "Rabi": ["Wheat", "Gram", "Potato"],
            "Zaid": ["Vegetables"],
        },
        "medium_water": {
            "Kharif": ["Groundnut", "Finger Millet", "Pearl Millet"],
            "Rabi": ["Mustard", "Gram", "Groundnut"],
            "Zaid": ["Vegetables", "Sesame"],
        },
        "low_water": {
            "Kharif": ["Finger Millet (Ragi)", "Sorghum", "Horsegram"],
            "Rabi": ["Horsegram", "Lentil"],
            "Zaid": ["Cluster Bean"],
        },
    },
    "Alluvial": {
        "high_water": {
            "Kharif": ["Paddy", "Sugarcane", "Jute", "Banana"],
            "Rabi": ["Wheat", "Mustard", "Potato", "Peas"],
            "Zaid": ["Vegetables (All)", "Watermelon"],
        },
        "medium_water": {
            "Kharif": ["Maize", "Paddy", "Soybean", "Cotton"],
            "Rabi": ["Wheat", "Gram", "Mustard"],
            "Zaid": ["Vegetables"],
        },
        "low_water": {
            "Kharif": ["Pulses", "Sorghum", "Cotton"],
            "Rabi": ["Gram", "Lentil", "Barley"],
            "Zaid": ["Cluster Bean"],
        },
    },
    "Laterite": {
        "high_water": {
            "Kharif": ["Coconut", "Cashew", "Banana", "Paddy"],
            "Rabi": ["Vegetables", "Gram"],
            "Zaid": ["Vegetables"],
        },
        "medium_water": {
            "Kharif": ["Cashew", "Coconut", "Finger Millet"],
            "Rabi": ["Gram", "Horsegram"],
            "Zaid": ["Sesame"],
        },
        "low_water": {
            "Kharif": ["Cashew", "Finger Millet", "Horsegram"],
            "Rabi": ["Horsegram", "Lentil"],
            "Zaid": ["Cluster Bean"],
        },
    },
}

# Soil health feedback and organic amendments by soil type
SOIL_HEALTH_ADVICE = {
    "Clay": {
        "characteristics": "Heavy, water-retentive, prone to waterlogging and compaction; high nutrient content.",
        "challenges": ["Poor drainage", "Root suffocation", "Difficult to till when wet or dry"],
        "organic_amendments": [
            "Add 3–5 tonnes/acre coarse vermicompost or FYM to improve aeration.",
            "Mix 500–800 kg/acre coarse sand or rice husk to break compaction.",
            "Apply green manure (sunhemp/dhaincha) and incorporate at peak growth to improve structure.",
            "Use raised bed planting to improve drainage.",
        ],
        "biofertilizers": ["Azospirillum", "Phosphate Solubilizing Bacteria (PSB)", "Mycorrhiza"],
        "ph_management": "Clay soils are often neutral to slightly acidic (pH 6–7.5). Add wood ash or lime if pH is below 6.",
    },
    "Sandy": {
        "characteristics": "Light, well-drained, low water retention, poor in nutrients; warms up quickly.",
        "challenges": ["Rapid nutrient leaching", "Poor moisture retention", "Low organic matter"],
        "organic_amendments": [
            "Apply 8–10 tonnes/acre FYM or vermicompost to improve water and nutrient retention.",
            "Use mulching (paddy straw, dry leaves) to reduce moisture loss.",
            "Apply compost in split doses to reduce leaching.",
            "Grow cover crops (legumes) to fix nitrogen and add organic matter.",
        ],
        "biofertilizers": ["Azotobacter", "VAM (Vesicular-Arbuscular Mycorrhiza)", "PSB"],
        "ph_management": "Sandy soils are often acidic (pH 5.5–6.5). Apply wood ash or dolomite lime to raise pH.",
    },
    "Loamy": {
        "characteristics": "Ideal agricultural soil; balanced sand, silt, clay; good drainage and moisture retention.",
        "challenges": ["Maintain organic matter as it degrades over time", "Avoid over-tillage"],
        "organic_amendments": [
            "Apply 3–5 tonnes/acre compost or FYM as annual maintenance.",
            "Practice crop rotation with legumes to maintain nitrogen levels.",
            "Use minimum tillage to preserve soil structure.",
            "Apply mulch after planting to conserve moisture.",
        ],
        "biofertilizers": ["Rhizobium (with legumes)", "PSB", "Azospirillum", "Trichoderma"],
        "ph_management": "Loamy soils are typically neutral (pH 6–7). Maintain with regular organic matter addition.",
    },
    "Black (Regur)": {
        "characteristics": "High clay content (montmorillonite), swells when wet and cracks when dry; very fertile; high pH.",
        "challenges": ["Waterlogging in rainy season", "Hard surface crust after rain", "High pH may lock out micronutrients"],
        "organic_amendments": [
            "Apply 3–4 tonnes/acre FYM or vermicompost to improve structure and lower pH gradually.",
            "Use green manure incorporation to prevent surface crusting.",
            "Add 100–150 kg/acre gypsum to improve sodium balance and drainage.",
            "Avoid over-irrigation; use drip or furrow irrigation.",
        ],
        "biofertilizers": ["PSB (especially important due to high pH)", "Azospirillum", "Trichoderma"],
        "ph_management": "Black soils are alkaline (pH 7.5–8.5). Apply organic matter, sulphur-rich amendments, and neem cake to lower pH.",
    },
    "Red": {
        "characteristics": "Iron-rich, well-drained, low in nutrients (N, P), slightly acidic; low water retention.",
        "challenges": ["Low fertility", "Acidic pH", "Iron and aluminium toxicity at very low pH"],
        "organic_amendments": [
            "Apply 5–6 tonnes/acre vermicompost or FYM to improve nutrient levels.",
            "Add 200–300 kg/acre rock phosphate to supplement low phosphorus.",
            "Incorporate leguminous green manure (sunhemp, cowpea) to fix nitrogen.",
            "Use mulching to conserve moisture in the dry season.",
        ],
        "biofertilizers": ["Rhizobium", "PSB", "VAM (Mycorrhiza)", "Azospirillum"],
        "ph_management": "Red soils are acidic (pH 5.5–6.5). Apply 200–300 kg/acre dolomite lime to raise pH to 6–6.5.",
    },
    "Alluvial": {
        "characteristics": "Deposited by rivers; very fertile, rich in minerals; variable texture (sandy to clayey).",
        "challenges": ["Leaching in sandy alluvial", "Compaction in clayey alluvial", "Needs regular organic replenishment"],
        "organic_amendments": [
            "Apply 4–5 tonnes/acre FYM or vermicompost annually.",
            "Practice crop rotation (cereal → legume) to maintain soil health.",
            "Use biofertilizers as seed treatment to reduce fertilizer dependency.",
            "Apply mulch to protect against erosion during heavy rains.",
        ],
        "biofertilizers": ["Rhizobium", "Azotobacter", "PSB", "Trichoderma"],
        "ph_management": "Alluvial soils range from neutral to slightly alkaline (pH 7–8). Regular organic matter addition keeps pH balanced.",
    },
    "Laterite": {
        "characteristics": "Hard, iron/aluminium-rich, low in nutrients; highly acidic; common in tropical regions.",
        "challenges": ["Very low fertility", "Strong acidity", "Aluminium toxicity", "Hard pan formation"],
        "organic_amendments": [
            "Apply 6–8 tonnes/acre vermicompost to overcome severe nutrient deficiency.",
            "Add 300–400 kg/acre dolomite lime to correct strong acidity.",
            "Grow acid-tolerant cover crops (cowpea, sesbania) as green manure.",
            "Deeply incorporate organic matter to break hard laterite crust.",
        ],
        "biofertilizers": ["VAM Mycorrhiza (critical for phosphorus uptake)", "Azospirillum", "Trichoderma"],
        "ph_management": "Laterite soils are strongly acidic (pH 4.5–5.5). Apply 400–500 kg/acre dolomite lime each season.",
    },
}

# Organic pest & disease management sprays (replacing pesticides)
ORGANIC_SPRAYS = {
    "general": [
        {
            "name": "Neem Oil Spray",
            "preparation": "Mix 5 ml neem oil + 1 ml liquid soap in 1 litre water.",
            "application": "Spray every 7–10 days on foliage.",
            "controls": "Aphids, whitefly, mites, scale insects, powdery mildew.",
        },
        {
            "name": "Garlic-Chilli Spray",
            "preparation": "Blend 100 g garlic + 50 g green chilli in 1 litre water; strain and dilute 1:10.",
            "application": "Spray early morning or evening every 10 days.",
            "controls": "Aphids, caterpillars, mites, fungal diseases.",
        },
        {
            "name": "Jeevamrut (Bio-stimulant Spray)",
            "preparation": "Mix 200 g cow dung + 200 ml cow urine + 50 g jaggery + 50 g chickpea flour in 10 litres water; ferment 48 hours.",
            "application": "Dilute 1:10 and spray or drench; apply every 15 days.",
            "controls": "Boosts plant immunity; suppresses soil-borne pathogens.",
        },
        {
            "name": "Buttermilk / Takra Spray",
            "preparation": "Dilute 1 part fresh buttermilk with 10 parts water.",
            "application": "Spray on leaves during early morning.",
            "controls": "Powdery mildew, leaf blight, downy mildew.",
        },
        {
            "name": "Wood Ash Spray",
            "preparation": "Dissolve 100 g wood ash in 1 litre water; filter and dilute 1:5.",
            "application": "Spray weekly on foliage.",
            "controls": "Aphids, soft-bodied insects; supplies potassium.",
        },
    ],
    "fungal": [
        {
            "name": "Trichoderma Bio-fungicide",
            "preparation": "Mix 5 g Trichoderma viride powder per litre water.",
            "application": "Soil drench at planting and every 30 days; seed treatment 10 g/kg seed.",
            "controls": "Root rot, damping-off, fusarium wilt, pythium.",
        },
        {
            "name": "Bordeaux Mixture (1%)",
            "preparation": "Dissolve 100 g copper sulphate + 100 g lime in 10 litres water separately, then mix.",
            "application": "Spray on dormant plants or before rainy season.",
            "controls": "Fungal diseases: blight, downy mildew, anthracnose.",
        },
    ],
}

# Crop-specific organic care tips
CROP_SPECIFIC_TIPS = {
    "Paddy (Rice)": {
        "key_nutrients": "Nitrogen (critical), Phosphorus, Zinc",
        "organic_schedule": [
            "Before transplanting: 5 tonnes/acre FYM + 2 kg Azospirillum + 2 kg PSB soil application.",
            "21 days after transplanting: 200 litres/acre jeevamrut soil drench.",
            "45 days after transplanting: 2 tonnes/acre vermicompost top dressing.",
            "At panicle initiation: foliar spray of 2% coconut water or 0.5% seaweed extract.",
        ],
        "water_management": "Maintain 2–5 cm standing water during vegetative stage; drain before harvest.",
        "weed_management": "Use hand weeding at 20–30 days; ducks can be introduced for weed/pest control.",
    },
    "Wheat": {
        "key_nutrients": "Nitrogen, Phosphorus, Zinc",
        "organic_schedule": [
            "Before sowing: 4 tonnes/acre vermicompost + seed treatment with Azotobacter.",
            "At first irrigation (21 DAS): 200 litres/acre jeevamrut drench.",
            "At crown root initiation: foliar spray of 2% fish amino acid.",
            "At booting stage: spray 0.5% seaweed extract.",
        ],
        "water_management": "5–6 irrigations; critical stages: crown root initiation, tillering, jointing.",
        "weed_management": "Early hand weeding or use of mulch between rows.",
    },
    "Cotton": {
        "key_nutrients": "Nitrogen, Potassium, Sulphur, Boron",
        "organic_schedule": [
            "Before planting: 3 tonnes/acre compost + 100 kg neem cake.",
            "30 DAS: 200 litres/acre jeevamrut drench + neem oil foliar spray.",
            "60 DAS: 2 tonnes/acre vermicompost top dressing.",
            "At boll formation: spray 1% banana peel extract for potassium.",
        ],
        "water_management": "Drip irrigation preferred; 1 irrigation/week in dry spells.",
        "weed_management": "Mulching with dry grass between rows; inter-crop with moong bean.",
    },
    "Maize": {
        "key_nutrients": "Nitrogen (high), Phosphorus, Zinc",
        "organic_schedule": [
            "Before sowing: 4 tonnes/acre FYM + Azospirillum seed treatment.",
            "At knee-high stage: 200 litres jeevamrut/acre soil drench.",
            "At tasselling: foliar spray of 2% coconut water.",
            "At grain filling: 0.5% seaweed extract spray.",
        ],
        "water_management": "Critical water need at silking and grain fill; 5–7 irrigations.",
        "weed_management": "Inter-crop with soybean; hand-weed at 20–30 DAS.",
    },
    "Groundnut": {
        "key_nutrients": "Phosphorus, Calcium, Sulphur (minimal nitrogen — self-fixes)",
        "organic_schedule": [
            "Before sowing: 100 kg/acre bone meal + 100 kg gypsum + Rhizobium seed inoculation.",
            "At peg formation: 200 litres/acre jeevamrut drench.",
            "At pod development: foliar spray 1% fish amino acid.",
        ],
        "water_management": "Critical at flowering, pegging, and pod filling; 5–6 irrigations.",
        "weed_management": "Inter-row weeding before canopy closes; avoid disturbing pegs.",
    },
    "Soybean": {
        "key_nutrients": "Phosphorus, Potassium (self-fixes nitrogen)",
        "organic_schedule": [
            "Before sowing: 3 tonnes/acre vermicompost + Rhizobium + PSB seed treatment.",
            "At flowering: spray 2% fermented cow urine.",
            "At pod fill: foliar spray 0.5% seaweed extract.",
        ],
        "water_management": "Sensitive to waterlogging; ensure good drainage; 4–5 irrigations.",
        "weed_management": "One early weeding at 20–25 DAS is sufficient with mulching.",
    },
}

SEASONS = ["Kharif", "Rabi", "Zaid"]
SOIL_TYPES = list(SOIL_HEALTH_ADVICE.keys())
WATER_LEVELS = ["high_water", "medium_water", "low_water"]
WATER_LEVEL_LABELS = {
    "high_water": "High (>800 mm/year or canal/river irrigated)",
    "medium_water": "Medium (400–800 mm/year or well/borewell irrigated)",
    "low_water": "Low (<400 mm/year or rain-fed only)",
}
CHEMICAL_FERTILIZERS = list(FERTILIZER_REPLACEMENTS.keys())
