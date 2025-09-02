class MovieBudget:
    def __init__(self):
        self.movies = [
            ("Dangal", 80000000),
            ("Memento", 150000000),
            ("PK", 85000000),
            ("Pushpa", 55000000),
            ("Sholay", 30000000),
            ("3 ideots", 215000000),
            ("Jawan", 100000000)
        ]

    def add_movies(self):
        numbers = int(input("How many movies to add: "))
        for i in range(numbers):
            name = input("Enter movie name: ")
            budget = int(input("Enter movie budget: "))
            self.movies.append((name, budget))

    def average_budgets(self):
        total_budget = 0
        for movie in self.movies:
            total_budget += movie[1]
        return total_budget / len(self.movies)

    def find_budget(self, average_budget):
        print("Movies budget higher than average:")
        count = 0
        for movie in self.movies:
            name, budget = movie
            if budget > average_budget:
                print(f"{name} — higher by {budget - average_budget}")
                count += 1
        print("Total movies with budget higher than average:", count)

total = MovieBudget()
total.add_movies()

average = total.average_budgets()
print("Average Budget:", average)

total.find_budget(average)