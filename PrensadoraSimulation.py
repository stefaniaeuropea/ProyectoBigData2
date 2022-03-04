# -*- coding: utf-8 -*-
"""
Created on Tue Dic 1 22:15:05 2021

@author: Jorge Capel
"""


import datetime
import time
import random
import requests

class PrensadoraSimulation:

    fuerza =  0;
    humedad = 0;
    temperatura = 0;
    vibracionh = 0;
    vibracionv = 0;
    iotagenturl="";
    iotagentkey="";
    
    def __init__(self,iotagenturl,iotagentkey):
        self.iotagenturl = iotagenturl
        self.iotagentkey = iotagentkey
        

    
    def payload(self,devicename,date):
        #p|80|b|50|t|85|d|%Y-%m-%dT%H:%M:%SZ
        ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        #p|80|b|50|t|85
        self.fuerza = random.uniform(5, 100)
        self.humedad = random.uniform(1, 50)
        self.temperatura = random.uniform(1, 50)
        self.vibracionh = random.uniform(1, 10);
        self.vibracionv = random.uniform(1, 10);
        payloadStr = "n|"+devicename+"|f|"+str("{0:.2f}".format(self.fuerza))+"|h|"+str("{0:.2f}".format(self.humedad))+"|t|"+str("{0:.2f}".format(self.temperatura))+"|d|"+str(ahora)
        payloadStr = payloadStr + "|vh|"+str("{0:.2f}".format(self.vibracionh))+"|vv|"+str("{0:.2f}".format(self.vibracionv))
        return payloadStr

    def sendData(self):

        

        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Prensadora0"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            payload1 = self.payload(devicename,datetime.datetime.now())
            r1 = requests.post(url= endpoint1,headers=header, data=payload1)
            print("datos sensor {} {} ".format(devicename,payload1))
            time.sleep(1)
            i+=1
            
       
    def sendHistoricalData(self):
        url = self.iotagenturl+"?i="
        #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911

        i=1
        while i<=5:
            devicename="Prensadora0"+str(i)
            endpoint1 = url+devicename+"&k="+self.iotagentkey
            header = {"ContentType":"text/plain"} 
            idays = 30
           
            while idays >=1:
                date=datetime.datetime.now() + datetime.timedelta(days=idays*-1)
                payload1 = self.payload(devicename,date)
                r1 = requests.post(url= endpoint1,headers=header, data=payload1)
                print("datos sensor {} {} ".format(devicename,payload1))
                idays-=1
                time.sleep(0.5)
            i+=1