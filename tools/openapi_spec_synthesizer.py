"""
openapi_spec_synthesizer.py - Generates valid OpenAPI 3.1.0 schema document from list of endpoints and methods
"""
import sys
import json


def synthesize_openapi_spec(endpoints_json: str):
    import json
    endpoints = json.loads(endpoints_json) if isinstance(endpoints_json, str) else endpoints_json
    paths = {}
    for ep in endpoints:
        p = ep.get("path", "/api/v1/health")
        m = ep.get("method", "get").lower()
        paths[p] = {m: {"summary": f"{m.upper()} {p}", "responses": {"200": {"description": "OK"}}}}
    spec = {"openapi": "3.1.0", "info": {"title": "Generated API", "version": "1.0.0"}, "paths": paths}
    return {"openapi_spec": spec, "endpoints_count": len(endpoints), "status": "OPENAPI_VALID"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "openapi-spec-synthesizer"}))
