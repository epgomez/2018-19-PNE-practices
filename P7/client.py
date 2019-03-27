# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import termcolor
from Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method
conn.request("GET", "sequence/id/ENSG00000165879?content-type=application/json")
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
msg = json.loads(data1)

seq = Seq(msg['seq'])

#How many bases are there in the FRAT1 gene?
#How many T bases are there in the FRAT1 gene?
#Which base is the most popular in the FRAT1 gene? What is its percentage?
#Calculate the percentage of all the bases in the FRAT1 gene

lenght = seq.len()
count_t = seq.count('T')

bases = ('A','C','T','G')
numbases = ''

for i in bases:
    if seq.count(i)>numbases: popular, numbases = i, seq.count(i)

print('Lenght: {}'.format(lenght))
print()
print('Number of T: {}'.format(count_t))
print()
print('The most popular base is {}, its percentage is {}%'.format(popular, seq.perc(popular)))
print()
termcolor.cprint('Percentages: ', 'green')
for i in bases:
    print('  Base {}: {}%'.format(i,seq.perc(i)))