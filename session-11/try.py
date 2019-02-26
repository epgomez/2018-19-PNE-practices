with open('index.html', 'r') as f:
    content = ''
    for line in f:
        content += line
print(content)