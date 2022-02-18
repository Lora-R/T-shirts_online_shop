import json

USERS_FILE_PATH = './db/users.txt'
SESSION_FILE_PATH = './db/session_user.txt'


def register(username, email, password, product):
    user_obj = {
        'username': username,
        'email': email,
        'password': password,
        'product': product
    }

    user_json = json.dumps(user_obj)
    with open(USERS_FILE_PATH, 'r+') as file:
        if file.read() == None:
            file.write(user_json + "\n")
            return True
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username:
                return False
        file.write(user_json + "\n")
        return True


def login(username, password):
    with open(USERS_FILE_PATH, 'r') as file, open(SESSION_FILE_PATH, 'w') as current_session_file:
        # if file.read() == None:
        #     return False
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username and existing_user['password'] == password:
                current_session_file.write(user_line)
                return True
        return False


def current_user():
    with open(SESSION_FILE_PATH, 'r') as file:
        # print(file.read().strip())
        return json.loads(file.read().strip())['username']