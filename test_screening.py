import unittest
from screening import assess_risk

class ScreeningTests(unittest.TestCase):
    def test_routine_values_low(self):
        r = assess_risk(35, 36.8, 78, 118, 76, 98, [])
        self.assertEqual(r["level"], "Low")
        self.assertFalse(r["urgent"])

    def test_fever_moderate(self):
        r = assess_risk(24, 38.5, 96, 120, 80, 97, ["fever"])
        self.assertEqual(r["level"], "Moderate")

    def test_breathlessness_urgent(self):
        r = assess_risk(52, 37.0, 118, 90, 60, 88, ["breathlessness"])
        self.assertEqual(r["level"], "High")
        self.assertTrue(r["urgent"])

    def test_chest_pain_urgent(self):
        r = assess_risk(45, 36.8, 80, 120, 80, 98, ["chest_pain"])
        self.assertTrue(r["urgent"])

if __name__ == "__main__":
    unittest.main()
