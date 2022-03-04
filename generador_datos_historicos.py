# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:01:07 2022

@author: Stephania
"""

#!/usr/bin/python
from subprocess import call
from time import sleep
from MotorSimulation import MotorSimulation

import os


IOT_AGENT_URL = os.getenv('IOT_AGENT_URL', 'http://localhost:7896/iot/d')
IOT_AGENT_KEY = os.getenv('IOT_AGENT_KEY', '4jggokgpepnvsb2uv4s40d5911')

i=0
motor = MotorSimulation(IOT_AGENT_URL_MOTOR,IOT_AGENT_KEY_MOTOR)
motor.sendHistoricalData()
"""
calidad = CalidadAireSimulation(IOT_AGENT_URL,IOT_AGENT_KEY)
calidad.sendHistoricalData()
"""