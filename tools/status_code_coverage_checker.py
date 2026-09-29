"""
status_code_coverage_checker.py - Verifies that endpoint operations define documentation for standard client/server errors
"""
import sys
import json


def check_status_code_coverage(responses_json: str):
    import json
    codes = json.loads(responses_json) if isinstance(responses_json, str) else responses_json
    required = ["200", "400", "401", "500"]
    missing = [c for c in required if str(c) not in [str(x) for x in codes]]
    is_complete = len(missing) == 0
    return {"is_complete": is_complete, "missing_codes": missing, "status": "COVERAGE_COMPLETE" if is_complete else "COVERAGE_PARTIAL"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "status-code-coverage-checker"}))
