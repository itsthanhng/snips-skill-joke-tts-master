#!/usr/bin/env python3

#- * -coding: utf - 8 - * -

from hermes_python.hermes import Hermes
import requests
import json
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

with open('jokes.json') as json_file:
    jokes = json.load(json_file)


def intent_received(hermes, intent_message):
    index = random.randint(0, jokes["count"] - 1)    
    print(index)    
    joke = jokes["jokes"][index]
    if joke["type"] == "single":
        sentence = joke["joke"]
    else:
        sentence = joke["setup"] + "      " + joke["delivery"]
    hermes.publish_end_session(intent_message.session_id, sentence)
    print(sentence)
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
