import requests
import json

url='http://bigentrance.elasticbeanstalk.com/api/users/0000.json'

def sendScan(scanid):
	print("sendScan: " + scanid)
	r = requests.get('http://bigentrance.elasticbeanstalk.com/api/users/0000.json')
	print(json.loads(r.text))
