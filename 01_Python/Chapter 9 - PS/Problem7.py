with open('log.txt') as f :
    lines=f.readlines()
lineno=1
for line in lines:
    if 'python' in line.lower():
        lineno+=1
        print(f'Yes! Python is in log file and it is in line number : {lineno}')
        break
else: 
    print('No! Python is not in log file.')