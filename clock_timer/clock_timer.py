import time
import sys  # Added sys to handle command-line arguments

def clock_timer():
    print("Welcome to the Clock Timer")
    print("Debug: Entering clock_timer function")

    try:
        if len(sys.argv) > 1:  # Check if arguments are passed via the command line
            countdown_time = int(sys.argv[1])
        else:
            countdown_time = int(input("Enter the countdown time in seconds: "))
        
        print(f"Debug: User entered {countdown_time}")
        if countdown_time < 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Timer set for {countdown_time} seconds.\n")

    # Countdown loop
    while countdown_time > 0:
        print(f"Debug: Countdown at {countdown_time}")
        print(countdown_time)
        time.sleep(1)
        countdown_time -= 1

    print("Time's up!")

if __name__ == "__main__":
    print("Debug: Entering main check")
    clock_timer()
