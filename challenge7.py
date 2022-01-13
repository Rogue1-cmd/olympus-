#something about identifying lists haha

print ("This is the matrix taking me : \n")

num_strings = ["35", "21", "46", "89"]
num_ints = [12, 34, 56, 34]
num_lists = [[1,2,3], [2,3,1], [2,6,8], [6,3,9]]
num_float = [12.3454, 56.00490, 34.0, 54.844]

#string type
type1_a = type(num_strings)
type1_b = type(num_strings[0])
type1_c = (num_strings)

#int type
type2_a = type(num_ints)
type2_b = type(num_ints[0])
type2_c = (num_ints)

#float type
type3_a = type(num_float)
type3_b = type(num_float[0])
type3_c = (num_float)

#lists type
type4_a = type(num_lists)
type4_b = type(num_lists)
type4_c = (num_lists)

        
def type_id1 (typ_entifier):    
    if type (user_input) == type1_a :             #Type
        return type1_a
    elif type (user_input) == type2_a:
        return type2_a
    elif type (user_input) == type3_a:
        return type3_a
    elif type (user_input) == type4_a:
        return type4_a
    else :
        return "RobotVoice: 'undeterminate!!! undeterminate!!! undeterminate!!!'"    
            
#First Element 
def type_id2(typ_entifier2):     
    if type (user_input) == type1_b:
        return "Element :", type1_b 
    elif type (user_input) == type2_b:
        return "Element : ", type2_b                 
    elif type (user_input) == type3_b:
        return "Element : ", type3_b
    elif type (user_input) == type4_b:      
        return "Element : ", type4_b
    else:
        return "RobotVoice: 'undeterminate!!! undeterminate!!! undeterminate!!!'"    
#Data
def type_id3(typ_entifier3):
    if type (user_input) == type1_c:
        return user_input
    elif type (user_input) == type2_c:
        return user_input
    elif type (user_input) == type3_c:        
        return user_input
    elif type (user_input) == type4_c: 
        return user_input                    
    else :
         return "RobotVoice: 'undeterminate!!! undeterminate!!! undeterminate!!!'" 
             
             
             
user_input = input("C'mon try me ;) \n Enter Here: ")
output1 = type_id1(user_input)  
output2 = type_id2(user_input)
output3 = type_id3(user_input)
print(output1)
print(output2)
print(output3)

         
         
         
         
         
         
         
         
         
         
         
         
                     
                 
                 
                 