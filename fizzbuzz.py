#Create a program that will run through the integers 1 to 25.
#If the number is a multiple of 3, print "Fizz"
#If the number is a multiple of 5, print "Buzz"
#If the number is a multiple of 3 and 5 print "FizzBuzz"
#If the number is not any of the stated multiples, print the number.
#Each output is on it's own line
#Also include in your repo a .drawio file that flowcharts out the logic

#Here is a section of sample output:
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function with n = 25
fizzbuzz(25)
