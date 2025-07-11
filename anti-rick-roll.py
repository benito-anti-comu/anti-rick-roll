#lib
from time import sleep
import requests

#start of program
while True:
    #for a security
    try:
        user_text = input("enter a URL: ")

        #see the URL if is ok
        try:
            r = requests.get(user_text, timeout=5)
        except requests.exceptions.MissingSchema:
            print("Invalid URL.")
            quit()
        except requests.exceptions.ConnectionError:
            print("ERROR CONNECTION.")
            quit()

        #see if is a rick roll
        if "Rick Astley" in r.text or "rick astley" in r.text:
            print("this is a rick roll, stop the program?")
            sleep(2)
            Re_user = input("YES/NO: ")
            if Re_user == "yes" or Re_user == "YES":
                quit()
            elif Re_user == "no" or Re_user == "NO":
                pass
        else:
            print("this isn't a rick roll")
            sleep(2)

    except KeyboardInterrupt:
        print("stop program from Keyboard")
        quit()
