from time import *
import random as r

def check(paratest,usertest):
    error =0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error= error+1
        except:
            error= error+1
    return error
            
def speed_time(time_S,time_e,userinput):
    time_delay = time_e - time_S
    tiem_r = round(time_delay,2)
    speed = len(userinput)/tiem_r
    return round(speed)



test = ["You have an ongoing Java Spring Boot challenge on LinkedIn", "where you focus on various Spring Boot topics weekly",
        " Currently, you are in week 12, focusing on Config Server and Exception Handling in REST API."  ]

test1 = r.choice(test)
print("************ Typeing Test***************")
print()
print(test1) 
time_1 = time()
user_iput = input("Type above text:  ")
time_2 = time()
print("speed", speed_time(time_1,time_2,user_iput))
print('Error', check(test1,user_iput))
