

#factorial

num = int(input("enter a #:"))
factorial = 1
if num < 0:
    print("not for negative numbers")
elif num == 00:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(factorial)


#double it

def Doubleit():
    input_string = input("enter phrase:")
    output=" "

    for i in input_string:
        output = output + i + i
    print(output)

#camelcase

def camelCode():

    lol = input(str("Enter file name:"))

    a = lol.title()

    b = a.replace(" ", "")

    c = b.replace("/", "-")

    d = c[0].lower() + b[1:]

    print(d)


def main():
    camelCode()
    #Doubleit()
    #factorial()


if __name__ == "__main__":
    main()






    
    
    
