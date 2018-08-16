def greet_user(username):
    """Say Hello to anyone"""
    print('Hello ' + str(username).title())
    
    username = username.upper()
    print('Username changed to ' + username)

user_name = input("What's your name: ")
greet_user(user_name)

print(user_name)