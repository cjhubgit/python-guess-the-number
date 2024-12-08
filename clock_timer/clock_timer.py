import time
import sys  

def clock_timer():
    print("Welcome to the Clock Timer")
    print("Debug: Entering clock_timer function")

    try:
        
        if len(sys.argv) > 1:
            countdown_time = int(sys.argv[1])
        else:
            print("Error: Countdown time not provided. Please run as 'python clock_timer.py <seconds>'")
            return
        
        print(f"Debug: User entered {countdown_time}")
        if countdown_time < 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Timer set for {countdown_time} seconds.\n")

    
    while countdown_time > 0:
        print(f"Debug: Countdown at {countdown_time}")
        print(countdown_time)
        time.sleep(1)
        countdown_time -= 1

    print("Time's up!")

if __name__ == "__main__":
    print("Debug: Entering main check")
    clock_timer()
