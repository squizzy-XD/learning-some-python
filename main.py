# if = Only do IF condition is true
#       else = do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("die lol")
else:
    print("You are not old enough to sign up!")