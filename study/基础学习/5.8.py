names=['admin','a','b','c','d']
if names:
    for name in names:
        if name=='admin':
            print('Hello admin,would you like to see status report?')
        else:
            print('Hlleo'+name+',thanks for logging in again.')
else:
    print("we need to find users")