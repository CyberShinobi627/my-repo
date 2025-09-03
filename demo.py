age = int(input("Enter your age: "))

if age < 0:
    print("invalid age")
elif 0 < age < 18:
    print("not adult")
else:
    print("adult")
