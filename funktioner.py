# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna

# TODO Skriv ut att namnet är bäst
# Ex: "Katherine" in - skriver ut "Katherine är bäst"
pass

def best(name):
    print(name,"is best")

best("Hundaol")

# TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
pass
def square(number):
      return number**2
print(square(30))
print(square(65))



def sums(a, b):
    return a+b

print(sums(9, 8))
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
pass



# Nu blir det lite svårare


def maximum(a, b, c):
    if a > b and a > c:
     return a
    elif b < c:
     return c 
    else:
     return b
    return maximum(a,b,c)
print(maximum(89,3,200))
    
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
pass


def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass