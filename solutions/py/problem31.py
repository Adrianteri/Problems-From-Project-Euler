#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?


def getCombs():
    #currency placeholders
    mydict = {'a': 1, 'b':2, 'c':5, 'd':10, 'e':20, 'f':50, 'g':100, 'h':200}
    mydictlen = len(mydict)
    ones,twos,fives,tens,twenties,fifties,oneth,twoth = [],[],[],[],[],[],[],[]
    goal = 200
    counter,step = 0,0

    # step += 1
    # if step == 1: # 1
    for i in mydict.values():
        for j in range(1,201):
            temp = i * j
            if i == 1:
                ones.append(temp)
            elif i == 2:
                twos.append(temp)
            elif i == 5:
                fives.append(temp)
            elif i == 10:
                tens.append(temp)
            elif i == 20:
                twenties.append(temp)
            elif i == 50:
                fifties.append(temp)
            elif i == 100:
                oneth.append(temp)
            elif i == 200:
                twoth.append(temp)
            if temp == goal:
                counter += 1


    print(ones)
    print("\n")
    print(counter)

getCombs()

    # step = 2
    # elif step = 2: # 2
    #     for j in range(1,100):
    #
    # elif step = 3: # 3
    #     for k in range(0,20):
    # elif step = 4: # 4
    #     for l in range(0,10):
    # elif step = 5: # 5
    #     for m in range(0,4):
    # elif step = 5: # 6
    #     for n in range(0,2):
