class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 2  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Creating objects
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Display object count using class method
Counter.display_count()
