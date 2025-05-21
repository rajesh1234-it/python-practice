#Blind Auction
# Function to find the highest bidder from the dictionary
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n🏆 The winner is {winner} with a bid of ${highest_bid}.")

# Main auction logic
def blind_auction():
    print("Welcome to the Blind Auction Program!")
    bids = {}  # Dictionary to store bidder names and their bid amounts
    continue_bidding = True

    while continue_bidding:
        name = input("Enter your name: ")
        bid = int(input("Enter your bid amount: $"))

        # Store the bid in the dictionary
        bids[name] = bid

        # Ask if there are more bidders
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == 'no':
            continue_bidding = False

    # Determine and display the winner
    find_highest_bidder(bids)

# Run the auction
if __name__ == "__main__":
    blind_auction()
