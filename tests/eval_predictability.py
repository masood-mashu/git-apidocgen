"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitApiDocGen.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.openapi_spec_synthesizer import *
from tools.status_code_coverage_checker import *
from tools.curl_example_generator import *

class TestGitApiDocGenPredictability(unittest.TestCase):
    def test_openapi_spec_synthesizer(self):
        res = synthesize_openapi_spec('[{"path": "/users", "method": "GET"}]')
        self.assertEqual(res["openapi_spec"]["openapi"], "3.1.0")
        self.assertEqual(res["status"], "OPENAPI_VALID")

    def test_status_code_coverage_checker(self):
        res = check_status_code_coverage('["200", "400", "401", "500"]')
        self.assertTrue(res["is_complete"])
        self.assertEqual(res["status"], "COVERAGE_COMPLETE")

    def test_curl_example_generator(self):
        res = generate_curl_example('{"method": "POST", "url": "https://api.example.com/items"}')
        self.assertIn("curl -X POST", res["curl_command"])
        self.assertEqual(res["status"], "CURL_GENERATED")


if __name__ == "__main__":
    unittest.main()
