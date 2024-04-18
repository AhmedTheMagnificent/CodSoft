import re


while(1):
    response = input("What kind of operation do you want to perform?")
    resp = re.findall(r"([A-Za-z0-9]*)$",response) 
    res = response[0] + ".txt"
    if response[0:6] == "create":
        with open(res,"w") as file:
            pass
        cont = input("Do you want to continue? ")
        if cont == "yes":
            continue
        else:
            break
    elif response[0:6] == "update":
        if res is not None:
            try:
                with open(res,"a") as file:
                    file.write(input())
            except:
                raise("File not found, file must be created first")
        cont = input("Do you want to continue? ")
        if cont == "yes":
            continue
        else:
            break
    elif reponse[0:5] == "track":
        with open(res, "r") as file:
            print(file.readlines())
        cont = input("Do you want to continue? ")
        if cont == "yes":
            continue
        else:
            break