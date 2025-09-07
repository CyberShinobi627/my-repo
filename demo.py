age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif 0 < age < 18:
    print("Not adult")
else:
    print("Adult")
