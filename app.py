# app.py
import datetime

def main():
    """Prints a simple message and the current time."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from the basic Python application!")
    print(f"The current UTC time is: {current_time}")
    

if __name__ == "__main__":
    main()