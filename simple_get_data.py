#!user/bin/env python
import fitbit
import ConfigParser
import datetime
import os
import time
import sys
import cherrypy
import threading
import traceback
import webbrowser
import argparse
import gather_keys_oauth2

from fitbit.exceptions import HTTPTooManyRequests
from fitbit.exceptions import HTTPUnauthorized
from base64 import b64encode
from fitbit.api import FitbitOauth2Client
from oauthlib.oauth2.rfc6749.errors import MismatchingStateError, MissingTokenError
from requests_oauthlib import OAuth2Session

#below is that way you get it without having to refresh the token
#basic test to query from temporary tokens
consumer_key = '229R96'
consumer_secret = 'e520d1a8a82f5afae1ba40e7cb9a25b6'
#temporary user keys for Laura Pina, UW CSE
u_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0U0w5TVkiLCJhdWQiOiIyMjlSOTYiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDkzMTg5NTk3LCJpYXQiOjE0OTMxNjA3OTd9.4fb1CsOR7vumawAEEr6aiDkdoMr4zjN3uLoSONF7-OQ'
u_secret = '0379abc38a28f825ec9ab58c27e17161654fa510789b53ab869ecd89ebace065'
d = datetime.date(2016, 8, 11);
# authd_client = fitbit.Fitbit(consumer_key, consumer_secret, access_token=u_key, refresh_token=u_secret)
# #body_stats = authd_client._COLLECTION_RESOURCE('body')
# #print body_stats 
# sleep = authd_client.get_sleep(d)
# #sleep = authd_client.sleep()
# print sleep

#but eventually you need to refresh
f_oauth = FitbitOauth2Client(consumer_key, consumer_secret,access_token=u_key, refresh_token=u_secret)
#print f_oauth.token['refresh_token']
#print f_oauth.client_id
#print f_oauth.client_secret
#f_oauth.authorize_token_url(redirect_uri='http://localhost:8080')
#f_oauth.fetch_access_token('http://localhost:8080')
#token = f_oauth.refresh_token()
f = fitbit.Fitbit(consumer_key, consumer_secret, access_token=u_key, refresh_token=u_secret)
sleep = f.get_sleep(d)
print sleep