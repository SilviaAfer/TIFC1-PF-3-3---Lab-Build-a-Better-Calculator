def main():
  print("Welcome to my new and better calculator By Silvi!")

if __name__=="__main__":
  main()

#This is for the New Lab, Building a new and better calculator

  #Addmultiplenumbers([num, num, ..])
def addmultiplenumbers(numbers) :
    total = 0
    for num in numbers:
        total += num
    return total

#Multiplymultiplenumbers
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

#Isiteven 
def isiteven(num):
    # Must be an integer AND divisible by 2
    return isinstance(num, int) and num % 2 == 0

#isitaninteger(num)
def isitaninteger(num):
    return isinstance(num, int)


def main():
    print("Bye bye!")


if __name__ == "__main__":
    main()
