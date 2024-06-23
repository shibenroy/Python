import pyttsx3
import speech_recognition as SR
import random
import time
from googlesearch import search
import requests
from bs4 import BeautifulSoup

print("Process initiated ...")
print()


# List of riddles
riddles_with_answers = [
    ("What has keys but can't open locks? A piano!", "A piano!"),
    ("What can travel around the world while staying in a corner? A stamp!", "A stamp!"),
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? An echo!", "An echo!"),
    ("What belongs to you but is used more by others? Your name!", "Your name!"),
    ("The more you take, the more you leave behind. What am I? Footsteps!", "Footsteps!"),
    
]

# Audio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def say(text):
    print(text)
    speak(text)

# Function to get the meaning of a name from Google
def get_name_meaning(name):
    query = f"meaning of the name {name}"
    url = None
    for result in search(query, num=1):
        url = result
        break  # Only take the first result
    
    if not url:
        return None

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract the meaning from the webpage (this part might need to be customized based on the actual page structure)
    meaning_div = soup.find('div', class_='BNeawe')
    if meaning_div:
        return meaning_div.text
    return "Sorry, I could not find the meaning of your name."

# Rock Paper Scissor
def rockpaperscissor():
    while True:
        continue1 = ''
        say("Please enter [R]ock or [P]aper or [S]cissor")
        userinput = input('User Input : ').capitalize()
        mylist = ['R', 'P', 'S']

        if userinput not in mylist:
            say('Incorrect Input, Please enter [R]ock or [P]aper or [S]cissor...')
        else:
            comp_input = random.choice(mylist)
            say(f"user input is {userinput} and Computer input is {comp_input}")

            # Determine winner
            if userinput == 'P' and comp_input == 'R' or \
               userinput == 'R' and comp_input == 'S' or \
               userinput == 'S' and comp_input == 'P':
                say('User Win!!!')
            elif userinput == comp_input:
                say('Draw!!!')
            else:
                say('Computer Wins!!!')

        say('To Continue Type - C - And to Quit Type - Q - ...')

        while continue1 != 'Q' and continue1 != 'C':
            continue1 = input().capitalize()
            if continue1 == 'Q':
                say('To See More options Please Rerun The Program')
                exit()
            elif continue1 == 'C':
                break

# Starting the process .................................
say("Hi, I am Fun Bot!")
say('Please, Enter your name')

Name1 = input('Name?: ')
Name1 = Name1.capitalize()
say('Welcome, ' + Name1)
time.sleep(0.5)

while True:
    say('I can do many things')
    say(' 1. Do you know what is the meaning of your Name ?')
    say(' 2. Play a game, Rock Paper Scissor *')
    say(' 3. Funny Riddle *')
    say(' 4. Birthday Poem for you *')
    ask1 = input('Input Your Choice (1 / 2 / 3 / 4) : ')

    if ask1 == '3':
        say('Sure! Here is a random riddle for you:')
        random_riddle, answer = random.choice(riddles_with_answers)
        say(random_riddle)
        say('...')
        time.sleep(3)  # Wait for 3 seconds before revealing the answer
        say(f"The answer is: {answer}")     

    elif ask1 == '2':
        rockpaperscissor()

    elif ask1 == '4':
        poem = [
            'Happy Birthday to my very best friend.',
            'Your special day has come by again.',
            'We had so much fun last time around.',
            'Each year June 7th is a wonderful day',
            'As we June Seventh in our own fun way.',
            'Just hanging around and laughing a lot',
            'It is truly amazing what we have got.'
        ]
        for line in poem:
            say(line)
            time.sleep(1)

    elif ask1 == '1':
        meaning = get_name_meaning(Name1)
        if meaning:
            say(f'The meaning of your name, {Name1}, is {meaning}')
        else:
            say('Sorry, I could not find the meaning of your name.')

    say('To Continue Type - C - And to Quit Type - Q - ...')
    
    myask2 = ''
    while myask2 != 'q' and myask2 != 'c':
        myask2 = input().lower()
        if myask2 == 'q':
            say("Good Bye Sreejon!, Enjoy your Birthday.")
            say('App ShuttingDown!')
            time.sleep(1)
            exit()
        elif myask2 == 'c':
            break
