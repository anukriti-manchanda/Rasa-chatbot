# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# 

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")
#         return []

import requests
from typing import Dict, List, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        print(city)
        if city:
            api_key = "69aa8775bdaf718c8f40a2c2c90c2b91"
            endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            try:
                response = requests.get(endpoint)
                data = response.json()

                if response.status_code == 200:
                    print(data)
                    temperature = data["main"]["temp"]
                    description = data["weather"][0]["description"]
                    message = f"The weather in {city} is {description} with a temperature of {temperature}°C."
                    dispatcher.utter_message(message)
                else:
                    dispatcher.utter_message("Sorry, I couldn't retrieve the weather information at the moment.")

            except Exception as e:
                dispatcher.utter_message("Sorry, there was an error while fetching weather data.")
                # Log the error for debugging purposes
                print(str(e))
        return []



