def find_biggest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
game_over = False

while not game_over:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))  # Convert to int
    bids[name] = price

    should_continue = input("Are there any other bids? Type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        game_over = True
        find_biggest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)  # Clears the screen
