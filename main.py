import os
print("AUTO RUN IS ENABLED.")
os.system("python src/manage.py runserver 0.0.0.0:3000")
while True:
  print("\n")
  option = ""
  optionb = ""
  optionc = ""
  option = input("Would you like to run the server? (Y/n)")
  if option == "Y":
    os.system("python src/manage.py runserver 0.0.0.0:3000")
  else:
    optionb = input("Would you like to migrate the server? (Y/n)")
    if optionb == "Y":
      
        
        os.system("python src/manage.py makemigrations")
        os.system("python src/manage.py migrate")
    else:
      optionc = input("Would you like to create a superuser (Y/n)")
      if optionc == "Y":
        os.system("python src/manage.py createsuperuser")

"""
이건 그냥 기본 틀 ㅋㅋ 옆에 채팅으로 확인해주세요

음... ㅋㅋㅋ 
아
그래서 일단 src/participater/views.py 로 가세요

"""
        