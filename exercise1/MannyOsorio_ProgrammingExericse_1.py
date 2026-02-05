def main():
    """
    Runs the main ticket purchasing program.
    
    Parameters:
        None
    
    Variables:
        total_tickets_sold (int): The total number of tickets sold so far.
        ticket_amt (int): The number of tickets the user wants to purchase.
    
    Logic:
        1. Initialize total_tickets_sold to 0.
        2. Loop while total_tickets_sold is less than 20.
        3. Prompt the user for the number of tickets to purchase.
        4. Validate the ticket amount using check_condition().
        5. If valid, purchase the tickets and display the result.
    
    Return:
        None
    """
    total_tickets_sold = 0
    total_buyers = 0
    total_tickets = 10

    while total_tickets_sold < total_tickets:
        # Get user input for number of tickets
        ticket_amt = input("How many tickets would you like to purchase (max = 4): ")
        ticket_amt = int(ticket_amt)

        if check_condition(ticket_amt) == True:
            # Add the tickets to the total if valid
            total_tickets_sold = purchase_ticket(total_tickets_sold, ticket_amt)
            total_buyers += 1
            print("Purchase successful")
            print(f"Remaining Tickets: {total_tickets - total_tickets_sold}")

    print(f"Total Buyers: {total_buyers}")
    
def check_condition(ticket_amt: int) -> bool | None:
    """
    Validates that the ticket amount does not exceed the maximum of 4.
    
    Parameters:
        ticket_amt (int): The number of tickets to be purchased.
    
    Variables:
        None
    
    Logic:
        1. Check if ticket_amt is greater than 4.
        2. If true, display an error message.
        3. Otherwise, return True.
    
    Return:
        bool: True if the ticket amount is valid (4 or less), False otherwise.
    """
    # Check if the requested amount exceeds the maximum of 4
    if ticket_amt > 4:
        print("Error: more tickets than the maximum are being purchased")
    else:
        return True

def purchase_ticket(current_ticket_amt: int, ticket_amt: int) -> int:
    """
    Adds purchased tickets to the current total and returns the new total.
    
    Parameters:
        current_ticket_amt (int): The current number of tickets sold.
        ticket_amt (int): The number of tickets being purchased.
    
    Variables:
        total_tickets_sold (int): The updated total number of tickets sold.
    
    Logic:
        1. Add ticket_amt to current_ticket_amt.
        2. Store the result in total_tickets_sold.
        3. Return the new total.
    
    Return:
        int: The updated total number of tickets sold.
    """
    # Calculate the new total by adding purchased tickets to current total
    total_tickets_sold = current_ticket_amt + ticket_amt

    return total_tickets_sold
    
if __name__ == "__main__":
    main()
