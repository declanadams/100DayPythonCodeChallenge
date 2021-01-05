
from art import logo
import os

clear = lambda: os.system('cls')

print(logo)
bids = {}
bidding_done = False


def find_winner(bidding_record):
	high_bid = 0
	winner = ""

	for bidder in bidding_record:
		bid_amt = bidding_record[bidder]
		if bid_amt > high_bid:
			high_bid = bid_amt
			winner = bidder
	print(f"the winner is {winner} with a bid of $ {high_bid}")		

		


while not bidding_done:
  name = input("what is your name?\n")

  price = int(input("what is your bid?\n"))

  bids[name] = price
  should_continue = input("are there any more bidders type yes or no")
  if should_continue == "no":
	   bidding_done = True
  elif should_continue == "yes":
	  clear()

