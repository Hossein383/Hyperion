import random
import time
import logging
import sys
import requests
import time
from requests import post
import datetime
from termcolor import colored
import os
from os import system, name
import logging
from threading import Thread
import httpx
import time
from threading import Thread



Fruit1 = os.getenv("Fruitpass1")
Fruit2 = os.getenv("Fruitpass2")
Fruit3 = os.getenv("Fruitpass3")

def Num1():
    while True:
        try:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit1}"}
            p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
            print("ok FruitPass 1 ")
            time.sleep(225)
        except:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit1}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 1 ")
                time.sleep(225)
        else:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit1}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 1 ")
                time.sleep(225)
            


def Num2():
    while True:
        try:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit2}"}
            p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
            print("ok FruitPass 2 ")
            time.sleep(225)
        except:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit2}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 2 ")
                time.sleep(225)
        else:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit2}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 2 ")
                time.sleep(225)
            

    

def Num3():
    while True:
        try:
            r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit3}"}
            p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
            httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
            print("ok FruitPass 3 ")
            time.sleep(225)
        except:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit3}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 3 ")
                time.sleep(225)
        else:
            while True:
                r ={'User-Agent' : "Dalvik/2.1.0 (Linux; U; Android 13; SM-A326B Build/TP1A.220624.014)" ,'Connection':'close','Content-Type':"application/x-www-form-urlencoded" ,'Cookie':"FRUITPASSPORT="f"{Fruit3}"}
                p = {'edata' :'Gk4KXVpRXRJDSEMTfmMXSA=='}
                httpx.post("http://iran.fruitcraft.ir/cards/collectgold" , data=p,headers=r)
                print("ok FruitPass 3 ")
                time.sleep(225)
            

    

Thread(target=Num1).start()
Thread(target=Num2).start()
Thread(target=Num3).start()