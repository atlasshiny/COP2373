def main():
    """
    Runs the main spam scoring program.

    Parameters:
        None

    Variables:
        word_list (list[str]): The list of spam words and phrases.
        test_email (str): The email message loaded from the file.
        score (int): The computed spam score for the message.
        matches (list[str]): The words/phrases found in the message.
        likelihood (str): The human-readable spam likelihood rating.

    Logic:
        1. Define the spam word list.
        2. Load the test email message from a file.
        3. Scan the email for spam words and compute the score.
        4. Convert the score into a likelihood rating.
        5. Display the score, rating, and matched words.

    Return:
        None
    """
    # spam world list
    word_list = [
        "Free",
        "Cash",
        "Bonus",
        "Winner",
        "Prize",
        "Refund",
        "Guaranteed",
        "Discount",
        "Profit",
        "Million",
        "Urgent",
        "Immediate",
        "Instant",
        "Limited",
        "Expire",
        "Hurry",
        "Now",
        "Important",
        "Alert",
        "Final",
        "Verify",
        "Login",
        "Suspended",
        "Password",
        "Secure",
        "Update",
        "Account",
        "Billing",
        "Access",
        "Activity",
    ]
    # import the test email
    with open("./exercise2/test_email.txt", "r", encoding="utf-8") as f:
        test_email = f.read()

    score, matches = check_word_list(word_list, test_email)
    likelihood = rate_spam(score)

    print("Spam score:", score)
    print("Likelihood:", likelihood)
    print("Matched words/phrases:", ", ".join(matches) if matches else "None")

def check_word_list(word_list: list[str], email: str) -> tuple[int, list[str]]:
    """
    Scans the email for spam words and returns the score and matches.

    Parameters:
        word_list (list[str]): The list of spam words and phrases.
        email (str): The email message to scan.

    Variables:
        email_lower (str): Lowercase version of the email message.
        score (int): The number of spam words found.
        matches (list[str]): The spam words/phrases found in the email.

    Logic:
        1. Convert the email to lowercase.
        2. For each word in the word list, check if it appears in the email.
        3. If found, increment the score and record the word.

    Return:
        tuple[int, list[str]]: The spam score and list of matched words.
    """
    email_lower = email.lower()
    score = 0
    matches = []

    for word in word_list:
        if word.lower() in email_lower:
            score += 1
            matches.append(word)

    return score, matches

def rate_spam(score: int) -> str:
    """
    Converts a numeric score into a spam likelihood rating.

    Parameters:
        score (int): The spam score calculated from the message.

    Variables:
        None

    Logic:
        1. Use score thresholds to classify the message.
        2. Return a descriptive likelihood label.

    Return:
        str: The likelihood rating for the message.
    """
    if score <= 2:
        return "Unlikely spam"
    if score <= 5:
        return "Possible spam"
    return "Likely spam"

if __name__ == "__main__":
    main()