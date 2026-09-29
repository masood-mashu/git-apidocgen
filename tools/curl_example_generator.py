"""
curl_example_generator.py - Generates copy-paste executable cURL command line string with headers and dummy body
"""
import sys
import json


def generate_curl_example(endpoint_metadata_json: str):
    import json
    data = json.loads(endpoint_metadata_json) if isinstance(endpoint_metadata_json, str) else endpoint_metadata_json
    m = data.get("method", "GET").upper()
    url = data.get("url", "https://api.example.com/v1/data")
    curl = f'curl -X {m} "{url}" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json"'
    return {"curl_command": curl, "status": "CURL_GENERATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "curl-example-generator"}))
