def main():
    # Input the first integer value and assign it the variable 'val1'
    val1 = int(input("Enter the first integer value: ")) 
    
    # Input the second integer value and assign it the variable 'val2'
    val2 = int(input("Enter the second integer value: "))   

    # Input the third integer value and assign it the variable 'val3'
    val3 = int(input("Enter the third integer value:)"))    
    # Get sum of three values and assign it to the variable 'total'
    total = val1 + val2 + val3 

    # Get average and save it as average
    average = total / 3        

    # Print three values in a line
    print(f"Values {val1} {val2} {val3}")

    # Print the total
    print(f"Total: {total}")

    # Print the average with two fractional digits (123.45)
    print(f"Average: {average:.2f}")

    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
