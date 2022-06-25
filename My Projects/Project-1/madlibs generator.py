from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
root.configure(bg="grey")
Label(root, text= 'Mad Libs Generator', anchor = "center", font = 'arial 20 bold').grid(row = 0, column = 0)
Label(root, text = 'Choose one:', justify = "center", font = 'Helvetica 15 italic').grid(row = 1, column = 0)
def madlib1():
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    noun4 = input("Enter a noun: ")
    noun5 = input("Enter a noun: ")
    noun6 = input("Enter any plural noun: ")
    profession = input("Enter any profession: ")
    verb2 = input("Enter a verb ending in 'ed': ")
    verb1 = input("Enter a verb: ")
    verb3 = input("Enter a verb ending in 'ing': ")
    place = input("Enter a location: ")
    emotion = input("Enter your feeling: ")
    
    template1 = [noun1, noun2, noun3, profession, verb1, place, place, verb2, noun4, verb3, noun5, place, emotion]
    print("It was during the battle of {} when I was running through a {} when a {} went off right next to my platoon. Our {} yelled for us to {} to the nearest {} we could find. When we got to the {} we {} to start a fire. As we were starting the fire, the enemy saw the {} from the fire and started {} People at us. we all quickly ducked behind the {} at the {} and returned fire. we quickly eliminated the enemy and were {} that we had won the battle.".format(*template1))
    

def madlib2():
    noun1 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    noun4 = input("Enter a noun: ")
    noun2 = input("Enter any plural noun: ")
    adjective = input("Enter any adjective: ")
    place = input("Enter a location: ")
    
    template2 = [noun1, noun2, noun3, noun2, noun4, place, adjective]
    print("Be kind to your {}-footed {}. For a duck may be somebody`s {}, Be kind to your {} in {}. Where the weather is always {}. You may think that this is the {}, Well it is.".format(*template2))
    
    
def madlib3():
    noun1 = input("Enter any plural noun: ")
    place = input("Enter a location: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter any plural noun: ")
    noun4 = input("Enter a noun: ")
    adjective1 = input("Enter any adjective: ")
    verb1 = input("Enter a verb: ")
    number = input("Enter any number: ")
    adjective2 = input("Enter any adjective: ")
    body_part = input("Enter the name of a human organ: ") 
    verb2 = input("Enter a verb: ")
    
    template3 = [noun1, place, noun2, noun3, noun4, adjective1, verb1, number, adjective2, body_part, verb2]
    print("Two {}, both alike in dignity. In fair {}, where we lay our scene. From ancient {} break to new mutiny, where civil blood makes civil hands unclean. From forth the fatal loins of these two foes, a pair of star-cross`d {} take their life; Whole misadventured piteous overthrows. Do with their {} bury their parents` strife. The fearful passage of their {} love, and the continuance of their parents` rage which, but their children`s end, nought could {}. Is now the {} hours` traffic of our stage; The which if you with {} {} attend, what here shall {}, our toil shall strive to mend.".format(*template3))


Button(root, text= 'War', font ='arial 15 bold', command= madlib1, relief=RAISED, anchor = "center", bg = 'blue', foreground="white").grid(row= 5, column= 0 )
Button(root, text= 'Kindness', font ='arial 15 bold', command= madlib2, relief=RAISED, anchor = "center", bg = 'green', foreground="white").grid(row= 6, column= 0 )
Button(root, text= 'Romeo and Juliet', font ='arial 15 bold', command= madlib3, relief=RAISED, anchor = "center", bg = 'red', foreground="white").grid(row= 7, column= 0 )

root.mainloop()