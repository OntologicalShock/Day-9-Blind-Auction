from replit import clear
import art


bidder = ""
bid = int(0)
bidDB = {}
anotherBidder = "yes"

def bidLoop():
    global bidder
    global bid
    global bidDB
    global anotherBidder
    
    print(art.logo)
    bidder = input("what's your name?\n")
    bid = int(input("What's your bid in $?\n"))
    bidDB[bidder] = bid
    anotherBidder = input("Is there another bidder? (y/n)")

bidLoop()
while anotherBidder == "y":
    clear()
    # print(bidDB) #Bit of debugging, ignore.
    bidLoop()

winBidder = max(bidDB, key=bidDB.get)
winBid = bidDB[winBidder]
print(f"The winner is {winBidder} for ${winBid}!")