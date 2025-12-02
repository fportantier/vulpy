from cryptography.fernet import Fernet
import geoip2.database

import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('SESSION_KEY')
fernet = Fernet(key)
ttl = 7200  # seconds
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')


def getcountry(request):
    country = 'XX'  # For local connections

    try:
        geo = reader.country(request.remote_addr)
        country = geo.country.iso_code
    except Exception:
        pass

    return country


def create(request, response, username):
    country = getcountry(request)

    # Build the session payload and encrypt it
    plaintext = f"{username}|{country}".encode()  # bytes for Fernet
    token = fernet.encrypt(plaintext)             # bytes
    token_str = token.decode("utf-8")             # string for cookie

    # Cookie value must be a str, not bytes
    response.set_cookie('vulpy_session', token_str)

    return response


def load(request):
    cookie = request.cookies.get('vulpy_session')

    if not cookie:
        return {}

    try:
        # cookie is a str, Fernet expects bytes
        token = fernet.decrypt(cookie.encode(), ttl=ttl)
        username, country = token.decode().split('|')
    except Exception as e:
        print(e)
        return {}

    # getcountry expects the full request, not just remote_addr
    if country == getcountry(request):
        return {'username': username, 'country': country}
    else:
        return {}


def destroy(response):
    response.set_cookie('vulpy_session', '', expires=0)
    return response