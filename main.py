import os
import replit
import time
import pymongo
import dns
from termcolor import colored
import options
import var

 
def inv_tutorial():
  print(f"{var.username}'s Inventory")
  print("-------------------------------")
  print("")

def tutorial():
  replit.clear()
  go_to = None
  print(f"{var.users} Shopˏˋ°•*⁀➷")
  print("--------------------------")
  print("[1]Inventory\n[2]Orders\n[3]Buy\n[4]Sell\n")
  time.sleep(2.5)
  print(colored(f"This is your own shop! You can check your inventory..", "cyan"))
  time.sleep(2.5)
  print(colored("Buy things!", "green"))
  time.sleep(2.5)
  print(colored("Check incoming orders! And so much more! (Coming soon..)", "red"))
  time.sleep(2.5)
  print("We're gonna do the tutorial first! Please enter option 1 to start with inventory!")
  while go_to == None:
    try:
      go_to = int(input(' '))
      if go_to == 1:
        inv_tutorial()
      elif go_to == 2:
        
        quit()
      else:
        print("Please try that again! Put the number 1")
        go_to = None
    except ValueError:
      print("Please try that again! Put the number 1")


def intro():
  replit.clear()
  italics = '\033[3m'
  end = '\033[0m'
  print(colored(f"Hey! It's you!! I've been waiting a long bit for you to arrive, {users}, right?", "cyan"))
  time.sleep(4)
  print(colored(f"I'm Jade, the very very very amazing shop owner! I'm the best at literally everything I do! I-.. {italics}Jade notices her ranmbling quickly fixes her posture.{end}", "cyan"))
  print(colored("Sorry!! Anyways, you're new around, yeah? I'm excited to see a new shop owner in the making! Check out everything and come back to me when you're ready!", "cyan"))
  time.sleep(7)
  tutorial()

def guest():
  global username
  global logins
  var.username = "Guest"
  var.logins = "Guests"
  replit.clear()
  red = '\033[91m'
  end = '\033[0m'
  print(f"You are now playing a guest and your data will {red}NOT{end} be saved if you refresh or leave this tab")
  print("To log in to your account or make one, please restart the program")
  menu()



def login():
    global username
    global password
    global logins
    var.logins = "no"
    tries = 0
    while var.logins != "yes":
        print(colored("\nUser Login", "green"))
        var.username = input("Username: ")
        password = input("Password: ")
        try:
            if var.mycol.find_one({"username": var.username}) == None:  # Searches database for user log
                print(colored("\nAccount not found! (case sensitive)\n", "red"))
                var.logins = "no"
                tries += 1
                if tries % 3 == 0:
                    print(colored(
                        "\nTip... You can sign up by restarting and selecting option 1", "green")
                    )
            else:  # Verifies the password with a specific user
                result = var.mycol.find({"username": var.username})
                for i in result:
                    if i["password"] != password:
                        print(colored("Incorrect Password! (case sensitive)","red"))
                        var.logins = "no"
                    else:
                       var.logins = "yes"
        except KeyError:
            pass

    result = var.mycol.find({"username": var.username})
    for i in result:
        if i["password"] == password:
            print(colored(f"Welcome back {var.username}! Stats have been restored!", "white"))
            time.sleep(2)
            replit.clear()
            var.logins = "No"
            menu()


def signup():
    global username
    global password
    global logins
    var.username = "."
    print("\nUser SignUp\n")
    while var.username != "":
        var.username = input("Username: ")
        try:
            if var.mycol.find_one({"username": var.username}) != None:
                print("User already exist, try again")
                var.username = "."
            else:
                break
        except KeyError:
            pass
    var.password = input("Password: ")
    userlog = {"username": var.username, "password": var.password, "Tutorial_Passed": var.tutorial_passed}
    var.mycol.insert_one(userlog)
    replit.clear()
    logins = "No"
    print("Finalizing account.")
    time.sleep(1)
    print("Finalizing account..")
    time.sleep(1)
    print("Finalizing account...")
    time.sleep(2)
    print("Account Created!")
    main()


# ------------------------------------------------------------
# Login/Signup stuff above


def user():
    while (log := input("[1]New user?\n[2]Login\n[3]Play as Guest\n\nUse the numbers\n")) not in ["1", "2","3"]:
        print("I don't know that option, please try again\n")
    if log == "1":
        signup()
    elif log == "2":
        login()
    else:
        guest()


def menu():
   print(colored(f"Welcome to Jade's Shop Tycoon", "magenta"))
   if var.logins == False:
     print("Not Logged In..")
     user()
   else:
     print(f"Player {var.username}")
     print("-------------------------------")
     print("[1]Play \n[2]Stats \n[3]Exit/Log Out")
     choice = int(input(""))
     if choice == 1:
       result = var.mycol.find({"username": var.username})
       for i in result:
          if i["Tutorial_Passed"] == False:
            intro()
     elif choice == 2:
       status()
     else:
       quit()
 
menu()
