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

 #Load Settings
 # not sure if the variables need to be double quoted
 # will test inserting the strings and then will test importing the file
 # parser.read('config.ini')
 # consumer_key= parser.get('Login Parameters', 'C_KEY')
 # consumer_secret = parser.get('Login Parameters', 'C_SECRET')
consumer_key = '229R96'
consumer_secret = 'e520d1a8a82f5afae1ba40e7cb9a25b6'
u_key = '3ed195d7f3e022c8601d76233c1a13bd50d1f6f5'
u_secret = 'eheeP2dfGqYYOIyO5FNN9Y6oFEiKrq'

oauth_app = fitbit.Fitbit(consumer_key, consumer_secret)
oauth_client = fitbit.FitbitOauth2Client(u_key, u_secret)


