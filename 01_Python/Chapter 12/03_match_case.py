#  The match case is the same as the switch case in the C programming language.
def http_Statue(status):
    match status:
        case 200:
            return 'ok'
        case 404:
            return 'Not found'
        case 500:
            return 'Internal server error'
        case _: # In C language here default case is present.
            return 'Unknown status'    
        
n=int(input('Enter the http status code : '))
print(http_Statue(n))

