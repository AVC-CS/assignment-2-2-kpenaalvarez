def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input("Enter your temperature in Celsius:"))
    fahrenheit = (celsius *9/5) + 32
    print(f"Temperature is {fahrenheit:.2f} fahrenheit")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
