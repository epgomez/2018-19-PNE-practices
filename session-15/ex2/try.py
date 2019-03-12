msg = 'localhost:8000/echo?msg=e&chk=on'.partition('=')[2].split('&')[1].split('=')[1]

print(msg)