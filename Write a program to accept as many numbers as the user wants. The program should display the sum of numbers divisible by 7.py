from array import array

c = 0
a = int(input("enter the no of times you want to enter a no. : "))
array = [a]
nofdivide = 0
for i in range(0, a):
    x = int(input("enter a no. : "))
    array.append(x)
    if x % 7 == 0:
        c = c + x
print(c)