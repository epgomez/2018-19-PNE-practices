import json
import termcolor

f = open('person.json', 'r')

people = json.load(f)

print()
print('Number of people in the database: {}'.format(len(people)))
print()

for person in people:

    termcolor.cprint('Name: ', 'green', end='')
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint('Age: ', 'green', end='')
    print(person['age'])

    termcolor.cprint('Phone numbers: ', 'green',end='')
    print((len(person['phonenumber'])))

    for i, num in enumerate(person['phonenumber']):
        termcolor.cprint(' Phone {}'.format(i),'blue', end='\n')

        termcolor.cprint('      Type: ', 'red', end='')
        print(num['type'])

        termcolor.cprint('      Number: ', 'red', end='')
        print(num['number'])
