def fizzbuzz(num):
        aux1 = num % 5
        aux2 = num % 3

        if (aux1 == 0) and (aux2 == 0):
                return("FizzBuzz")
        elif (aux1 == 0) and (aux2 != 0):
                return("Buzz")
        elif (aux1 != 0) and (aux2 == 0):
                return("Fizz")
        else:
                return("%s"%(num))

	
	
