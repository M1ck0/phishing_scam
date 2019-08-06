import grequests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*()_+}{:|?><"
random.seed = (os.urandom(1024))

url = "https://romanianxa.gq/Serv/e090f9777728f2044e78674d2bbda89e/Up-dating.php?log=CheckLog"

names = json.loads(open("names.json").read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + "@live.com"
	password = ''.join(random.choice(chars) for i in range(8))

	grequests.post(url, allow_redirects = False, data={
		"1": username,
		"2": password,
		"_eventId_continue": ""
	})
	
	print("sending username %s and password %s" % (username, password))
