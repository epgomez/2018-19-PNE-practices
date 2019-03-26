import http.client
import json


HOSTNAME = "api.github.com"
ENDPOINTS = ["/users/", '/repos/']
GITHUB_ID = input('Enter the user you want to check: ')
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)


conn.request(METHOD, ENDPOINTS[0] + GITHUB_ID, None, headers)
r1 = conn.getresponse()

print("\nResponse received from {}: {} {}".format('r1', r1.status, r1.reason))

text_json = r1.read().decode("utf-8")
user = json.loads(text_json)

name = user['name']
print(name)

conn.request(METHOD, ENDPOINTS[1] + GITHUB_ID + '/2018-19-PNE-practices/commits', None, headers)
r2 = conn.getresponse()

print("\nResponse received from {}: {} {}".format('r2', r2.status, r2.reason))

text_json2 = r2.read().decode("utf-8")
commits = json.loads(text_json2)

num_commits = len(commits)
print(num_commits)

conn.request(METHOD, ENDPOINTS[0] + GITHUB_ID, None, headers)
r3 = conn.getresponse()

print("\nResponse received from {}: {} {}".format('r3', r1.status, r1.reason))

text_json3 = r3.read().decode("utf-8")
repos = json.loads(text_json)



conn.close()