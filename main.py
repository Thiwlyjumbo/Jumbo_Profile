state = "waiting"
clarity = False
enegy = 100

while state != "Exit":
    if state == "waiting":
        print("The system is waiting for input.")
        command = input("Enter command (start/exit): ")
        if command == "start":
            state = "active"
        elif command == "exit":
            state = "Exit"
    elif state == "active": 
        print("The system is active.")
        if enegy > 0:
            enegy -= 10
            print(f"Energy level: {enegy}")
            if enegy <= 50 and not clarity:
                clarity = True
                print("Clarity mode activated.")
        else:
            print("Energy depleted. Returning to waiting state.")
            state = "waiting"
            clarity = False