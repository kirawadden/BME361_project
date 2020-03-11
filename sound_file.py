from playsound import playsound
from twilio.rest import Client
import os
import serial
import time


def twilio_setup():
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    return client


def send_message(message_text, twilio_client):
    message = twilio_client.messages.create(
        to = '+17788582033',
        from_ = '+12054559856',
        body = message_text
    )
    print(message.sid)


def play_audio(f_name):
    playsound(f_name)


def ser_loop(serobj):
    while 1:
        if serobj.in_waiting > 0:
            line = serobj.readline()
            

def main():
    # ser = serial.Serial('/dev/ttyUSB0', 9600)
    twilio_client = twilio_setup()
    send_message("sup g", twilio_client)
    # ser_loop(ser)


if __name__ == '__main__':
    main()

