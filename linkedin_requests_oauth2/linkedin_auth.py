import string
import random
from .oauth2 import OAuth2

LINKEDIN_URL = 'https://www.linkedin.com/uas/oauth2'
AUTHORIZATION_URL = '/authorization'
TOKEN_URL = '/accessToken'


class LinkedIn_OAuth2(OAuth2):
    response_type = 'code'
    grant_type = 'authorization_code'

    def __init__(self, client_id, client_secret, redirect_uri):
        self.state = self.unique_string()
        OAuth2.__init__(self, client_id, client_secret, LINKEDIN_URL, redirect_uri, AUTHORIZATION_URL, TOKEN_URL)

    def unique_string(size=20, valid_chars=None):
        if valid_chars is None:
            valid_chars = string.letters + string.digits

        return ''.join(random.choice(valid_chars) for x in range(20))

    def authorize_url(self, scope='', **kwargs):
        return OAuth2.authorize_url(self, scope=scope, state=self.state, response_type=self.response_type)

    def get_token(self, code, **kwargs):
        return OAuth2.get_token(self, code, grant_type=self.grant_type)
