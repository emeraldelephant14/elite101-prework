print("Welcome to the food ordering chatbot")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")
print()

print("Welcome "+name+"! Oh, to be "+str(age)+" again! How can I help you today?")
print()

print("Please choose from the following options: ")
print("1. placeholder response")
print("2. placeholder response")
print("3. placeholder response")
print("4. exit conversation")

print()

user_response = int(input("Enter the number of your choice: "))

if user_response == 4:
    print("Have a great day, "+name+"!")
