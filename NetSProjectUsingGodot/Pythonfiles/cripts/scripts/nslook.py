import os
user_website_input = input("PLS ENTER THE TARGET WEBSITE \n = ")
print("THERE IS YOUR VALID INFOS :")
os.system("nslookup " +user_website_input)
input(" Press any key to End ! ")