# Write a Python algorithm that, given a list of numbers, separates the odd and even numbers from the
# original list into two new lists and prints the two lists created.
def seperate_odd_and_even(numbers):
    even = []
    odd = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return odd, even


x,y = seperate_odd_and_even([1,11,111,2,22,222])
print(x,"\n",y)

# chcemy wypisać  liczby od 1 do 100, podzielne przez 3
for i in range(1,101):
    if i %3 == 0:
        print(i)


# Tworzymy listę produktów, które kupił użytkownik, aż nie wpiszę 'q'

products = []
p = " "
while (p !="q"):
    p = input("Please write a product name or exit with 'q' \n")
    if p != "q":
        products.append(p)

print(products)

