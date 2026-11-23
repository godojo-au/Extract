import unittest
from extract import validate


class ExtractionTests(unittest.TestCase):
    def test_rejects_invented_evidence(self):
        with self.assertRaises(ValueError):
            validate("Ada", {"contact": "name"}, {"contact": {"value": "Sam", "evidence": "Sam"}})

    def test_accepts_missing_value(self):
        result = {"budget": {"value": None, "evidence": None}}
        self.assertEqual(validate("Ada", {"budget": "budget"}, result), result)

    def test_rejects_value_outside_quote(self):
        with self.assertRaises(ValueError):
            validate("Ada, Sam", {"contact": "name"}, {"contact": {"value": "Sam", "evidence": "Ada"}})
