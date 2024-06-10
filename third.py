'''Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function'''

max = int(input("Enter upper limit: "))
print("The upper limit is " + str(max))

oddNumbers = []

for i in range(1,max):
    if i % 2 != 0:
        oddNumbers.append(i)

print(oddNumbers)
