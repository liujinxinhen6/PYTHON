currt_users=['a','b','c','d','e']
new_users=['a','D','e','h','t']
for new_user in new_users:
    if new_user.title() in currt_users:
        print(new_user+' you need input other user')
    else:
        print(new_user+' the name is not used')
