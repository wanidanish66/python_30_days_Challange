from functools import reduce

l = [1,2,3,4,5]

squar = lambda x: x*x
sqlist = map(squar,l)
print(list(sqlist))

def even(n):
    if (n % 2 == 0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

sum = lambda x,y : x + y
sum(4,5)

print(reduce(sum,l))