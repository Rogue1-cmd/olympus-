#Database Admin program
import time
print("Welcome to the database administration program.")
log_in_info = {"admin00":"IamTheMan","chewbacca":"hidaya96","aurellius":"jabanana22",
              "danjuma":"IamNeo77","proteus":"symbian2","syme":"NorthernLights"}

username = input("Enter username: ")

if username in log_in_info:
    password = input("Enter password: ")
    time.sleep(1)
    if password == log_in_info[username]:
        print("\nHello,", username, ",You're in :)")
        if username == "admin00":
            for key, value in log_in_info.items():
                print("username: ",key, "\tpassword: ", value)  #prints entire dictionary for admin
        else :
            prompt = input("\nWould you like to change your password? (y/n):").title().strip()                    
            if prompt == "Y":  #Prompting users to change password
                new_pass = input("\nEnter new password: ")
                if len(new_pass) >=8: #password should be 8 or more characters
                    log_in_info[username] = [new_pass]
                    time.sleep(1)
                    print("successful!!!","\nusername: ", username, "\tnew password: ", new_pass )
                else:
                    print("\nInvalid. Password should be at least 8 characters long.")    
            else:
                print("Okay, bye :)")  
    else:
        print("Incorrect password!!!")              
else:
    print("User not found!!!")        

                