class guess:
    def showMenu(self):
        x = "----"
        while("-" in x):
            print(x)
            x = "a"
            print("g = guess, t = tell me, l for a letter, and q to quit")
            c = raw_input()
            if (c == "q"):
                break

        return c


gss = guess()
print("** The great guessing game **")
print("Current Guess: ----")
print("g = guess, t = tell me, l for a letter, and q to quit")
c = raw_input()
while(c != "q"):
    c = gss.showMenu()
