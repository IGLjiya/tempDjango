

def order_pizza():
    order = input("What is your pizza order :- ")
    # cheese = input("Do you want extra cheese :- ")
    sp = 150
    mp = 200
    lp = 250
    psp = 20
    pmlp = 30
    cs = 10
    sum= 0
    if order == 'sp':
        sum= sp
        pepp = bool(input("Do you want Pepperoni :- "))
        if pepp == True:
            sum = sum+psp
        cheese = bool(input("Do you want extra cheese :- "))
        if cheese == True:
            sum = sum + cs
        print(sum)


    if order == 'mp':
        sum= mp
        pepp = bool(input("Do you want Pepperoni :- "))
        if pepp == True:
            sum = sum+pmlp
        cheese = bool(input("Do you want extra cheese :- "))
        if cheese == True:
            sum = sum + cs
        print(sum)

    if order == 'lp':
        sum= lp
        pepp = bool(input("Do you want Pepperoni :- "))
        if pepp == True:
            sum = sum+pmlp
        cheese = bool(input("Do you want extra cheese :- "))
        if cheese == True:
            sum = sum + cs
        print(sum)



order_pizza()





