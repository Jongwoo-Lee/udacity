# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/



#QUIZ 1 (http://www.elcivics.com/lifeskills/breakfast.pdf)

sample1 = '''Jack is a bachelor. He works in downtown Chicago as a shoe salesman. Every morning on his way
    to ___1___, Jack stops at a donut shop and buys a chocolate donut and a ___2___ of coffee. Jack likes this morning
    routine because it is quick and easy. He doesn’t have to cook breakfast or ___3___ the dishes.'''

answer1 = ["work", "cup", "wash"]


#QUIZ 2

sample2 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answer2 = ["function", "parameters", "None", "lists"]


#QUIZ 3 (LOVE RINGS TWICE by Bill Loguidice, http://www.armchairarcade.com/neo/node/1173)

sample3 = '''Theirs was a true ___1___, thought Tony, one to stand the test of time. Eva, his soul-mate, was
somehow even more beautiful than the day they first met, he realized. And even though she always seemed to
say something ___2___, it ultimately didn't matter, as he was happy just to hear her soft, melodic ___3___.
Someday soon, he imagined, they would have children together, and their ___1___ would blossom as a family.
These wonderful thoughts made him feel ___4___ and tingly inside. Suddenly, without warning, Tony was yanked
from his ___5___ by the doorbell. He let out a long sigh, realizing that that would be the courier with the
divorce papers.'''

answer3 = ["love", "interesting", "voice", "warm" ,"daydream"]




# To make a list of quiz blanks more easily. Enter number of blanks in the quiz.
def createQuizNumber(a):
    number_list = []
    for i in range(1,a+1):
        number_list.append("___"+str(i)+"___")
    return number_list

# Checks if a word in parts_of_speech is a substring of the word passed in.

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# The main function of the quiz. Checks each blank, and receives answers.
# If the answer is correct, prints the whole line with blanks filled with answers
# ml_string is the quiz, and ans is the list of answers.


def fill_blanks(ml_string, ans):
    replaced = []
    count = 0
    num_quiz = createQuizNumber(len(ans))

    print(ml_string)
    print(num_quiz)
    
    ml_split = ml_string.split() #Assigned new list, so I can use ml_string to print while quiz is in progress
    
    for word in ml_split:
        
        replacement = word_in_pos(word,num_quiz)
        
        if replacement != None:

            user_input = None            
            while user_input != ans[count]:
                user_input = raw_input("What should go in " + replacement + ": ")
            print("Correct!")

            del num_quiz[0] #The corrected num_quiz is deleted
            
            ml_string = ml_string.replace(replacement, user_input)
            print ml_string
            
            count += 1
            
    return ml_string
                
def choose_level():
    a = raw_input("Choose level (1,2,3) or (easy, medium, hard) :")
    if a == '1' or a == "easy":
        fill_blanks(sample1,answer1)
        return
    elif a == '2' or a == "medium":
        fill_blanks(sample2,answer2)
        return
    elif a == '3' or a == "hard":
        fill_blanks(sample3,answer3)
        return
    choose_level()
     
        

choose_level()







            
