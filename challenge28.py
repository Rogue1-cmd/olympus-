# Prime numbers
import time
print("Hello, there. Welcome")
active = True

while active:
    choice = input("What would you like to do? \n \
          \t 1. Check if number is prime.\n \
          \t 2. Check prime numbers for a range of values. \n \
          \n\t Enter Choice : ")
    #if user wants to check whether number is prime      
    if choice == "1":
        num = int(input("Enter number: "))
        prime_status = True
        for number in range (2,num): 
            if (num%number) == 0:
                prime_status = False
                break
        if prime_status :
            print(num, " is a prime number.")  
        else:
            print(num, " is not a prime number.")  

    #if user wants to check for prime number within certain range
    elif choice == "2":
        primes = []
        upper = int(input("Enter upper limit:\t"))
        lower = int(input("Enter lower limit:\t"))
         
        start = time.time()
        for number in range(lower, upper+1):
            if number > 1:
                prime_status = True
                for i in range(2, number):                    
                    if (number%i) == 0: #if there is no remainder after division, flag becomes false
                        prime_status = False
                        break
            else:
                prime_status = False    
            if prime_status:
                primes.append(number)  
        
        end = time.time()
        delta_time = round((end - start), 4 )
        
        #output
        print("\nThis process took ",delta_time,"seconds.")
        prompt = input("\n\tPress enter to continue: ")
        for i in primes:
            print("\t -",i)


    else:
        print("Invalid option!!!")

    prompt2 = input("Would you like to continue(y/n): ").lower()
    if prompt2 != "y":
        active = False 
        print("Okay, bye.")







                            




               



 