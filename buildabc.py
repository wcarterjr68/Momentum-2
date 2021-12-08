import string
az_Upper = string.ascii_uppercase
abcs = open("abcs.txt","w")
for x in az_Upper:
    abcs.write(x+"'"+"\n")
abcs.close()

