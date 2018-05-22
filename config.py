import os

location = '47.6769,-122.2060'

def get_key(type):
    key = None
    try:
        key = os.environ[type.upper()]
    except KeyError:
        print(f'No {type.title()} API key detected.  Expecting it in a {type.upper()} environment variable.')
    return key