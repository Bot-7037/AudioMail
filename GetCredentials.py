def GetCredentials(type):

    # Read username and password
    f = open('./Files/credentials', 'r')
    creds = f.read()
    username = creds.split()[0]
    password = creds.split()[1]
    if(type == 'recieve'):
        return(username, password)
    # Read contacts
    f = open('./Files/contacts', 'r')
    arr = f.read().split()
    for i in range(len(arr)):
        print(i+1, arr[i])
    choice = int(input("Enter choice : "))
    return(username, password, arr[choice-1])   