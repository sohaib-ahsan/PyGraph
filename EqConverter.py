
def converter(eq):
    eq = eq.lower()
    eq = eq.split('=')[1]
    eq = eq.replace('cube', '**3')
    eq = eq.replace('power', '**')
    eq = eq.replace('square', '**2')
    a = eq.split()
    print(a)
    list1 = [str(x) for x in range(10)]

    for i in range(len(a)-1):
        if a[i] in list1:
            a.insert(i+1, '*')
    a = ''.join(a)
    return a


#print(converter('y = 2 x + x power 3'))