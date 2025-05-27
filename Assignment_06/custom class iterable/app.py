class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End iteration when below zero
        else:
            val = self.current
            self.current -= 1
            return val

# Usage example:
for number in Countdown(5):
    print(number)