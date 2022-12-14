from replit import clear
#HINT: You can call clear() to clear the output in the console.

bidder_dict = {}

print("Welcome to the secret auction program.")

def ask_user():
  global user_name 
  user_name = input("What is your name? ")
  global user_bid
  user_bid = input("What is your bid? ")
  global other_bidders 
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear() 
  bidder_dict[user_name] = user_bid

ask_user()

final_bid = 0
final_bidder = ''

while other_bidders == 'yes':
  ask_user()
  for x in bidder_dict:
    if int(bidder_dict[x]) > int(final_bid):
      final_bid = bidder_dict[x]
      final_bidder = x
  
print(f"The winner is {final_bidder} with a bid of ${final_bid}.")