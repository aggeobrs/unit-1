number=1
time=0
score=0
import time
start = time.time()
def action5():
    global score
    print("Do you see the sign there? It writes 'Robert 44'. This might be the address. Now, check your phone. Yeah, the signal is working. Call the police! ")
    ans=int(input("Press the correct digits: "))
    while ans!=911:
        ans=int(input("Press the correct digits: "))
    else:
        print("It is calling...")
        print("Hello, you called 911. Is there an emergency?")
        ans=input("Press 'Y' for yes and 'N' for no: ")
    if ans=='N':
        print("Ok, then. Have a nice day!")
    else:
        print("What is your adress? ")
        ans=input("Print your adress: ")
        print("OK! We will be there in 3 minutes. Bye! ")
        print("Hey, "+name+"! Do you have enough time? Check the time.")
        ans=input("Press C to see the time: ")
        while ans!='C':
            ans = input("Press C to see the time: ")
        else:
            import time
            end = time.time()
            time = round(end - start)
            if time<4*60:
                score=score+4*60-time
                print("Yeah! Congratlation "+str(name)+"!!! You will survive!")
                print(name+", your score is "+ str(score) +" and the time is "+ str(time) + " seconds!")
            else:
                print("Oh no... The time is not enough! Unfortunately, you will not survive :( ...")
def action4(a):
    global score
    score = score + a
    print(name+", wow! You are out of the house! Do you have the smartphone?")
    ans=input("Press 'Y' for yes and 'N' for no: ")
    if ans=='Y':
        action5()
    else:
        print("No? Run back to the house and go left to your room!")
        action2b(0)
def action2(a):
    global score
    score=score+a
    print("Look on the table. There is a smartphone on there. Take it. It may be useful. ")
    ans=input("Press 'T' to open it: ")
    print("Oh! The smartphone is working, but the signal does not. Let's go outside to see if it works.")
    action3()
def action2b(a):
    global score
    score=score+a
    print("Look on the table. There is a smartphone on there. Take it. It may be useful. ")
    ans=input("Press 'T' to open it: ")
    print("Oh! The smartphone is working, but the signal does not. Let's go outside to see if it works.")
    action5()
def action3():
    code2=7259
    print("There is a door with another code. This is a 4 digit code. It seems like you are stuck here for ever... But wait! If you see closely, the key digits 2, 5, 7 and 9 are faded out. You just have to find the correct combination! ")
    try1 = int(input("Insert the code: "))
    if try1!=code2:
        print("I will give you a clue. The first digit is 7")
        try1 = int(input("Insert the code: "))
        if try1!=code2:
            try1 = int(input("Insert the code: "))
            if try1!=code2:
                try1 = int(input("Insert the code: "))
                if try1!=code2:
                    try1 = int(input("Insert the code: "))
                    if try1!=code2:
                        try1 = int(input("Insert the code: "))
                        if try1!=code2:
                            try1 = int(input("Insert the code: "))
                            action4(10)
                        else:
                            action4(20)
                    else:
                        action4(30)
                else:
                    action4(50)
            else:
                action4(70)
        else:
            action4(100)
    else:
        action4(200)
def answer():
      ans="Press 'Y' for yes and 'N' for no: "
      return (ans)
def action1(a):
      global score
      score=score+a
      print("Congrats, "+name+" ! The door is open. Go ahead! Now we are in the central hall. Would you like to move Left or right?")
      ans=input("Press 'R' for right and 'L' for left: ")
      if ans=='R':
          action3()
      else:
          action2(30)
print("Listen carefully!")
print("You may not remember how you ended up here, but now as you can see, you are trapped alone in an abandoned place!")
print("Creepy, isn't it? But you can do things to survive and escape. You see the clock up there? No? "
      "The time now is " + str(time) + "."
      "The time is really important, because the man that locked you up will be here in 7 minutes. So you have to HURRY UP!")
ans=input("Do you want to escape player number " + str(number) + "? Press 'Y' for yes and 'N' for no: ")
if ans=="N":
    print("Sorry to hear that! Good luck in your rest of your life...")
    quit()
else:
      code1=number
      print("But you don't want me to call you player number " + str(number) + ", right? What is your real name?")
      name=input()
      print("Perfect. Let's start! "
            "Go closer to the door. Do you see the locker? It is a 3 digit code. What could it be?")
      try1=int(input("Insert the code: "))
      if try1!=number:
            print("Think of something more personal. Try again!")
            try1 = int(input("Insert the code: "))
            if try1 != number:
                  print("Think of the information you know. You can do it!")
                  try1 = int(input("Insert the code: "))
                  if try1 != number:
                        print("What about your player's number. Do you remember it?")
                        ans=input("Press 'Y' for yes and 'N' for no: ")
                        if ans=='Y':
                              try1 = int(input("Insert the code: "))
                              action1(10)
                        else:
                              print("Your player's number is "+ str(number))
                              try1 = int(input("Insert the code: "))
                              action1(0)
                  else:
                        action1(20)
            else:
                  action1(30)
      else:
            action1(50)
