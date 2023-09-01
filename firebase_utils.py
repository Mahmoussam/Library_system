import pyrebase
import json
class FireBase():
    default_config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "databaseURL":""
    }
    def __init__(self,config=default_config):
        firebase = pyrebase.initialize_app(config)
        self.db=firebase.database()
    def re_set(self,data):
        self.db.remove()
        self.db.set(data)
    def raw_load_books(self):
        return dict(self.db.get().val())
    def delete_book(self,title):
        self.db.child(title).remove()
if __name__=='__main__':
    fb=FireBase()
    with open('books.json','r') as file:
        data=json.load(file)
        #fb.re_set(data)
        fb.delete_book('Clean Code')
        print(dict(fb.raw_load_books()))
        
