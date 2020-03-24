from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pycountry
import requests
import json


URL = "https://coronavirus-tracker-api.herokuapp.com/v2/"


class ActionTotalInfected(Action):

    def name(self) -> Text:
        return "action_total_infected"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = URL+"latest"
        response = requests.get(url)
        res = json.loads(response.content)

        r = res['latest']['confirmed']

        dispatcher.utter_message(template="utter_total_infected", cases=str(r))

        return []


class ActionTotalInfectedByLocation(Action):

    def name(self) -> Text:
        return "action_total_infected_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = list(tracker.get_latest_entity_values("GPE"))[0]

        try:
            country = pycountry.countries.lookup(loc)
            cc = country.alpha_2
            cname = country.name

            url = URL + f"locations?country_code={cc}"
            response = requests.get(url)
            res = json.loads(response.content)

            r = sum([r['latest']['confirmed'] for r in res['locations']])

            dispatcher.utter_message(template="utter_total_infected_by_location", cases=str(r), location=str(cname))
        except LookupError:
            dispatcher.utter_message(template="utter_error_unknown_location", location=str(loc))
        return []


class ActionTotalDeathsByLocation(Action):

    def name(self) -> Text:
        return "action_total_deaths_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('GPE').lower()
        try:
            country = pycountry.countries.lookup(loc)
            cc = country.alpha_2
            cname = country.name

            url = URL + f"locations?country_code={cc}"
            response = requests.get(url)
            res = json.loads(response.content)

            r = sum([r['latest']['deaths'] for r in res['locations']])

            dispatcher.utter_message(template="utter_total_deaths_by_location", cases=str(r), location=str(cname))
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
        try:
            country = pycountry.countries.lookup(loc)
            cc = country.alpha_2
            cname = country.name

            url = URL + f"locations?country_code={cc}"
            response = requests.get(url)
            res = json.loads(response.content)

            r = sum([r['latest']['recovered'] for r in res['locations']])

            dispatcher.utter_message(template="utter_total_recoveries_by_location", cases=str(r), location=str(cname))
        except LookupError:
            dispatcher.utter_message(template="utter_error_unknown_location", location=str(loc))
        return []

"""
class ActionRateOfIncreaseByLocation(Action):

    def name(self) -> Text:
        return "action_rate_of_increase_by_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc = tracker.get_slot('GPE').lower()
        country = pycountry.countries.lookup(loc)
        cc = country.alpha_2
        cname = country.name

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
"""


class ActionFAQQA(Action):

    def name(self) -> Text:
        return "action_covid_qa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        question = tracker.latest_message['text']

        URL = "https://covid-middleware.deepset.ai/api/bert/question"
        headers = {"content-type": "application/json"}
        data = json.dumps({"question": question})

        response = requests.post(URL, headers=headers, data=data)
        res = json.loads(response.content)

        res_question = res['answers'][0]['question']
        answer = res['answers'][0]['answer']
        relevance = str(round(float(res['answers'][0]['probability'])*100,1))
        source = res['answers'][0]['meta']['source']
        link = res['answers'][0]['meta']['link']
        last_update = res['answers'][0]['meta']['last_update']

        # TODO format message
        dispatcher.utter_message(template="utter_covid_qa", question=res_question, answer=answer, relevance=relevance, source=source, link=link, last_update=last_update)
        # dispatcher.utter_message(template="utter_faq_qa", question=res_question, answer=answer, relevance=relevance, source=source, link=link, last_update=last_update)

        return []
