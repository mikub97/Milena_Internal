name = input("Whats your name?\n")
print("Welcome", name, "!")
age = int(input("How old are you?\n"))

if age>=18:
    print("You are an adult,",name)
    ans = input("Would you like a drink? (y/n)")
    if ans.lower() == "n":  # 'n'->'n'  'N'->'n'
        print("bye bye")
    elif ans.lower() == "y":
        print("here you go..")
    else:
        print("im not sure what you mean..")
else:
    print("You are not adult",name)
    print("byebye")
