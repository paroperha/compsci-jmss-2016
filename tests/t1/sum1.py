# write a program that reads in 10 numbers, then prints the sum of those

total = 0

for iteration in range(10):
    notanumber = True
    while notanumber:
        try:
            number = int(input(str(iteration+1) + ". Please input an integer: "))
            notanumber = False
        except ValueError:
            print("Please input an integer.")
    total += number

print("Total is: " + str(total))