 #!user/bin/env python
import fitbit
import ConfigParser
import datetime
import os
import time
from fitbit.exceptions import HTTPTooManyRequests
from fitbit.exceptions import HTTPUnauthorized
import argparse
import sys
#this didn't work was getting a missing access token
parser = ConfigParser.SafeConfigParser()
 #Load Settings
 # not sure if the variables need to be double quoted
 # will test inserting the strings and then will test importing the file
 # parser.read('config.ini')
 # consumer_key= parser.get('Login Parameters', 'C_KEY')
 # consumer_secret = parser.get('Login Parameters', 'C_SECRET')
#consumer_key = '229R96'
#consumer_secret = 'e520d1a8a82f5afae1ba40e7cb9a25b6'

#Setup an unauthorised client (e.g. with no user)
unauth_client = fitbit.Fitbit("229R96", "e520d1a8a82f5afae1ba40e7cb9a25b6")
 
#Get data for a user
user_params = unauth_client.user_profile_get(user_id='4RX4QJ')
#print "user params"