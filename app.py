#imports
import os
import sys
import json
import random
import requests
import time
from flask import Flask, request

#define our flask app
app = Flask(__name__)

#Method will automatically execute when our endpoint receives a POST call
@app.route('/', methods=['POST'])
def msg_received_from_group():
  #Format the data we receive as a JSON
  data = request.get_json()
  log('{}'.format(data))
  
  #Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "!test":
    send_msg("Hello I'm Megan")
	

  return "ok", 200

 
#Sends a message to the chat that the bot originates from
def send_msg(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  payload = { 'text' : msg, 'bot_id' : '6c2b350e4f92a451d063e670cf'}
  r = requests.post(url, data=json.dumps(payload))

#logging function to help debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
