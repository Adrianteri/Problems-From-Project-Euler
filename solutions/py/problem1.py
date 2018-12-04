array1 = []
array2 = []
array3 = []

#initiliaze array of numbers below 1000
def arrBelow1000(array1):
    for i in range(1,1000):
        array1.append(i)

    return array1

arrBelow1000(array1)

#find multiplesOf3 and multiplesOf5
def multiplesOf3(array1,array2,array3):
    for numbers in array1:
        if numbers % 3 == 0:
            array2.append(numbers)
        elif numbers % 5 == 0:
            array3.append(numbers)

    return array2,array3

multiplesOf3(array1,array2,array3)

def addMultiples(array2,array3):
    sumOfMultiples = 0
    sumOf3Multiples = 0
    sumOf5Multiples = 0

    sumOf3Multiples = sum(array2)
    sumOf5Multiples = sum(array3)

    sumOfMultiples = sumOf3Multiples + sumOf5Multiples

    print "\nThe sum of 3s and 5s Multiples is %d " %(sumOfMultiples)

addMultiples(array2,array3)
