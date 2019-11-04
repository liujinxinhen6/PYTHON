class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("The user's name is " + self.first_name + self.last_name + '.')
        print("The first name is " + self.first_name + '.')
        print("The last name is " + self.last_name + '.')
        print("The user's age is " + str(self.age) + '.')

    def greet_user(self):
        print("Welcome " + self.first_name + self.last_name + '!')

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempt(self):
        self.login_attempts = 0


a = User("liu","jinxin",21)
a.describe_user()
a.greet_user()
a.increment_login_attempt()
a.increment_login_attempt()
a.reset_login_attempt()
print(a.login_attempts)
