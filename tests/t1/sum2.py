# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read


# if I am not supposed to use <break>, then...
total = 0
stilladding = True
iteration = 0

while stilladding and iteration < 10:
    notanumber = True
    while notanumber:
        try:
            number = int(input(str(iteration+1) + ". Please input an integer: "))
            notanumber = False
        except ValueError:
            print("Please input an integer.")
    iteration += 1
    if number == -1:
        stilladding = False
    else:
        total += number


print("Total is: " + str(total))
