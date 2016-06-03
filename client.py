import requests

import json





class Client(Object):

	def __init__(self, url):
	
	self.url = url



	def concat_payload (self, volt, curr)
		return {"Voltage":vol,"Current":curr}

	def info_shows (self, response)
		info = response["payload"]
		for array in info
			print "ID:{}\nVoltaje:{}\nCorriente{}\n'----------'".format(array[0], array[1], array[2])
		

	def save(self, volt, curr):

		header = {"Content-Type":"application/json" }

		payload = concat_payload (volt, curr)
    		url = "'url'+'/save'"

    		r = requests.post(url = url, headers = header, data = json.dumps(payload))
    		response = r.json()
		print "Status: %d" % response



	def read(self, volt, curr):

    		header = {"Content-Type":"application/json" }

		payload = concat_payload (volt, curr)
    		url = "'url'+'/read'"

    		r = requests.post(url = url, headers = header, data = json.dumps(payload))
    		response = r.json()
		info_shows (self, response)



	def request(self, volt, curr):
  %comparación
    		header = {"Content-Type":"application/json" }

		payload = concat_payload (volt, curr)
    		url = "'url'+'/request'"

    		r = requests.post(url = url, headers = header, data = json.dumps(payload))    		
		response = r.json()
		info_shows (self, response)






