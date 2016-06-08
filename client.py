import requests
import json

class Client:
	def __init__(self, url):
		self.url = url

	def info_shows (self, response):
		info = response["payload"]
		for array in info:
			print "ID:{}\nVoltaje:{}\nCorriente{}\n'----------'".format(array[0], array[1], array[2])
		

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
		info_shows (self, response)



	def request(self, volt, curr):
    		header = {"Content-Type":"application/json" }
		payload = {"Voltage":"volt","Current":"curr"}
    		url = self.url+'/request'
    		r = requests.post(url = url, headers = header, data = json.dumps(payload))    		
		response = r.json()
		info_shows (self, response)






