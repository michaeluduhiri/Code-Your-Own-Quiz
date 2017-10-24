#Difficulty level options
level_options = ["easy", "medium", "hard"]

#Blank fields
fill_in_blanks = ["__1__", "__2__", "__3__", "__4__"]



#Question to display at end of paragraph prompting user input
eop_question = ["""What should be substituted for __1__ """, """What should be substituted for __2__ """,
                """What should be substituted for __3__ """, """What should be substituted for __4__ """]

#Array to temporarily store quiz answers
temp_answers = []


#Encouragement for right answers and try again for wrong answers
right_answer = "You're correct. Good job!"
wrong_answer = "Sorry, that's incorrect. Please try again"

data =  {
    "easy": "There are __1__ states in the United States of America."
                        "The most populous state is __2__ with over 39 million people living in this west coast state."
                        "The President of the United States lives in the __3__ House located at 1600 Pennsylvania Ave"
                        "and it is located in Washington D.C aka District of __4__.",
    "medium": "These are some fun facts regarding the state of Washington."
                        "The 5 mile long __1__ glacier is the longest in the continental United States."
                        "King county was originally named after __2__ before it was renamed in 1986 after Dr. Martin Luther King Jr."
                        "The highest point in Washington is Mount Rainer named after the British Soldier __3__. Washington's state insect is the __4__ .",
    "hard": "The state of Washington is located in the Pacific Northwest"
                        "among other states such as Oregon, Idaho and also close to British Columbia."
                        "Washington is the __1__ largest state with an area of under 72,000 square miles."
                        "Washington was granted statehood in the year __2__ and was named"
                        "in honor of George Washington. It is also the only U.S state named after a president."
                        "Washington, also known as The Evergreen state, attracted Europeans"
                        "to its region in the 18th century. The Spanish explorer, __3__, visited"
                        "in the 1700's and claimed it for his country however,"
                        "the British were also interested in the region which was leading to a potential"
                        "clash between the 2 countries. In order to avert a war between these 2 countries,"
                        "the __4__ were agreements put in place to resolve overlapping claims"
                        "by the Kingdom of Spain and the Kingdom of Britain." ,
    }


quiz_answers = {"easy":["50", "California", "White", "Columbia"],
                "medium":["Emmons", "William R. King", "Peter Rainier", "Green Darner Dragonfly"],
                "hard":["18th", "1889", "Bruno Heceta", "Nootka Sound Conventions"]}

#Get the difficulty level from the raw input and return the corresponding quiz
def get_level():
    """ Behavior: Ask the user to enter one of the following 3 levels: easy, medium or hard
        Input: Quiz type
        Output: Run the quiz"""
    level = raw_input ("Please enter one of the 3 difficulty levels: easy, medium or hard ")
    wrong_level = "Sorry! That's not an option. Please enter one of these options: easy, medium or hard "
    while level not in level_options:
        print wrong_level
        return get_level()
    if level.lower() == "easy" or level.lower() == "medium" or level.lower() == "hard":
        return run_quiz(level,0)
    

def run_quiz(level, answer):
    """Behavior:Show quiz text and ask for user input at the end of each paragraph. If user response
        is correct, run the right function. If all answers are correct, congratulate the user.
        If answers are wrong, run the wrong function.
        are correct, congratulate the user.
        Input: Answers to quiz
        Output: """
    #for question in eop_question:
    print data[level]
    if answer == len(quiz_answers[level]):
        return congratulations()
    temp_answers.append(raw_input(eop_question[answer]))
    if temp_answers[answer] == quiz_answers[level][answer]:
        return right(answer, level)
    else:
        return wrong(level, answer)
        
      
  
def right(answer, level):
    """Behavior: If the user response is correct, print the right answer and replace the blank field in quiz with the answer from the array
    Input: N/A
    Output: Correct answer with quiz
    """
    print right_answer
    data[level] = data[level].replace(fill_in_blanks[answer], temp_answers[answer])
    return run_quiz(level, answer + 1)

def wrong(level, answer):
     """Behavior: If the user response is incorrect, pop the answer from the temporary array,
        redisplay the quiz and prompt user for correct response
        Input: N/A
        Output: Wrong answer text with the quiz
    """
    print wrong_answer + temp_answers.pop()
    return run_quiz(level, answer)

def congratulations():
    print "Congratulations"



print get_level()
