import os
user_input = input("PLEASE ENTER A WEBSITE TARGET \n =")

os.system("curl -Is " + user_input)
input(" Press any key to End ! ")