print("We Need help");
print("start - to start the car")
print("stop - to stop the car")
print("quit -to exit");

while True:
    userInput=input(">\n");
    if userInput.upper()=="START":
        print("Car is start Lets go");
    elif userInput.upper()=="STOP":
        print("car is stopped");
    elif userInput.upper()=="QUIT":
        break;
    else:
        print("Sorry I cant undertsand")





