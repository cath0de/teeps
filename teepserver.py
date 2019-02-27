#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import zmq

ctx = zmq.Context()
app = Flask(__name__)
Bootstrap(app)

# Socket to send messages to the Teep over
teep = ctx.socket(zmq.PUSH)
teep.bind("tcp://*:6640")

labels = []

@app.route('/')
def listen():
    return render_template('listen.html')    

@app.route('/label', methods=['POST'])
def claim_label(label=None):
    if label not in labels:
        labels.append(label)
    return render_template('listen.html', label=label)

@app.route('/say', methods=['POST'])
def say(speaker=None, speech=None):
    pass

# Socket to receive presence notifications/speech actions over
remote_pull = ctx.socket(zmq.PULL)
remote_pull.bind("tcp://*:6641")

# Socket to redistribute text of speech actions over
remote_pub = ctx.socket(zmq.PUB)
remote_pub.bind("tcp://*:6642")



    
