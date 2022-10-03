import random
i=10
while(True):
    temp=random.randint(1,100)
    humi=random.randint(1,100)
    print("Temperature :",temp,"  Humidity :",humi)
    if(temp>25 and humi<40):
        print("High Temperature!!!  ALARM ON...")
        print("")
    else:
        print("Low Temperature      ALARM OFF...")
        print("")
    i-=1