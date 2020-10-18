"""
This is a programm for a chat bot.......
My bot will first introduce what it will do.
After it will ask the users name.And greet the user.
It will display its futures to select the user which information they want.
This chatbot contains two futures 
1.Perform some calculations.
2.Give some details about the inventors of some languages.
It will ask to select one future and it will execute that future and display the output to the user.
"""
import random
from datetime import datetime

def greet_and_intro():
    # Introduce the use about the bot.
    responses=[
        "Hi There! I am a bot i have two futures programming language developer details and calculations.May i know your name please ?",
        "Wounderful, It is so nice to be in touch with you.I am a bot which have two special futures programming language developer details and calculations.Can i know your name please?. ",
        "Hi darling! I am a bot which have two special futures programming language developer details and calculations.Can i get your name?"
    ]
    # Pick randome responses.
    print(random.choice(responses))

def get_date_time():
    # To get the date and time.
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour <= 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour > 17 and current_time.hour <= 22:
        timeofday_greeting = "Good Evening"
    elif current_time.hour >= 22:
        timeofday_greeting = "Hi,Thats late"
    return timeofday_greeting 

def welcome(name):
    # Welcome wishes to the user.
    message=[
        "Nice to meet you ",
        "Very good to have a coversation with you ",
        "Very happy to meet you ",
        "Nice to have conversation with you "
    ]
    print(f"{get_date_time()} {random.choice(message)}{name}")

def bot_details():
    # Details of the bot to know the user which futures bot contains. 
    print("1.calcy")
    print("2.developers")
    print("3.end")
    try:
        return input("Enter the name to get that bot details :")
    except:
        print("Not able to provide information.")
        return 0

def evaluate_exp():
    #To execute the mathematical operation.
    expr=input("Enter an expression ")
    try:
        print("Result = ",eval(expr))#eval built in function.
    except Exception as e:
        print(str(e))

def inventors_list():
    # List of the languages which this dvelopers bot explain.
    print("This is the list of languages about what we have an information :")
    print("1.C")
    print("2.C++")
    print("3.Python")
    print("4.Java")
    print("5.Java Script")
    print("6.To stop conversation.")
    print("-----------------------")
    try:
        return int(input("Enter your choice[1-6] : "))
    except:
        print("Only enter choice from 1 to 6 ")
        return 0
def bot():
    greet_and_intro()
    name = input("Your Name : ")
    welcome(name)
    boti = bot_details()
    while(boti != "end"):
        if(boti == "calcy"):
            # To execute the calculations.
            evaluate_exp()
            boti=bot_details()
        if(boti == "developers"):
            #To execute developers details.
            print("Enter the number of the language .To get information about the developer of that language.")
            choice=inventors_list()
            while choice != 6:
                if choice ==1:
                    print("The language C is introduced by 'DENNIS RITCHIE'")
                    print("He was born on September 8th, 1941 in Bronxville, New York.")
                    print("He introduced C language in the year : 1972.")
                    print("-----------------------")
                elif choice ==2:
                    print("The language C++ is introduced by 'BJARNE STROUSTRUP'")
                    print("He was born on 1950 in Aarhus, Denmark.")
                    print("He introduced C++ language in the year : 1998.")
                    print("-----------------------")
                elif choice ==3:
                    print("The language Python is intoduced by 'GUIDO VAN ROSSUM'")
                    print("He was born on 31 January 1956 in Netherlands.")
                    print("He introduced Python language in the year : 1991.")
                    print("-----------------------")
                elif choice ==4:
                    print("The language Java is intoduced by 'JAMES ARTHUR COSLING'")
                    print("He was born on 1956 near Calgary, Alberta.")
                    print("He introduced Java language in the year : 1996.")
                    print("-----------------------")
                elif choice ==5:
                    print("The language Java is intoduced by 'Brendan Eich'")
                    print("He was born on July 4, 1961 Pittsburgh, Pennsylvania, U.S.")
                    print("He introduced Java language in the year : 1995.")
                    print("-----------------------")
                else:
                    print("I don't understand that")
                    print("-----------------------")
                choice=inventors_list()
        else:
            print("Sorry unable aceppt your request.")
        boti = bot_details()

bot()