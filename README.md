#CURT SDA Task Solution
======
Library GUI software  written in Python with the taste of OOP and pyqt5.

![screenshot of the UI](https://github.com/Mahmoussam/Library_system/blob/master/Screenshot%202023-09-01%20203717.png)

Library.py is the main code, based on JSON file input
Library_firebase.py is the main code based on Firebase
```
#Requirements:
Pyqt5
pyrebase
pprint
```
```
//Thoughts and to-add
//Add an extra class to handle the main logic flow and UI,in other words, make Library.py a model, not model+View+control 
//This enables the idea of creating a parent Library class with primary functions and extending it to 2 classes (JSON-based input  , FireBase-based input)

//In order to enhance the role of Firebase in this app, we may need to apply multithreading (QThread?) , It is no problem in this case because the app is pretty simple with basic functions, no much networking or loading for example.
```
