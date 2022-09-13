from models.user import User
import json

class Controller():
    file = 'user.json'

    def add_run(self, ):
        if __name__ == '__main__':

            while True:
                print("1. Add New User\n"
                       + "2. Get All Users\n"
                       + "3. Search\n"
                       + "4. Update User By Id"
                      )
                menu_flag = int(input("Type your choose: "))

    def user_add(self, menu_flag=1):
        if menu_flag == 1:
            id = int(input("ID: "))
            location = input("Location: ")
            name = input("Name: ")
            user_id = int(input("User ID: "))
            user = User(id, location, name, user_id)
            user.save()



    def get_all(cls, menu_flag=2):
        global data
        if menu_flag == 2:
            data = cls.get_file_data(cls.file)
        return data

    def search_by(search_str, what_to_search, menu_flag=3):
        if menu_flag == 3:
            with open('database/users.json', 'r') as file:
                users = json.loads(file.read())
                for user in users:
                    if str(user[what_to_search]).lower() == str(search_str).lower():
                        print("User #" + str(user['id']))
                        print("First Name: " + user['first_name'])
                        print("Last Name: " + user['last_name'])
                        print("Email: " + user['Email'])


    def update_user(cls, menu_flag = 4):
        if menu_flag == 4:
            file = open('database/users.json', 'r')
            users = json.loads(file.read())
            file.close()
            id = int(input("Type id of user which you want to update: "))
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            for user in users:
                if user['id'] == id:
                    user['first_name'] = first_name
                    user['last_name'] = last_name
                    user['Email'] = email

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    @staticmethod
    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()

