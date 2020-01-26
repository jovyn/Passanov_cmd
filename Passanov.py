import pyfiglet
import sys
import getpass
from AddAndStore import AddCredentials
from CheckPasscode import CheckMasterPass, CheckSecretAns
from ShowData import ViewCredentials

banner = pyfiglet.figlet_format("Passanov")  + "\n" + "Version 0.0.1 Prototype - 2020 \n"
usage = "\n Usage : " \
        "\n To Add credentials  --> python Passanov.py add \n" \
        "\n To view credentials --> python Passanov.py view \n"

if __name__ == "__main__":
    print(banner)
    master_passcode = input("Enter the Master Password : ")
    secret_answer = input("Which City Were you born in ?? : ")

    if len(sys.argv) == 2:

        if str(sys.argv[1]) == 'add':
            #print("add")
            if CheckMasterPass(master_passcode) and CheckSecretAns(secret_answer) == True :
                AddCredentials(master_passcode,secret_answer)

        elif str(sys.argv[1]) == 'view':
            #print("View")
            if CheckMasterPass(master_passcode) and CheckSecretAns(secret_answer) == True:
                ViewCredentials(master_passcode,secret_answer)

        else :
            print(usage)
            sys.exit(1)

    else:
        print(usage)
        sys.exit(1)


