import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import tkinter as tk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# some predefined chats

greetings = ["hello", "hi", "hey"]
wish = {"morning": "Good morning", "night": "Good night", "care": "You too.", "bye": "Please don't go",
        "date": str(datetime.date.today()), "time": "you can see that on taskbar my dear"}
silly = {"marry": "No, I have a boyfriend", "love": "I love myself", "hate": "lmao, look at your face",
         "children": "Oh,please.", "how": "Currently bug free", "gender": "i have no gender i am god",
         "movie": "Terminator", "Actor": "wall e", "name": "It's God I am Intelligent in short GIAIN"}


def check():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        order = r.recognize_google(audio, language="en-in")
    e2.insert(tk.END, order)
    x = order.split(" ")

    for word in x:
        if word in greetings:
            answer = "hey, my name is , GIAIN , G I A I N, How are you !"
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)
        elif word in wish:
            answer = wish[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)

        elif "play" in x:
            webbrowser.open_new(f'https://www.youtube.com/results?search_query={x[1]}')
        elif "search" in x:
            webbrowser.open_new(f'https://www.google.com/search?q={x[1]}')

        elif "search YouTube" in x:
            webbrowser.open_new(f'https://www.google.com/search?q={x[1]}')
        elif "search Google" in x:
            webbrowser.open_new(f'https://www.google.com/search?q={x[1]}')

        elif word in silly:
            answer = silly[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(tk.END, answer)


        elif "quit" in x:
            root.destroy()


root = tk.Tk()
root.geometry("200x300")
root.title('GIAIN')
root.configure(bg="black")
e1 = tk.Text(root)
e1.place(x=10, y=35, height=50, width=180)
l1 = tk.Label(root, text="Output")
l1.place(x=10, y=5)

e2 = tk.Text(root)
e2.place(x=10, y=150, height=30, width=180)
l2 = tk.Label(root, text="You said")
l2.place(x=10, y=120)
b = tk.Button(root, text="Speak", bg="red", fg="white", command=check)
b.place(x=50, y=200, height=50, width=100)
root.mainloop()
