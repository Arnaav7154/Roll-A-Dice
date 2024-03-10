import random
user = input("Would you like to roll the the dice(y/n):").lower()
dice_value=random.randint(1,6)
while True:
    if(dice_value==1 and user=='y'):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        break
    elif(dice_value==2 and   user=='y'):
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
        break
    elif(dice_value==3 and user=='y'):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        break
    elif(dice_value==4 and user=='y'):    
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]") 
        break
    elif(dice_value==5 and user=='y'):    
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]") 
        break
    elif(dice_value==6 and user=='y'):    
        print("[-----]")
        print("[0   0]")
        print("[0   0y]")
        print("[0   0]")
        print("[-----]")
        break
    else:
        print("Thanks") 
        break    