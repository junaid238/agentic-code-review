import json


def safe_json_parse(response):

    try:
        return json.loads(response)

    except Exception:

        return {
            "findings": [
                {
                    "issue": "Parsing Error",
                    "severity": "LOW",
                    "recommendation": response
                }
            ]
        }