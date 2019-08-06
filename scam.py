import grequests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*()_+}{:|?><"
random.seed = (os.urandom(1024))

url = "url"

names = json.loads(open("names.json").read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + "@live.com"
	password = ''.join(random.choice(chars) for i in range(8))

	grequests.post(url, allow_redirects = False, data={
		"username": username,
		"password": password
	})
	
	print("sending username %s and password %s" % (username, password))
