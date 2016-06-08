import requests
import json

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
		print response
		db = response["payload"]
		print db

#		for data in db:
#			for dict in data:
#				print dict, data(dict)


	def request(self, volt, curr):
    		header = {"Content-Type":"application/json" }
		payload = {"Voltage":"volt","Current":"curr"}
    		url = self.url+'/request'
    		r = requests.post(url = url, headers = header, data = json.dumps(payload))    		
		response = r.json()

		for data in response:
			for dict in data:
				print dict, data(dict)


