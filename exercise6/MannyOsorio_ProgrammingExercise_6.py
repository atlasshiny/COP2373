import re


def validate_ssn(value: str) -> bool:
    """
    Validates whether the input is a Social Security Number (XXX-XX-XXXX).
    
    Parameters:
        value (str): The string to validate.
    
    Variables:
        pattern (str): The regex pattern for a valid SSN.
    
    Return:
        bool: True if the string is a valid SSN, False otherwise.
    """
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, value))


def validate_phone(value: str) -> bool:
    """
    Validates whether the input is a US phone number.
    
    Parameters:
        value (str): The string to validate.
    
    Variables:
        pattern (str): The regex pattern for a valid phone number.
    
    Return:
        bool: True if the string is a valid phone number, False otherwise.
    """
    pattern = r"^(\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4}|\d{10})$"
    return bool(re.match(pattern, value))


def validate_zip(value: str) -> bool:
    """
    Validates whether the input is a US zip code (XXXXX or XXXXX-XXXX).
    
    Parameters:
        value (str): The string to validate.
    
    Variables:
        pattern (str): The regex pattern for a valid zip code.
    
    Return:
        bool: True if the string is a valid zip code, False otherwise.
    """
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, value))


def main():
    """
    Runs the main input validation program.
    
    Parameters:
        None
    
    Variables:
        ssn (str): The user's input for a Social Security Number.
        phone (str): The user's input for a phone number.
        zipcode (str): The user's input for a zip code.
    
    Return:
        None
    """
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")

    #check if ssn is valid
    if validate_ssn(ssn):
        print(f'"{ssn}" is a valid SSN.')
    else:
        print(f'"{ssn}" is NOT a valid SSN.')

    phone = input("Enter a phone number: ")

    #check if phone number is valid
    if validate_phone(phone):
        print(f'"{phone}" is a valid phone number.')
    else:
        print(f'"{phone}" is NOT a valid phone number.')

    zipcode = input("Enter a zip code: ")
    
    #check if zip code is valid
    if validate_zip(zipcode):
        print(f'"{zipcode}" is a valid zip code.')
    else:
        print(f'"{zipcode}" is NOT a valid zip code.')


if __name__ == "__main__":
    main()