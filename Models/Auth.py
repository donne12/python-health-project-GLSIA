from .Helpers import loadAuthUsersStore
import bcrypt # pip install bcrypt


class Authenticate :
    username: str
    password : str

    def __init__(self, username, password):
        self.username = username
        self.password = password

    


    def checkUser(self):
        data = loadAuthUsersStore()
        for k, v in data.items():
            for m, n in v.items():
                n["password"].encode('utf-8')
                if n["username"] == self.username and bcrypt.checkpw(self.password, str(n["password"]).encode('utf-8')) :
                    return True
                else :
                    return False