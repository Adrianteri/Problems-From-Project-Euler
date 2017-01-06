
arrayFib = []
evenTerms = []
memo = {}
n = 0
#generate fibonnaci numbers below 4 million using memoization
def memoizedFib(n,memo):
    def decorated_func(*fibs):
        if fibs in memo:
            return memo[fibs]
        else:
            memo[fibs] = n(*fibs)
            return memo[fibs]
        return decorated_func

@memoizedFib
def fib(g,arrayFib):
    temp = 0

    if temp <= 4000000000:
        temp = fib(g-2) + fib(g-1)
        arrayFib.append(temp)

    return arrayFib

fib(g,arrayFib)
memoizedFib(n,memo)

def sortEvenTerms(arrayFib,evenTerms):
    evenTerms = [term for terms in arrayFib if term == 0 or term % 2 == 0]
    #for terms in arrayFib:
    #    evenTerms.append(term) if term == 0 or term % 2 == 0

    return evenTerms

sortEvenTerms()

def addTerms(evenTerms):
    print"\nThe sum of the even Fibonacci numbers is %d " % sum(evenTerms)

addTerms()
