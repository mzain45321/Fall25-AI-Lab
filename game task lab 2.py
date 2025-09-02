class FizzBuzz:
    def __init__(self, start, end):
    
        self.start = start
        self.end = end
    def play(self):
    
        n = self.start
        while n <= self.end:
            if n % 3 == 0:
                print("Fizz")
                if n % 5 == 0:
                    print("Buzz")
            elif n % 5 == 0:
                print("Buzz")
            else:
                print(n)

            print() 
            n += 1

game = FizzBuzz(1, 15)
game.play()
