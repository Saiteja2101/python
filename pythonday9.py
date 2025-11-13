
game_over = False

while not game_over:
    name = input("What is  your name?\n")
    price = input("What is your bid?\n$")

    bids = {}
    bids[name] = price

    should_continue = input("Are there any other bids? type yes or no\n")
    if should_continue == "no":
        game_over = True
        find_biggest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)


def find_biggest_bidder(bidding_dictiony):
    winner = ""
    highest_bid = 0
    max(bidding_dictiony)
    for bidder in bidding_dictiony:
        bid_amount = bidding_dictiony[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder



print(f"The winner is {winner} with a bid of ${highest_bid}.")