import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("I am Sheeben's CHAT BOT, please input a Sentence to Continue.")

mystr = input('Please input Sentence :')

def point6():

    for i in mystr:
        if i==' ':
            print('*')
        else:
            print(i)

while(True):

    print("What Do You Want?")
    print(' 1.Lenght')
    print(' 2.Count of Word')
    print(' 3.Split by Word')
    print(' 4.LowerCase')
    print(' 5.UpperCase')
    print(' 6.Replace Space By *')
    print(' 7. All Word Frist Letter Capital')  
    print()
    speak(" -- Please select your choice. You have 7 options. --")

    myask = input('Please Enter You Choice  :')
    spl = mystr.split()
    if myask == '1':
        print(len(mystr))
    elif myask == '2':
        print(len(spl))
    elif myask == '3':
        for x in spl:
            print(x)
    elif myask == '4':
        print(mystr.lower())
    elif myask == '5':
        print(mystr.upper())
    elif myask == '6':
        point6()
    elif myask == '7':
        for y in spl:
            z = y.capitalize()
            print(z,end=" ")


    else:
        speak("Incorrect input provied. Please select options between 1 to 7 only.")
        print("incorrect input")

    myask2 = ""

    speak("To continue press c and to quit press q..")
    print('To continue press c and to quit press q  :')
    
    while (myask2 != 'q' and myask2 !='c'):
        myask2 = input()
        if myask2 == 'q':
            speak("Good Bye! Have a good day.")
            exit()
        elif myask2 == 'c':
            continue




