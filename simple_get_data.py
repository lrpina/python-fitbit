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
refresh_token = 'abf7637259d318e81bb5132522e035b84054c018e5f4d236addffd7def93e9d7'
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0U0w5TVkiLCJhdWQiOiIyMjlSOTYiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDk3NDA3OTcwLCJpYXQiOjE0OTczNzkxNzB9.BwzhNO4idM4n0eBSgQ_KkQIthsPcyTOPrf1dK37yUZI'
expires_in = 28800
expires_at = 1496556709.63

#u_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0U0w5TVkiLCJhdWQiOiIyMjlSOTYiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDkzMTg5NTk3LCJpYXQiOjE0OTMxNjA3OTd9.4fb1CsOR7vumawAEEr6aiDkdoMr4zjN3uLoSONF7-OQ'
#u_secret = '0379abc38a28f825ec9ab58c27e17161654fa510789b53ab869ecd89ebace065'
#need to figure out
#how to create a function
#We also strongly recommend passing in a refresh_cb keyword argument, which should be a function taking one argument: a token dict.
d = datetime.date(2016, 8, 11);
f = fitbit.Fitbit(consumer_key, consumer_secret, access_token=access_token, refresh_token=refresh_token, redirect_uri='http://localhost:8080')
#f.client.authorize_token_url()
#f.client.fetch_access_token (redirect_uri='http://localhost:8080' 	)
#f.client.refresh_token()
#print f.client.access_token
sleep = f.get_sleep(d)
print sleep