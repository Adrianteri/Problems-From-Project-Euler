def isprime():
    temp = 2
    arrayPrime = []
    while len(arrayPrime) <= 10001:
            if temp % temp == 0 and temp % 1 == 0:
                arrayPrime.append(temp)
            temp = temp + 1

    print "The 10001 prime number is %d" %arrayPrime[10001]
    print (arrayPrime)

isprime()
