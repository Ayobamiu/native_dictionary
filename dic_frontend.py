from tkinter import *
import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\Ayobamiu\PycharmProjects\Training\data.json"))

window = Tk(screenName="Dictionary", baseName="usman")

search_text = StringVar()
e1 = Entry(window, textvariable=search_text)
e1.grid(row=0, column=1)


def meaning():
    word = search_text.get()
    close_matches = get_close_matches(word, data, 5, cutoff=0.6)

    if word in data:
        t1.delete(1.0, END)
        t1.insert(END, f" {word.capitalize()}: \n")
        for i in data[word]:
            t1.insert(END, f" {data[word].index(i) + 1}: {i} \n")

    elif len(close_matches) > 0:
        t1.delete(1.0, END)
        t1.insert(END, f"Do you mean {close_matches[0]}?\n")
        for i in data[close_matches[0]]:
            t1.insert(END, f" {data[close_matches[0]].index(i) + 1}: {i} \n")
        # t1.insert(END, f"\n Do you mean {close_matches[1]}?\n")
        # for i in data[close_matches[1]]:
        #     t1.insert(END, f" {data[close_matches[1]].index(i) + 1}: {i} \n")

        # answer = input(f"Do you mean {get_close_matches(word, data, 5, cutoff=0.6)[0]}? \n Press Y/N > ").lower()
        #
        # if answer == 'y':
        #     print(f"{get_close_matches(word, data, 5, cutoff=0.6)[0]}:")
        #     for i in data[get_close_matches(word, data, 5, cutoff=0.6)[0]]:
        #         return (f"-- {i}")
        # elif answer == 'n':
        #     print("Word does not exist")
        #
        # else:
        #     while answer != 'y' or answer != 'n':
        #         ynn = input("Please enter Y/N>> ")
        #         if ynn == 'y':
        #             print(f"{get_close_matches(word, data, 5, cutoff=0.6)[0]}:")
        #             for i in data[get_close_matches(word, data, 5, cutoff=0.6)[0]]:
        #                 print(f"-- {i}")
        #             break
        #         elif ynn == 'n':
        #             print("Word does not exist")
        #             break
        #


b1 = Button(window, text="search", command=meaning)
b1.grid(row=0, column=0)

t1 = Text(window)
t1.grid(row=0, column=2)

window.wm_title("Dictionary")

window.mainloop()
