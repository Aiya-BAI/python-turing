class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'全名：{self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'hello {self.first_name} {self.last_name}')


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('管理员权限有：')
        for privilege in self.privileges:
            print(f'-{privilege}')


admin = Admin('bai', 'yunce')
admin.privileges.show_privileges()
