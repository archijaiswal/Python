import random,sys
#reference constants

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""
swin=0
slose=0
wwin=0
wlose=0
srate=0
wrate=0
while True:
    l=[1,2,3]
    Dict = { 1:FIRST_GOAT, 2:SECOND_GOAT,3:THIRD_GOAT }
    doorwithcar=random.randint(1,3)
    print(ALL_CLOSED)
    while True:
        a=int(input("Enter a door number you think have a car. (1/2/3) "))
        if a in range(1,4):
            break
        elif a==0:
            print("Thanks for playing")
            sys.exit()
        else:
            print("Enter valid input. (1/2/3) ")          
    
     #implementation
    
    if a!=doorwithcar:
        for x in range(1,4):
            if x!= a and x!= doorwithcar:
                print(Dict[x])
    else:
        del l[a-1]
        x= random.choice(l)
        print(Dict[x])
    
    #swap
    swap= input("Do you want to swap your selection? (Y/N) ")
    while(swap.upper()!= 'Y' and swap.upper()!='N'):
        swap = input("Enter Y/N. ")        
    if swap.upper() == 'Y':
        for i in range(1,4):
            if i!=a and i!=x:
                a=i
    
    if a == doorwithcar and swap.upper() == 'Y':
        swin+=1
        srate= round((swin/(swin+slose))*100,1)
        print("Congrats! You won!")
    elif a== doorwithcar and swap.upper()== 'N':
        wwin+=1
        wrate= round((wwin/(wwin+wlose))*100,1)
        print("Congrats! You won!")
    elif a != doorwithcar and swap.upper() == 'N':
        wlose+=1
        print("Better luck next time!")
    elif a != doorwithcar and swap.upper() == 'Y':
        slose+=1
        print("Better luck next time!")
    else :
        print("Error")

    print("""

    Thanks for playing!

    Wins after swapping: {}
    Wins without swapping: {}
    Losses after swapping:  {}
    Losses without swapping: {}  

    Success rate if you swap: {}
    Success rate if you don't swap: {}
    
    """.format(swin,wwin,slose,wlose,srate,wrate))
