#!/usr/bin/python
from subprocess import call
from time import sleep
from PrensadoraSimulation import PrensadoraSimulation
from ProductsSimulation import ProductsSimulation 
from MotorSimulation import MotorSimulation 
import os

IOT_AGENT_URL_MOTOR = os.getenv('IOT_AGENT_URL', 'http://localhost:7896/iot/d')
IOT_AGENT_KEY_MOTOR = os.getenv('IOT_AGENT_KEY', '4jggokgpepnvsb2uv4s40d5911')
motor = MotorSimulation(IOT_AGENT_URL_MOTOR,IOT_AGENT_KEY_MOTOR)
prensadora = PrensadoraSimulation(IOT_AGENT_URL_MOTOR,IOT_AGENT_KEY_MOTOR)
i=0
while 1==1:
  prensadora.sendData()
  motor.sendData()
  i+=1
 
