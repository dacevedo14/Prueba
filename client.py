import requests
import json
from json import dumps

class Client:
	def __init__(self, url):
		self.url = url
	

	def save(self, volt, curr):
		header = {"Content-Type":"application/json" }
		payload = {"Voltage":volt,"Current":curr}
    		url = self.url + '/save'
    		r = requests.post(url = url, headers = header, data = json.dumps(payload))
    		response = r.json()
		
		if "status" in response.keys():
			status = response["status"]
			print "Status: %s" % status
		else:
			return None


	def read(self, volt, curr):
    		header = {"Content-Type":"application/json" }
		payload = {"Voltage":volt,"Current":curr}
    		url = self.url + '/read' 
    		r = requests.post(url = url, headers = header, data = json.dumps(payload))
    		response = r.json()
		db = response["payload"]

		for key in db.keys():
			print key,":",db[key]
		print '-------------'

	def request(self, volt, curr):
		
		header = {"Content-Type":"application/json" }
		payload = {"Voltage":volt,"Current":curr}
		url = self.url+'/requests'
		r = requests.post(url = url, headers = header, data = dumps(payload))    		
		response = r.json()
		db = response["payload"]
				
		for data in db:
			for key in data.keys():
				print key,":", data[key]
			print '--------------------------'
	

			
