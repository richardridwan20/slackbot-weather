# ☀️ Slack Bot Weather
SlackBot to display weather everytime user asks the weather.

## Installation ##
First you need a few things pre-installed:
* Python (in this case we're using Python 3)
* Visual Studio Code for Editor
* pip for installing packages

If you manage to install all of the points above, proceed here:

```
pip install slackclient 
pip install python-dotenv
pip install flask
pip install slackeventsapi
pip install requests
```

Then download ngrok for rerouting our Flask Local Server to the Web Server:
https://ngrok.com/

> Make sure that you follow the tutorial / documentation on how to install Ngrok on respective OS that you have.

For the Weather API, we will use OpenWeatherMap API:
https://home.openweathermap.org/

>Sign up for an account (Free Plan) until you can get an API KEY.

## Project Architecture ##

```python
.
└── env.py                  # Please copy this to a file named .env
└── bot.py                 # Our main Bot Python file.
└── readme.md               # Yes, you are reading me now.
```
