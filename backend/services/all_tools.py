from services.create_booking import create_booking,create_booking_tool
from services.extract_entities import extract_entities,extract_entities_tool
from services.get_booking import get_booking,get_booking_tool
from services.get_flight_details import get_flight_details,get_flight_details_tool
from services.retrieve_info import retrieve_info,retrieve_info_tool
from services.search_flights import search_flights,search_flights_tool
tools=[{"type":"function","function":create_booking_tool},
      {"type":"function","function":extract_entities_tool},
      {"type":"function","function":get_booking_tool},
       {"type":"function","function":get_flight_details_tool},
       {"type":"function","function":retrieve_info_tool},
       {"type":"function","function":search_flights_tool}]
tool_functions = {
    "create_booking": create_booking,
    "extract_entities": extract_entities,
    "get_booking": get_booking,
    "get_flight_details": get_flight_details,
    "retrieve_info": retrieve_info,
    "search_flights": search_flights
}
