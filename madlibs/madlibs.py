def madlib():
    adj1 = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous person: ")

    madlib = f"Computer programming is so {adj1}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    
    print(madlib)
    
if __name__ == '__main__':
    madlib()
    
# you could have a collection of python files like this one above in a folder, then make a script that imports all the madlib files and imports random,
# then using random.choice you could pick a madlib at random and run it from the script. don't forget to run the function madlib() on the random choiced madlib.
# e.g. randomly_chosen_madlib.madlib()