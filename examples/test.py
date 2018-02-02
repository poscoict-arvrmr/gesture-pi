#!/usr/bin/env python
import skywriter
import signal
import paho.mqtt.client as mqtt

broker_address="192.168.42.79"
print("creating new client instance")
client = mqtt.Client("Pi")
client.connect(broker_address)

client.subscribe("gesture/state")

some_value = 5000

'''
@skywriter.move()
def move(x, y, z):
  print( x, y, z )
'''
'''
@skywriter.flick()
def flick(start,finish):
    print('Got a flick!', start, type(start), finish)
'''
'''
@skywriter.airwheel()
def spinny(delta):
  global some_value
  some_value += delta
  if some_value < 0:
  	some_value = 0
  if some_value > 10000:
    some_value = 10000
  print('Airwheel:', some_value/100)
'''
@skywriter.double_tap()
def doubletap(position):
	client.publish("gesture/state", "double tap")
	print('Double tap!', position)

@skywriter.tap()
def tap(position):
    if position=='west':
        client.publish("gesture/state", "right")
    elif position=='east':
        client.publish("gesture/state", "left")
    print('Tap!', position)
'''
@skywriter.touch()
def touch(position):
	client.publish("gesture/state", "tap")
	print('Touch!', position)
'''
signal.pause()
