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

#runThrough = range(1, 26)
#fBlist = (())
#for x in runThrough:

#        if x % 3 == 0:
#            runThrough.pop(x)
#            runThrough.insert(x, "Fuzz")
#print(runThrough)

fizzList = [x for x in range(1, 26) if x % 3 == 0]
buzzList = [x for x in range(1, 26) if x % 5 == 0]

runThrough = range(1, 26)

for x in runThrough:
    if x in (fizzList and buzzList):
        x = "FizzBuzz"
    if x in fizzList:
        x = "Fizz"
    if x in buzzList:
        x = "Buzz"
    else:
        print(x)

