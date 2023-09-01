import pyrebase

config = {
  "apiKey": "AIzaSyDagD8S-hRiJNPdvCn0wjhfCxmelGTHzbk",
  "authDomain": "library-system-81139.firebaseapp.com",
  "projectId": "library-system-81139",
  "storageBucket": "library-system-81139.appspot.com",
  "messagingSenderId": "24319336607",
  "appId": "1:24319336607:web:a2d01a3c331e224cc902aa",
  "databaseURL":"https://library-system-81139-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()

#push
#data={"name":"Palo","age":200,"addr":"ox9D"}
#db.push(data)
