import time
import var
import replit


def status():
 replit.clear()
 access = True
 while access==True:
    print("""
        Items Sold: 2946
        """)
    print("\nType: 'Back' to go back to the home menu")
    i = input("")
    if i.lower() == "back":
      access = False
    else:
      


def quit():
  print(f"Logging out of {var.username}...")
  time.sleep(2.5)
  print("Successful")
  print("Come back soon!")