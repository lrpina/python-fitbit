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

DUMP_DIR = '../fitbit-dumps'

#double checks that it is a string, but needs to be entered with format 'YYYY-MM-DD' (or with double quotes)
def mkdate(datestr):
	try:
		fulltime = time.strptime(datestr, '%Y-%m-%d')
		return datetime.date(fulltime.tm_year, fulltime.tm_mon, fulltime.tm_mday)
	except ValueError:
		raise argpase.ArgumentTypeError(datestr + ' is not a proper date string')

#returns a message with a date, but there's a place where the word, None, comes out and I don't know where
#that is coming from
def logmsg(msg):
	time = datetime.datetime.now()
	print("[%04i/%02i/%02i %02i:%02i:%02i]: %s" % (time.year, time.month, time.day, time.hour, time.minute, time.second, msg))

#haven't figure out how to make this one work	
def dump_to_str(data):
	return "\n".join(["%s,%s" % (str(d['time']), d['value']) for d in data])

#print out type of argument
def dump_to_json_file(data_type, date, data):
	directory = "%s/%i/%s" % (DUMP_DIR, date.year, date)
	if not os.path.isdir(directory):
		os.makdirs(directory)
	with open ("%s/%s.json" % (directory, data_type), "w") as f:
		f.write(json.dumps(data, indent=2))
	time.sleep(1)


def previous_dumped(date):
	return os.path.isdir("%s/%i/%s" % (DUMP_DIR, date.year, date))

# def dump_day (c, date):
# 	steps_data = c.intraday_time_series('activities/steps', base_date=date, detail_level='1min', start_time=None, end_time=None)
# 	steps = steps_data['activities-steps-intraday']['dataset']
#      # Assume that if no steps were recorded then there is no more data
#     if sum(s['value'] for s in steps) == 0:
#         return False
 
#     dump_to_json_file("steps", date, steps_data)
 
#     cals_data = c.intraday_time_series('activities/calories', base_date=date, detail_level='1min', start_time=None, end_time=None)
#     dump_to_json_file("calories", date, cals_data)
 
#     distance_data = c.intraday_time_series('activities/distance', base_date=date, detail_level='1min', start_time=None, end_time=None)
#     dump_to_json_file("distance", date, distance_data)
 
#     floor_data = c.intraday_time_series('activities/floors', base_date=date, detail_level='1min', start_time=None, end_time=None)
#     dump_to_json_file("floors", date, floor_data)
 
#     sleep_data = c.get_sleep(date)
#     dump_to_json_file("sleep", date, sleep_data)
#     return True
 
parser = ConfigParser.SafeConfigParser()

consumer_key = '229R96'
consumer_secret = 'e520d1a8a82f5afae1ba40e7cb9a25b6'
u_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0Ulg0UUoiLCJhdWQiOiIyMjlSOTYiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDgxMDc3MzE5LCJpYXQiOjE0ODEwNDg1MTl9.QAD7eoeiig41v_E8Y901qkDYne6vuRziUOJ8Qusfw2U'
u_secret = 'b4ede7267445c5e37438d297b2971fc51e129781be5a9930a47bb598d1e4918a'

#d = datetime.date(2016, 7, 23)
authd_client = fitbit.Fitbit(consumer_key, consumer_secret, access_token=u_key, refresh_token=u_secret)
# #body_stats = authd_client._COLLECTION_RESOURCE('body')
# #print body_stats 

# #sleep = authd_client.sleep()
#print sleep
d = '2016-07-23'
d = mkdate(d)
sleep = authd_client.get_sleep(d)
print sleep
print dump_to_json_file('json', sleep, d)




 
