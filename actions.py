from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import COVID19Py
import pycountry


class ActionTotalInfected(Action):

    def name(self) -> Text:
        return "action_total_infected"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        covid19 = COVID19Py.COVID19()
        res = covid19.getLatest()

        r = res['confirmed']

        dispatcher.utter_message(text=f"there are {r} reported cases")

        return []


class ActionTotalInfectedByLocation(Action):

    def name(self) -> Text:
        return "action_total_infected_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = list(tracker.get_latest_entity_values("GPE"))[0]
        # print("Entities:", list(entities)[0])

        # loc = tracker.get_slot('GPE').lower()
        try:
            cc = pycountry.countries.lookup(loc).alpha_2

            covid19 = COVID19Py.COVID19()
            res = covid19.getLocationByCountryCode(cc)
                       
            r = sum([r['latest']['confirmed'] for r in res])  # sum up all cases from all provinces

            dispatcher.utter_message(template="utter_total_infected_by_location", cases=str(r), location=str(loc))
        except LookupError:
            dispatcher.utter_message(template="utter_error_unknown_location", location=str(loc))
        return []


class ActionTotalRecoveriesByLocation(Action):

    def name(self) -> Text:
        return "action_total_recoveries_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('GPE').lower()
        cc = pycountry.countries.lookup(loc).alpha_2

        covid19 = COVID19Py.COVID19()
        res = covid19.getLocationByCountryCode(cc)

        r = sum([r['latest']['recovered'] for r in res])  # sum up all cases from all provinces

        dispatcher.utter_message(text=str(r))

        return []


class ActionRateOfIncreaseByLocation(Action):

    def name(self) -> Text:
        return "action_rate_of_increase_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('GPE').lower()
        cc = pycountry.countries.lookup(loc).alpha_2

        ## TODO

        dispatcher.utter_message(text="Coming soon.")

        return []


class ActionHighestBy(Action):

    def name(self) -> Text:
        return "action_highest_by"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('GPE').lower()
        cc = pycountry.countries.lookup(loc).alpha_2

        covid19 = COVID19Py.COVID19()
        res = covid19.getLocationByCountryCode(cc)

        r = sum([r['latest']['confirmed'] for r in res])  # sum up all cases from all provinces

        dispatcher.utter_message(text=str(r))

        return []


class ActionLowestBy(Action):

    def name(self) -> Text:
        return "action_lowest_by"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('GPE').lower()
        cc = pycountry.countries.lookup(loc).alpha_2

        covid19 = COVID19Py.COVID19()
        res = covid19.getLocationByCountryCode(cc)

        r = sum([r['latest']['confirmed'] for r in res])  # sum up all cases from all provinces

        dispatcher.utter_message(text=str(r))

        return []


class ActionFAQQA(Action):

    def name(self) -> Text:
        return "action_faq_qa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="faq-qa")

        return []
