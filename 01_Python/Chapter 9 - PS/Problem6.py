with open('log.txt') as f :
    content=f.read()

if 'python' in content.lower():
    print('Yes! Python is in log file.')
else:
    print('No! Python is not in log file.')