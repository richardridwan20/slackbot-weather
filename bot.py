import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request
from slackeventsapi import SlackEventAdapter
import requests
from datetime import datetime

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.getenv('SLACK_SIGNING_SECRET'), '/slack/events', app)

client = slack.WebClient(token=os.getenv('SLACK_TOKEN'))
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payLoad):
    event = payLoad.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Jakarta&units=metric&appid='+os.getenv('OPENWEATHERMAP_KEY'))
    json_object = r.json()
    degree_celcius = float(json_object['main']['temp'])    
    city = json_object['name']
    weather_main_condition = json_object['weather'][0]['main']   
    weather_desc_condition = json_object['weather'][0]['description']
    
    timestamp = json_object['dt']
    dt_object = str(datetime.fromtimestamp(timestamp))

    weather = 'Hi! \n The Weather now for you in '+ city +' is: ' + weather_main_condition + ' with ' + weather_desc_condition + '. \n The Current Temperature is: ' +str(degree_celcius)+ ' Degree Celcius. \n Current Time: ' + dt_object
    
    if BOT_ID != user_id:
        if 'weather' in text:
            client.chat_postMessage(channel=channel_id, text=weather)
            pass
        else:
            client.chat_postMessage(channel=channel_id, text='I am sorry but I dont understand what you are saying. Please type weather for weather information.')
        pass
    

if __name__ == "__main__":
    app.run(debug=True)