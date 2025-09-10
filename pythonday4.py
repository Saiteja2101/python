import random
#friends = ["Sai","Saketh","Akhil","Bharath","Surya","Vamsi","Abhinav"]
#print(random.choice(friends))
#Person = random.randint(0,6)
#if Person == 0:
    #print("Sai will pay the bill")
#elif Person == 1:
    #print("Saketh will pay the bill")
#elif Person == 2:
    #print("Akhil will pay the bill")  
#elif Person == 3:
    #print("Bharath will pay the bill")  
#elif Person == 4:
    #print("Surya will pay the bill")  
#elif Person == 5:
    #print("Vamsi will pay the bill")  
#elif Person == 6:
    #print("Abhinav will pay the bill")  


#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#dirty_dozen = [fruits, vegetables]
#print(dirty_dozen[1][2])

Person = int(input("WELCOME TO THE ROCK, PAPER and SCISSORS GAME\nPlease type 1 for rock, 2 for paper and 3 for scissors "))
Computer = random.randint(1,3)
#print(f"Computer choose {Computer}")
if Person == 1 and Computer == 1:
    print(f"Computer choose {Computer}")
    print("Its a draw")
elif Person == 1 and Computer == 2:
    print(f"Computer choose {Computer}")
    print("You lost")
elif Person == 1 and Computer == 3:
    print(f"Computer choose {Computer}")
    print("You won")
elif Person == 2 and Computer == 1:
    print(f"Computer choose {Computer}")
    print("You won")
elif Person == 2 and Computer == 2:
    print(f"Computer choose {Computer}")
    print("Its a draw")
elif Person == 2 and Computer == 3:
    print(f"Computer choose {Computer}")
    print("You lost")
elif Person == 3 and Computer == 3:
    print(f"Computer choose {Computer}")
    print("Its a draw")
elif Person == 3 and Computer == 2:
    print(f"Computer choose {Computer}")
    print("You won")
elif Person == 3 and Computer == 1:
    print(f"Computer choose {Computer}")
    print("You lost")
else:
    print("You have type invalid number. so, You lost!")