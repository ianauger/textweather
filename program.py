import darksky
from twilio.rest import Client
import config

twilio_acct = config.get_key('twilio_acct')
twilio_token = config.get_key('twilio_token')
twilio_tn = config.get_key('twilio_tn')
darksky_key = config.get_key('darksky')
tn = config.get_key('cell_phone_tn')

def send_text(forecast, tn, twilio_acct, twilio_token):
    text_body = f"Forecast: {forecast['summary'].lower()} High today of {forecast['apparentTemperatureHigh']}, " \
                f"low of {forecast['apparentTemperatureLow']}."

    client = Client(twilio_acct, twilio_token)
    message = client.messages.create(to=tn, from_=twilio_tn, body=text_body)

def main():
    forecast = darksky.get_today_weather(darksky_key, config.location)
    send_text(forecast, tn, twilio_acct, twilio_token)

if __name__ == '__main__':
    main()
