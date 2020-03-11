list_one = [1, 1, 1, 1, 1, 0]


def toDecimal(binaryList, start, num=0, add=0):
    if(start == -1):
        return 0
    elif(binaryList[start] != 0):
        add += 2**num
    return toDecimal(binaryList, start-1, num+1) +add

print(toDecimal(list_one, len(list_one)-1))