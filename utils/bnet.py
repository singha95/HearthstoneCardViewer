from rauth import OAuth2Service
from datetime import datetime as dt;
import requests, json 

class Bnet: 
    """
    A class created to deal with request made to the Blizzard Battle.net API. 
    Can generate tokens from the server and can validate tokens. In addition 
    can collect data from the server in the form of jsons. 
    """

    def __init__(self): 
        self.client_id = "01edd9199cd143e28d9f1dbc3e77dcff"
        self.secret = "k3kE3WGarYtQlkC14uRCfAIVRon0kyYx"
        self.redirect_uri = "http://127.0.0.1:8000"

        self.url = "https://us.api.blizzard.com/hearthstone/cards"
        self.token_url = "https://us.battle.net/oauth/token"
        self.auth_url = "https://us.battle.net/oauth/authorize"

        self.oauth_service = OAuth2Service(name = "bnet",
                                           client_id = self.client_id,
                                           client_secret = self.secret,
                                           access_token_url = self.token_url, 
                                           authorize_url = self.auth_url, 
                                           base_url = 
                                                "https://us.api.blizzard.com/"
                                           )
    def generate_token(self): 

        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post('https://us.battle.net/oauth/token', 
                                data=data, 
                                auth=('01edd9199cd143e28d9f1dbc3e77dcff', 
                                        'k3kE3WGarYtQlkC14uRCfAIVRon0kyYx')
                                )
        return json.loads(response.text)["access_token"]

    def check_token(self, token): 
        token_check = requests.post('https://eu.battle.net/oauth/check_token', 
                                    data = { 'token': token } )
        if not token_check.status_code == 200:
            #the following is inconsistent, content is sometimes HTML, 
            #sometimes JSON
            return (False, 'Invald request. Server sent: ' + 
                            token_check.content)
        else:
            #valid request; check the answer for whatever you want
            return (True,  
                    'Time:' + 
                    str(dt.fromtimestamp( token_check.json()['exp'] ) -  
                    dt.now()))

    def get_data(self, token, url): 
        session = self.oauth_service.get_session( token = token )
        data = session.get(url).json()
        return data 