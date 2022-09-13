import json


class User():
    file = "user.json"

    def __init__(self, id, location, name, user_id):
        self.id = id
        self.location = location
        self.name = name
        self.user_id = user_id

    @classmethod
    def check_email(email, all_users_data):
        for user in all_users_data:
            if email == user['Email']:
                return True
        return False

    # functions which used for adding users to user.json
    @classmethod
    def new_user_add(cls):
        user = {
            "first_name": input("First Name: "),
            "last_name": input("Last Name: "),
            "Email": input("Email: "),
        }
        file = open('database/users.json', 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()
        if len(all_users_data) > 0:
            user['id'] = all_users_data[-1]['id'] + 1
        else:
            user['id'] = 1
        if cls.check_email(user['Email']) == False:
            all_users_data.append(user)
            with open('database/users.json', 'w') as file:
                file.write(json.dumps(all_users_data))
        else:
            print("User with this email already exist!!!")

    @classmethod
    def get_all(cls):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['Email'])

    @classmethod
    def search_by(search_str, what_to_search):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + user['Email'])


    def _generate_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'name': self.name,
            'user_id': self.user_id
        }

    def save(self):
        user_in_dict_format = self._generate_dict()
        user = self.get_file_data(self.file)
        user.append(user_in_dict_format)
        self.save_to_file(user)

