# import os
#os.system("pip3 uninstall pyrebase")
#os.system("pip3 install pyrebase3")
import pyrebase 
# https://github.com/acevedog/Pyrebase3

# https://console.firebase.google.com/project/sistemasdistribuidos-4e300/database/sistemasdistribuidos-4e300/data
config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL":"https://sistemasdistribuidos-4e300.firebaseio.com/",
  "storageBucket": ""
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# db.child("alunos").child("Morty")





def edit(idAluno,dataType,data):
 
  # print(db.child("alunos").child(idAluno).val())
  etag = db.child("alunos").child(idAluno).get_etag()
  data = {
    "nome": "MariaJoao",
    "RA": 8888
  }
  response= db.child("alunos").child(idAluno).conditional_set(data, etag)
  
  if "ETag" in response:
      etag = response["ETag"] # our ETag was out-of-date
  else:
      print("Edited data successfully!")
  # print(response)

  # etag = db.child("users").child("Morty").get_etag()
  # response = db.child("users").child("Morty").conditional_remove(etag)


ans=True
while ans:
    print ("""
    1.Add a Student
    2.Edit a Student
    # 2.Delete a Student
    # 3.Look Up Student Record
    # 4.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      print("\n Student Added") 
    elif ans=="2":
      idAluno=input("Student id: ")

      dataType=input("What data do you want to change? ")
      data=input("New Value: ")

      edit(idAluno, dataType, data)
      # print("\n Student Deleted") 
    elif ans=="3":
      print("\n Student Record Found") 
    elif ans=="4":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 



