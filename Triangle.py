

#Q. triangle pattern printing:

print('---------------------------------------------------------------------------')
# right side below right angle triangle:
for i in range (1,6):
    for j in range (1,6-i):
        print(" ",end=" ")
    for k in range (1,i+1):
        print("*",end=" ")
    print()
print('---------------------------------------------------------------------------')

# right side upper right angle triangle:
for i in range(1,6):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(1,6-i+1):
        print("*",end=" ")
    print()
print('---------------------------------------------------------------------------')

# triangle:
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*"," ",end=" ")
    print()
print('---------------------------------------------------------------------------')

#left side upper right angle tiangle

for i in range(5,0,-1):

    for k in range(5,i-1+1):
        print(" " ,end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print('---------------------------------------------------------------------------')

# reverse triangle:
for i in range(5,0,-1):
    for j in range(0,5-i):
         print(end=" ")
    for k in range(0,i):
         print("*",end=" ")
    print()

