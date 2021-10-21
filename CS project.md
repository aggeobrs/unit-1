**CS PROJECT**

**CRITERION A: PLANNING**

**Problem definition**

The owner of the local game shop is an enthusiast of classic computer games. He has been looking for a talented programmer that can help him revive his passion for text-based games. He has few requirements for this task:

- The game has to be entirely text-based.
- The game must record the time played.
- The game must record the player’s name and score.

Apart from these requirements, the owner is open to any type of game, topic, or genre.


**Proposed solution**

The project I am going to make will be an only text-based program and will look like an escape room game. This game is designed to be played mainly by gamers, but it is easy, friendly, and accessible. Therefore, it can be played by everyone who is willing to play a mini mysterious escape room game for entertainment. So, this game will be made in PyCharm 2021.2 and is constructed using the software Python 3. I chose to use this software since it is popular, friendly to use software, and at the same time has powerful tools. It will take me about 3 weeks to make and will be evaluated according to the criteria:

- The program will give some options to the user like A, B, C or Yes and No, in order to take quick and efficient decisions.
- There will be a time limit, and according to the time spent and the efficiency of the decisions, there will be created a score of the player.

**Plan**

![image](https://user-images.githubusercontent.com/89012983/138294647-750bdd1b-78c5-45da-ab72-155caf08dcd0.png)

**CRITERION B: DESIGNING**

**System diagram**

![SYSTEM DIAGRAM](https://user-images.githubusercontent.com/89012983/138297386-ca6162df-6fb1-4489-bae7-34e1e7366e71.png)

**Figure 1: System diagram of the proposed solution**

As you can see, in Figure 1, we need to buy some 3 to input the information from the keyboard, then we process the info, store them if we need to and then print the outcome (output) on the screen.

**What is the personal relevance of the game? Why did you pick the theme?**

As you know the client wants a text-based game. He is an enthusiast of classic computer games and he has not a lot of requirements. For this reason, there are a lot of things that someone could do. I used my imagination to select a topic that would satisfy first of all the client and then, the consumer. From my own experience, even I am not a big fan of classical games, an escape room-looking game would be ideal for the situation. The concept is familiar for most of the consumers, it is simple as a concept and has the potential to become more complicated to offer the best experience to the user. Moreover, a mysterious game with adventure can satisfy the majority of the users, and since the requirements were not specific, a more well-known concept would be considered a safe option. Finally, about the personal relevance of the game, I mostly enjoy these types of games, especially with the pandemic, that there were restrictions with physical escape rooms.

**FLOW DIAGRAMS**

![First action flaw diagram](https://user-images.githubusercontent.com/89012983/138297572-57202b1e-5a37-45e1-ba83-7deded957981.png)

Figure 2: Flow diagram of the part of the program that asks for the correct code from the user

![Action 1 flaw diagram](https://user-images.githubusercontent.com/89012983/138297690-27afdff7-f228-44ca-87f4-c6ed2269d31f.png)

Figure 3: Flow diagram of the part of the program that asks the user to turn left or right 

![Action 5 flaw diagram](https://user-images.githubusercontent.com/89012983/138297697-2a4656df-6fd7-40ce-ab6f-84bec504ff24.png)

Figure 4: Flow diagram of the part of the program that calls the police to save the user


**TESTING PLAN**

After coding the basic structure of the program, I started coding the program. There were some minor mistakes that were easy to locate and correct. The major issue was the calculation of the score. At the beginning of the code, I inserted the value 0 into the variable score. Then, the value of the score was supposed to be changed in the following functions. Depending on the moves the player would choose, the final score would be different. Although, the value of the score remained 0 because it was saved in the global frame and the changes of the value were inside the functions. To address the problem, I created a smaller and easier version of the specific part of the program, that was enough to try solutions. By searching on the internet and asking the opinion of my professor, I decided to take advantage of the keyword ‘global’. A really useful tool was to visualize execution, in other words, to run the program line by line.  That way, I found the solution for my small program and applied the new information to the actual program. 

```.py
score=0
def A(a):
    score=+a
    print(score)
def B(a):
    score=+a
    A(1000)
def C(a):
    score=+a
    B(100)
C(10)
```

Beginning small program. Expectations: score == 1110, Reality: score == 1000

```.py
score=02
def A(a)  global score
    score=score+a
    print(score)
def B(a)
    global score
    score=score+a
    A(1000)
def C(a):
    global score
    score=+a
    B(100)
C(10)
```

Final small program. Expectations: score == 1110, Reality: score == 1110
