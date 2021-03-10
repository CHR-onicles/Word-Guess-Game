import time

from tkinter import *
from random import choice, sample
from words import words





# from Tk_module import *


# Main Window
root = Tk()
root.title("KP | Guess Game")
root.geometry("400x500")

# global variables
timer = None
entry_1 = None
word = None
declare = None
is_replay_clicked = False
timer_id = None


# Generates the random word from the list if words
def rand_word():
    word = choice(words)
    return word  # rand_word


# Jumbles up the random word.
# Pass in the value from rand_word()
def jumbled_word(rw):
    """Returns a jumbled-up word"""
    return sample(rw, len(rw))


# The Exit button || Quits the program when user presses button
def exit_btn():
    root.quit()


def replay():
    global is_replay_clicked
    is_replay_clicked = True
    main()
    return


# Submits the user input || verifies whether or not it is correct
def sub_btn():
    global timer, declare, entry_1
    timer.pack_forget()
    user_guess = entry_1.get()
    if user_guess == word:
        declare.config(text=f"Correct!\nCorrect Word: {word} ")
    elif user_guess in words:
        declare.config(text=f"Correct!\nCorrect Word: {user_guess} ")
    else:
        declare.config(text=f"Wrong!\nCorrect Word: {word} ")


# Count down timer || Limits the duration a user has to guess the word
def count_down(secs):
    global declare, timer, timer_id
    # timer["text"] = secs
    if secs >= 0:
        if is_replay_clicked is True:
            root.after_cancel(timer_id)
        timer.config(text=str(secs))
        timer_id = root.after(1000, count_down, secs - 1)
        # print(timer_id)
        if secs == 0:
            declare.config(text=f"Time Up!\nCorrect word is: {word}  ")


def main():
    global timer, word, declare, entry_1, is_replay_clicked, timer_id

    info = "What is the correct version of the word below?"

    # Preamble
    preamble = Label(root, text=info, font=("Sans", 14))
    preamble.place(y=8)

    # while replay_game:
    # Frame for jumbled word and timer
    frame_timer = Frame(root, width=380, height=25, relief='sunken', borderwidth=5)
    frame_timer.place(x=280, y=50)

    # Declaration || Correct or Wrong
    declare = Label(root, text="Welcome!\nGood Luck Playing", width=28, height=5, font=("Sans", 15), bg="blue",
                    fg="#fff")
    declare.place(x=49, y=180)

    timer = Label(frame_timer, text="00", width=4, font=("Helvetica", 20), bg="blue", fg="#fff")
    timer.pack()
    count_down(20)

    # Frame for jumbled word
    frame_jw = Frame(root, width=80, height=25, relief='sunken', borderwidth=5)
    frame_jw.place(x=50, y=50)

    word = rand_word()
    jumbo = jumbled_word(word)
    jumbled_word_label = Label(frame_jw, text=jumbo, width=12, font=("Arial", 20), bg="blue", fg="#fff")
    jumbled_word_label.pack(side=LEFT)

    # Entry box
    entry_1 = Entry(root, width=22, font=("Helvetica", 19))
    entry_1.place(x=49, y=110)

    is_replay_clicked = False





# Frame {Container} for the 3 buttons || Exit, Submit and Replay
frame_btns = Frame(root, width=360, bg="blue")
frame_btns.place(x=23, y=430)
# Exit button
exit_btn = Button(frame_btns, text="Exit", width=9, font=("Verdana", 14), bg="blue", fg="#fff", command=exit_btn)
exit_btn.pack(side=LEFT)
# Submit button
sub_btn = Button(frame_btns, text="Submit", width=9, font=("Verdana", 14), bg="blue", fg="#fff", comman=sub_btn)
sub_btn.pack(side=LEFT)
# Replay button
rep_btn = Button(frame_btns, text="Replay", width=9, font=("Verdana", 14), bg="blue", fg="#fff", command=replay)
rep_btn.pack(side=RIGHT)

if __name__ == '__main__':
    main()
    root.mainloop()
