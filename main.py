import os
import time
from time import sleep
import requests
import pypresence
import colorama
from colorama import *
import socket
from pypresence import *
import json
import configparser
from configparser import *


def buttons():
        button1_url_input = input('1st Button URL: ')
        if button1_url_input == '':
            button1_url_input = 'Undefined'
        else:
            pass

        button2_input = input('2nd Button Text: ')
        if button2_input == '':
            button2_input = 'Undefined'
        else:
            pass

        button2_url_input = input('2nd Button URL: ')
        if button2_url_input == '':
            button2_url_input = 'Undefined'
        else:
            pass
def menu():
    print('Welcome to NoelP\'s Presence Creator. Would you like to use your previous config?')
    choice = input('y/n: ')
    if choice == 'n':
        config = ConfigParser()


        ClientID_input = input('Client ID: ')
        if ClientID_input == '':
            ClientID_input = 'Undefined'
        else:
            pass

        state_input = input('Title: ')
        if state_input == '':
            state_input = 'Undefined'
        else:
            pass

        Description_input = input('Description: ')
        if Description_input == '':
            Description_input = 'Undefined'
        else:
            pass

        small_image_input = input('Small Image: ')
        if small_image_input == '':
            small_image_input = 'Undefined'
        else:
            pass

        large_image_input = input('Large Image: ')
        if large_image_input == '':
            large_image_input = 'Undefined'
        else:
            pass

        button1_input = input('Button Text: ')
        if button1_input == '':
            button1_input = 'Undefined'
            button1_url_input = 'Undefined'
            button2_input = 'Undefined'
            button2_url_input = 'Undefined'
        else:
            buttons()

        config['settings'] = {
            'ClientID(Required)': ClientID_input,
            'Title(Required)': state_input,
            'Description(Optional)': Description_input,
        }

        config['images'] = {
            'large_image(Optional)': large_image_input,
            'small_image(Optional)': small_image_input,
        }

        config['buttons'] = {
            'button1(Optional)': button1_input,
            'button1_url(Optional)': button1_url_input,
            'button2(Optional)': button2_input,
            'button2_url(Optional)': button2_url_input
        }

        with open('./settings.ini', 'w') as f:
              config.write(f)
    elif choice == 'y':
        parser = ConfigParser()
        parser.read('settings.ini')
        ClientID = parser.get('settings', 'ClientID(Required)')
        Title = parser.get('settings', 'Title(Required)')
        Description = parser.get('settings', 'description(optional)')
        rpc = Presence(ClientID)
        rpc.connect()   
        rpc.update(state=Title,details=Description,large_image='large_image',small_image='small_image',buttons=[{"label": "YouTube", "url": "https://youtube.com/c/NoelP"}, {"label": "Discord Server", "url": "https://discord.gg/P37GEjGQqu"}],start=time.time())
        print('Sucessfully set RPC')
        time.sleep(25)
menu()
