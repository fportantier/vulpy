import json
import base64

from cryptography.fernet import Fernet

key = 'JHtM1wEt1I1J9N_Evjwqr3yYauXIqSxYzFnRhcf0ZG0='
fernet = Fernet(key)

def create(response, username):
    response.set_cookie('vulpy_session', fernet.encrypt(username.encode()))
    return response


def load(request):

    session = {}
    cookie = request.cookies.get('vulpy_session')

    if cookie:
        try:
            session = {'username': fernet.decrypt(cookie.encode()).decode()}
        except Exception as e:
            print(e)
            pass

    return session


def destroy(response):
    response.set_cookie('vulpy_session', '', expires=0)
    return response

