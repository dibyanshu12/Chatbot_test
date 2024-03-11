# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_get_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        serv = tracker.get_slot('serv')
        if (serv=="Consulting & Auditing"):
            dispatcher.utter_message(text="Been in the field for 5+ years, watching many accounts grow from 0 to 100 to somewhere in Ks. Knowing the fundamentals of how the digital world works, I am here to help you grow exponentially.")
        elif (serv=="Development"):
            dispatcher.utter_message(
                text="Looking out for customized solutions for your websites & social media handles? Our team will develop and deliver websites as well as your social medias, that will serve your purpose.")
        elif (serv=="Marketing"):
            dispatcher.utter_message(
                text="With researched digital marketing, we will ensure that new customers and clients are able to find your business.")
        else:
            dispatcher.utter_message(
                text="Service currently not available for more info contact thesocialminder.in@gmail.com")







        return []
