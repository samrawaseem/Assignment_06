class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger closed: Object destroyed.")

# Creating an object
log = Logger()

# Deleting the object manually to see destructor message
del log
# The destructor will be called automatically when the object goes out of scope
# or when the program ends, but we can also call it explicitly.