#Binary Hexadecimal Conversion App
import time
print("Welcome to the binary hexadecimal conversion app.")
user_input = int (input("Enter the value you wish to convert: \n"))
print("generating lists...") 
time.sleep(1)
print("complete!")
decimal_values = list(range(1, user_input+1))
hex_values = []
bin_values = []
for x in decimal_values:
    
    bin_values.append(bin(x))
    hex_values.append(hex(x))



print("I will show you a range of values from each list")    
user_input2 = int(input("Enter upper range value: \n"))
user_input3 = int(input("Enter lower range value: \n"))


print("\nDecimal values from ", str(user_input3), " to ", str(user_input2),":")
for x in decimal_values[user_input3-1:user_input2]:
    print(x)


print("\nBinary values from ",str(user_input3), " to ", str(user_input2),":")
for x in bin_values[user_input3-1:user_input2]:
    print(x)

    
print("\nHexadecimal values from ",str(user_input3), " to ", str(user_input2),":")
for x in hex_values[user_input3-1:user_input2]:
    print(x)


input("Press Enter to see all values.")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------")

for d, b, h in zip(decimal_values, bin_values, hex_values):
    print(d,"----", b,"----",h,"----")



