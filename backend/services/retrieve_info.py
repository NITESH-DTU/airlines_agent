retrieve_info_tool = {
    "name": "retrieve_info",
    "description": "Retrieve relevant information about airline policies such as baggage, cancellation, or refunds.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "User question related to airline policies or FAQs"
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}
def retrieve_info(query: str):
    f""" Fetches relevant information from knowledge base (policies, FAQs)."""
    return 