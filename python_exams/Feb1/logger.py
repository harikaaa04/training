"""
Create a class `Logger` with a method `log(message)`. 
Implement method overloading to log different message types (`error`, `warning`, `info`).
"""

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        if message == "error":
            print("Log: ERROR")
            self.logs.append("ERROR")
        elif message == "warning":
            print("Log: WARNING")
            self.logs.append("WARNING")
        elif message == "info":
            print("Log: INFO")
            self.logs.append("INFO")
        else:
            print("Log: Unknown")
            self.logs.append("Unknown")


def main():
    logger = Logger()
    while True:
        msg = input("Enter the log (enter 'exit' to exit): ")
        if msg == 'exit':
            break
        logger.log(msg)
    print(f"The logs are: {logger.logs}")

main()