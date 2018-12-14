# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

#Generator for numbers
def number_generator(n):
    a_three_five = []
    for i in range(1,n+1):
        a_three_five.append(multiple_checker(i))


    print("The sum of multiples of 3 and 5 under 1000 is {} ".format(sum(a_three_five)))    

def multiple_checker(digit):
    if digit % 3 == 0 or digit % 5 == 0:
        print(digit)
        return digit
    else:
        return 0    

if __name__ == "__main__":
    number_generator(1000)