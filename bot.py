import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

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

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)
        pass
    

if __name__ == "__main__":
    app.run(debug=True)