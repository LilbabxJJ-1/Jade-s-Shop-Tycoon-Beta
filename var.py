import pymongo
with open("file.txt", "r") as f:
  for line in f:
    my_secs = line

client = pymongo.MongoClient(f"mongodb+srv://Jade:{my_secs}@cluster0.ajcet.mongodb.net/cluster0?retryWrites=true&w=majority")
mydb = client["mydatabase"]
mycol = mydb["users"]
username = "Unknown"
password = None
logins = False
tutorial_passed = False

items = {"Item_holder": username, "Coffee" : 1, "Bagel": 1, "Muffin": 1, "Chocolate": 0}
