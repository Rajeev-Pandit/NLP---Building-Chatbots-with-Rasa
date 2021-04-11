from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import pandas as pd
import zomatopy
import json
from email.message import EmailMessage
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ActionSearchRestaurants(Action):
    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "0c23e5a8ae272579ff9a18948484f909"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        budget = tracker.get_slot("money")
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {
            "Mexican": 73,
            "Chinese": 25,
            "American": 1,
            "Italian": 55,
            "North Indian": 50,
            "South Indian": 85,
        }
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 5
        )
        d = json.loads(results)
        if d["results_found"] == 0:
            dispatcher.utter_message("Sorry, i couldn't find any restaurants..")
        else:
            restaurants = [
                restaurant["restaurant"]["name"] for restaurant in d["restaurants"]
            ]
            locations = [
                restaurant["restaurant"]["location"]["address"]
                for restaurant in d["restaurants"]
            ]
            ratings = [
                restaurant["restaurant"]["user_rating"]["aggregate_rating"]
                for restaurant in d["restaurants"]
            ]
            prices = [
                restaurant["restaurant"]["average_cost_for_two"]
                for restaurant in d["restaurants"]
            ]
            #pd.set_option("display.max_colwidth", -1)
            df = pd.DataFrame(
                {
                    "name": restaurants,
                    "location": locations,
                    "rating": ratings,
                    "avg_cost_for2": prices,
                }
            )
            if budget == "299":
                df_filter = df[df["avg_cost_for2"] < 300]
            elif budget == "599":
                df_filter = df[
                    (df["avg_cost_for2"] >= 300) & (df["avg_cost_for2"] <= 700)
                ]
            else:
                df_filter = df[(df["avg_cost_for2"] > 700)]

            df_sorted = df_filter.sort_values(by=["rating"], ascending=False)
            dispatcher.utter_message(
                "-----Here are the top rated "
                + cuisine
                + " restaurants in "
                + loc
                + " with avg. budget of "
                + budget
                + " Rs. for 2 people-----"
            )
            for row in df_sorted.head(5).iterrows():
                dispatcher.utter_message(
                    row[1]["name"]
                    + " in "
                    + row[1]["location"]
                    + " has been rated "
                    + row[1]["rating"]
                    + "\n"
                )

            return [SlotSet("facility_type", loc), SlotSet("restaurants_list", df_sorted.to_html(index=False))]


class ActionCheckLocation(Action):
    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "0c23e5a8ae272579ff9a18948484f909"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot("location")
        city_list = [
            "Agra",
            "Ahmedabad",
            "Aligarh",
            "Amravati",
            "Amritsar",
            "Asansol",
            "Aurangabad",
            "Bangalore",
            "Bareilly",
            "Belgaum",
            "Bhavnagar",
            "Bhiwandi",
            "Bhopal",
            "Bhubaneswar",
            "Bikaner",
            "Bilaspur",
            "Bokaro Steel City",
            "Chennai",
            "Chandigarh",
            "Coimbator",
            "Cuttack",
            "Delhi",
            "Dehradun",
            "Dhanbad",
            "Bhilai",
            "Durgapur",
            "Erode",
            "Faridabad",
            "Firozabad",
            "Gandhinagar",
            "Ghaziabad",
            "Gorakhpur",
            "Gulbarga",
            "Guntur",
            "Gwalior",
            "Gurgaon",
            "Guwahati",
            "Hamirpur",
            "Hyderabad",
            "Hubli–Dharwad",
            "Indore",
            "Jabalpur",
            "Jaipur",
            "Jammu",
            "Jalandhar",
            "Jamnagar",
            "Jamshedpur",
            "Jhansi",
            "Jodhpur",
            "Kanpur",
            "Kolkata",
            "Kakinada",
            "Kannur",
            "Kochi",
            "Kolhapur",
            "Kollam",
            "Kozhikode",
            "Kurnool",
            "Ludhiana",
            "Lucknow",
            "Mumbai",
            "Madurai",
            "Malappuram",
            "Mathura",
            "Meerut",
            "Moradabad",
            "Mysore",
            "Nagpur",
            "Nanded",
            "Nashik",
            "Nellore",
            "Noida",
            "Patna",
            "Pondicherry",
            "Purulia",
            "Pune",
            "Prayagraj",
            "Raipur",
            "Rajkot",
            "Rajahmundry",
            "Ranchi",
            "Rourkela",
            "Salem",
            "Sangli",
            "Shimla",
            "Siliguri",
            "Solapur",
            "Srinagar",
            "Surat",
            "Thiruvananthapuram",
            "Thrissur",
            "Tiruchirappalli",
            "Tiruppur",
            "Ujjain",
            "Bijapur",
            "Vadodara",
            "Varanasi",
            "Vasai-VirarCity",
            "Vijayawada",
            "Visakhapatnam",
            "Vellore",
            "Warangal",
        ]
        if loc.title() in city_list:
            return [SlotSet("check_location", True)]

        else:
            return [SlotSet("check_location", False)]


class ActionCheckCuisine(Action):
    def name(self):
        return "action_check_cuisine"

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "0c23e5a8ae272579ff9a18948484f909"}
        zomato = zomatopy.initialize_app(config)
        cus = tracker.get_slot("cuisine")
        cuisine_list = [
            "Mexican",
            "Chinese",
            "American",
            "Italian",
            "North Indian",
            "South Indian",
        ]
        if cus.title() in cuisine_list:
            return [SlotSet("check_cuisine", True)]

        else:
            return [SlotSet("check_cuisine", False)]

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        sender_email = "chatbotrasa790@gmail.com"
        receiver_email = tracker.get_slot("emailid")
        password = "rasachatbot_study"
        restro_data = tracker.get_slot("restaurants_list")
        message = MIMEMultipart("alternative")
        message["Subject"] = "Here are the list of your Favourite restaurants"
        message["From"] = sender_email
        message["To"] = receiver_email
        html_body = MIMEText(restro_data, "html")
        message.attach(html_body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return []
