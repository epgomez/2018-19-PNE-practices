import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINTS = ["/jokes/count", '/categories', '/jokes/random']
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standard one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
dicts=[]
for i in range(3):
    conn.request(METHOD, ENDPOINTS[i], None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    elem = json.loads(text_json)
    dicts.append(elem)

conn.close()

print()
print('There are {} jokes'.format(dicts[0]['value']))
print()
print('The types of jokes are:')
for i in dicts[1]['value']:
    print('  ', i)
print()
print('Random joke: {}'.format(dicts[2]['value']['joke']))