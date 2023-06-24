import os

user_QR_Code = input("ENTER A TARGET WEBSITE \n = ")
os.system("curl qrenco.de/"+user_QR_Code)
input(" Press any key to End ! ")