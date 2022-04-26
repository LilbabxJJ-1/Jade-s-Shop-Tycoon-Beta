import os
import replit
import time
import pymongo
import dns
from termcolor import colored
import options
import var



def or_tutorial():
  pass
    

def inv_tutorial():
    replit.clear()
    print(f"{var.username}'s Inventory")
    print("-------------------------------")
    var.items["Item_holder"] = var.username
    for i in var.items:
        if i == "Item_holder":
            pass
        else:
            print(f"{i} - {var.items[i]}")
    if var.username !="Guest":
       var.mycol.insert_one(var.items)
    time.sleep(1.5)
    print(
        "This is your inventory! Small but can grow quickly with a bit of help!"
    )
    time.sleep(1.5)
    print("If you ever need to see the description of a item, you can always just type the item name. Try it now!")
  
    description = None
    while description is None:
        description = input("Item name: ")
        if description.title() in var.items:
         while description != None:
          try:
            print(var.item_descriptions[description.lower()])
            break
            
          except KeyError:
            print("That item does not have a description yet!")
            description = None
            
        else:
            print("\nItem does not exist! Try again!")
            description = None
    q = {"username": var.username}
    result = var.mycol.find({"username": var.username})
    for i in result:
      if i["pt1"] == False:
        var.mycol.update_one(q, { "$set": {"pt1": True}})
    tutorial()


def tutorial():
    result = var.mycol.find({"username": var.username})
    for i in result:
      if i["pt1"] == False or var.username == "Guest":
          replit.clear()
          var.go_to = None
          print(f"{var.username}'s Shopˏˋ°•*⁀➷")
          print("--------------------------")
          print("[1]Inventory\n[2]Orders\n[3]Buy\n[4]Sell")
          time.sleep(2.5)
          print(colored(f"This is your own shop! You can check your inventory..","cyan"))
          time.sleep(2.5)
          print(colored("Buy things!", "green"))
          time.sleep(2.5)
          print(colored("Check incoming orders! And so much more! (Coming soon..)","red"))
          time.sleep(2.5)
          print("We're gonna do the tutorial first! Please enter option 1 to start with inventory!")
          while var.go_to == None:
            try:
               var.go_to = int(input(''))
               if var.go_to == 1:
                   inv_tutorial()
               else:
                 print("Please try again and put 1")
                 var.go_to = None
            except ValueError:
               print("Please try that again! Put the number 1")
               var.go_to = None
      elif i["pt2"] == False or var.username == "Guest":
          var.go_to = None
          time.sleep(1)
          print("\nGood Job! Now that you've seen the inventory, you can learn to sell items!")
          time.sleep(2.5)
          replit.clear()
          print(f"{var.username}'s Shopˏˋ°•*⁀➷")
          print("--------------------------")
          print("[1]Inventory\n[2]Orders\n[3]Buy\n[4]Sell")
          time.sleep(1)
          print("\nNow, select 2 to see orders")
          try:
               var.go_to = int(input(''))
               if var.go_to == 2:
                   or_tutorial()
               else:
                 print("Please try again and put 1")
                 var.go_to = None
          except ValueError:
               print("Please try that again! Put the number 1")
               var.go_to = None
        
        
 

#-----------------------------------------------------------
#Tutorial above

def intro():
  result = var.mycol.find({"username": var.username})
  for i in result:
    if i["Intro_Passed"] != True:
      replit.clear()
      italics = '\033[3m'
      end = '\033[0m'
      print(colored(f"Hey! It's you!! I've been waiting a long bit for you to arrive, {var.username}, right?","cyan"))
      time.sleep(4)
      print(
          colored(
           f"I'm Jade, the very very very amazing shop owner! I'm the best at literally everything I do! I-.. {italics}Jade notices her ranmbling quickly fixes her posture.{end}",
            "cyan"))
      print(
        colored(
            "Sorry!! Anyways, you're new around, yeah? I'm excited to see a new shop owner in the making! Check out everything and come back to me when you're ready!",
            "cyan"))
      q = {"username": var.username}
      result = var.mycol.find({"username": var.username})
      for i in result:
        if i["Intro_Passed"] == False:
          var.mycol.update_one(q, { "$set": {"Intro_Passed": True}})
      time.sleep(10)
      tutorial()
      
    else:
      tutorial()


def guest():
    global username
    global logins
    var.username = "Guest"
    var.logins = "Guests"
    replit.clear()
    red = '\033[91m'
    end = '\033[0m'
    print(
        f"You are now playing a guest and your data will {red}NOT{end} be saved if you refresh or leave this tab"
    )
    print("To log in to your account or make one, please restart the program")
    menu()


def login():
    global username
    global password
    global logins
    replit.clear()
    var.logins = "no"
    tries = 0
    while var.logins != "yes":
        print(colored("User Login", "green"))
        var.username = input("Username: ")
        password = input("Password: ")
        try:
            if var.mycol.find_one(
                {"username":
                 var.username}) == None:  # Searches database for user log
                print(colored("\nAccount not found! (case sensitive)\n",
                              "red"))
                var.logins = "no"
                tries += 1
                if tries % 3 == 0:
                    print(
                        colored(
                            "\nTip... You can sign up by restarting and selecting option 1",
                            "green"))
            else:  # Verifies the password with a specific user
                result = var.mycol.find({"username": var.username})
                for i in result:
                    if i["password"] != password:
                        print(
                            colored("Incorrect Password! (case sensitive)",
                                    "red"))
                        var.logins = "no"
                    else:
                        var.logins = "yes"
        except KeyError:
            pass

    result = var.mycol.find({"username": var.username})
    for i in result:
        if i["password"] == password:
            print(
                colored(
                    f"Welcome back {var.username}! Stats have been restored!",
                    "white"))
            time.sleep(2)
            replit.clear()
            var.logins = "No"
            menu()


def signup():
    global username
    global password
    global logins
    var.username = "."
    replit.clear()
    print(colored("\nUser SignUp", "green"))
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
    userlog = {
        "username": var.username,
        "password": var.password,
        "Tutorial_Passed": var.tutorial_passed,
        "Intro_Passed":var.intro_passed,
        "pt1": var.pt1,
        "pt2": var.pt2,
        "pt3": var.pt3,
        "pt4": var.pt4
    }
    var.mycol.insert_one(userlog)
    replit.clear()
    var.logins = "No"
    print("Finalizing account.")
    time.sleep(1)
    print("Finalizing account..")
    time.sleep(1)
    print("Finalizing account...")
    time.sleep(2)
    print("Account Created!")
    menu()


# ------------------------------------------------------------
# Login/Signup stuff above


def user():
    while (log := input(
            "[1]New user? <-- (Recommended for new players)\n[2]Login\n[3]Play as Guest\n\nUse the numbers\n")
           ) not in ["1", "2", "3"]:
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
            if var.username == "Guest":
                intro()
            elif var.username != "Guest":
                result = var.mycol.find({"username": var.username})
                for i in result:
                    if i["Tutorial_Passed"] == False and i["Intro_Passed"] == False:
                        intro()
                    else: 
                      print("Continuing Tutorial...")
                      time.sleep(1.5)
                      tutorial()
            else:
              pass
        elif choice == 2:
            options.status()
            
        else:
            quit()


menu()
