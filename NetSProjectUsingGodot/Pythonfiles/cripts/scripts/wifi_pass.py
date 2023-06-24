import os
print("THESES ARE ALL NETWORKS THAT YOU HAVE CONNECTED TO BEFORE : ")
os.system("netsh wlan show profile")
user_ssid_input = input("CAN YOU PLEASE ENTER SSID OF THE TARGET NETWORK \n = ")
os.system("netsh wlan show profile " + user_ssid_input + " key=clear")

input(" Press any key to End ! ")