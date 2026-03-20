extract_entities_tool = {
    "name": "extract_entities",
    "description": "Extract structured information like source, destination, date, flight_id, or booking_id from the user query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "User input text"
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}
def extract_entities(query: str):
    f"""Extracts structured information from user query"""
    return 