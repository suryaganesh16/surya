"""
Tests for the Organic Farming Advisor application.
"""

import pytest
import agricultural_data as data
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-secret"
    with app.test_client() as client:
        yield client


# ── agricultural_data tests ───────────────────────────────────────────────────

class TestAgriculturalData:
    def test_all_chemical_fertilizers_have_organic_alternatives(self):
        for fert, info in data.FERTILIZER_REPLACEMENTS.items():
            assert "organic_alternatives" in info, f"{fert} missing organic_alternatives"
            assert len(info["organic_alternatives"]) > 0, f"{fert} has no alternatives"
            for alt in info["organic_alternatives"]:
                for key in ("name", "application", "benefits", "preparation"):
                    assert key in alt, f"{fert} alternative missing '{key}'"

    def test_all_soil_types_have_health_advice(self):
        for soil in data.SOIL_TYPES:
            assert soil in data.SOIL_HEALTH_ADVICE, f"No health advice for {soil}"
            advice = data.SOIL_HEALTH_ADVICE[soil]
            for key in ("characteristics", "challenges", "organic_amendments", "biofertilizers", "ph_management"):
                assert key in advice, f"{soil} advice missing '{key}'"

    def test_crop_recommendations_cover_all_soils_seasons_water(self):
        for soil in data.SOIL_TYPES:
            assert soil in data.CROP_RECOMMENDATIONS, f"No crop recs for {soil}"
            for water in data.WATER_LEVELS:
                if water in data.CROP_RECOMMENDATIONS[soil]:
                    for season in data.SEASONS:
                        crops = data.CROP_RECOMMENDATIONS[soil][water].get(season, [])
                        assert isinstance(crops, list)

    def test_water_level_labels_match_constants(self):
        for key in data.WATER_LEVELS:
            assert key in data.WATER_LEVEL_LABELS

    def test_chemical_fertilizers_list_not_empty(self):
        assert len(data.CHEMICAL_FERTILIZERS) > 0


# ── Flask route tests ─────────────────────────────────────────────────────────

class TestRoutes:
    def test_index_get(self, client):
        resp = client.get("/")
        assert resp.status_code == 200
        assert b"Farmer" in resp.data

    def test_land_details_missing_fields(self, client):
        """Submitting empty form should return 200 with error messages."""
        resp = client.post("/land-details", data={})
        assert resp.status_code == 200
        assert b"required" in resp.data.lower() or b"error" in resp.data.lower()

    def test_land_details_invalid_phone(self, client):
        resp = client.post("/land-details", data={
            "name": "Test Farmer",
            "phone": "123",          # too short
            "village": "TestVillage",
            "pincode": "500001",
            "area": "2",
            "area_unit": "acres",
            "crop": "Paddy",
        })
        assert resp.status_code == 200
        assert b"phone" in resp.data.lower()

    def test_land_details_invalid_pincode(self, client):
        resp = client.post("/land-details", data={
            "name": "Test Farmer",
            "phone": "9876543210",
            "village": "TestVillage",
            "pincode": "12345",       # only 5 digits
            "area": "2",
            "area_unit": "acres",
            "crop": "Paddy",
        })
        assert resp.status_code == 200
        assert b"pincode" in resp.data.lower()

    def test_land_details_valid_moves_to_step2(self, client):
        resp = client.post("/land-details", data={
            "name": "Ramaiah",
            "phone": "9876543210",
            "village": "Nandipeta",
            "pincode": "500001",
            "area": "3",
            "area_unit": "acres",
            "crop": "Cotton",
        })
        assert resp.status_code == 200
        # Step 2 form should contain soil type choices
        assert b"soil" in resp.data.lower()

    def test_fertilizer_select_redirects_without_session(self, client):
        resp = client.post("/fertilizer-select", data={})
        assert resp.status_code == 302  # redirect to index

    def test_recommendations_redirects_without_session(self, client):
        resp = client.post("/recommendations", data={})
        assert resp.status_code == 302

    def test_restart_clears_session(self, client):
        with client.session_transaction() as sess:
            sess["farmer"] = {"name": "Test"}
        resp = client.get("/restart")
        assert resp.status_code == 302
        with client.session_transaction() as sess:
            assert "farmer" not in sess

    def _setup_session(self, client):
        """Helper: inject a complete session so recommendations step works."""
        with client.session_transaction() as sess:
            sess["farmer"] = {
                "name": "Ramaiah",
                "phone": "9876543210",
                "village": "Nandipeta",
                "pincode": "500001",
                "area": "3",
                "area_unit": "acres",
                "crop": "Cotton",
            }
            sess["land"] = {
                "soil_type": "Black (Regur)",
                "water_level": "medium_water",
                "season": "Kharif",
                "weather": "Semi-arid",
                "soil_ph": "7.8",
                "soil_health": "Hard crust",
            }

    def test_fertilizer_select_with_session(self, client):
        self._setup_session(client)
        resp = client.post("/fertilizer-select", data={
            "soil_type": "Black (Regur)",
            "water_level": "medium_water",
            "season": "Kharif",
            "weather": "Semi-arid",
            "soil_ph": "7.8",
            "soil_health": "",
        })
        assert resp.status_code == 200
        assert b"fertilizer" in resp.data.lower()

    def test_recommendations_with_valid_session(self, client):
        self._setup_session(client)
        resp = client.post("/recommendations", data={
            "fertilizers": ["Urea", "NPK (Mixed Fertilizer)"],
        })
        assert resp.status_code == 200
        assert b"Urea" in resp.data
        assert b"Vermicompost" in resp.data

    def test_recommendations_no_fertilizer_shows_error(self, client):
        self._setup_session(client)
        resp = client.post("/recommendations", data={})
        assert resp.status_code == 200
        assert b"select at least one" in resp.data.lower()
