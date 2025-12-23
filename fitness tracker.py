import json
class Workout:
    def __init__(self, date, type, duration, calories):
        self.date = date
        self.type = type
        self.duration = duration
        self.calories = calories
    def __str__(self):
        return(f"Date:{self.date},Type: {self.type},Duration: {self.duration} mins,calories: {self.calories}")
class FitnessTracker:
    def __init__(self):
        self.workouts = []
    def add_workout(self, workout):
        self.workouts.append(workout)
        print("Workout added successfully.")
    def save_data(self, filename="fitness_data.json"):
        with open(filename, 'w') as f:
            json.dump([vars(w) for w in self.workouts],f, indent=4)
        print("Data saved.")
    def load_data(self, filename="fitness_data.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.workouts = [Workout(**w_data) for w_data in data]
                print("Data loaded.")
        except FileNotFoundError:
            print("No previous data found,starting fresh.")
    def view_summary(self):
        total_calories = sum(w.calories for w in self.workouts)
        print(f"Total workout recorded:{len(self.workouts)}")
        print(f"Total calories burned: {total_calories}")
        for workout in self.workouts:
            print(f"*{workout}")
            # main application logic
if __name__ =="__main__":
    tracker=FitnessTracker()
    tracker.load_data()
    while True:
        print("\nPersonal Fitness Tracker Menu:")
        print("1.Add a new workout")
        print("2.View progress summary")
        print("3.Save and exit")
        choice = input("Enter your choice:")
        if choice == '1':
            date = input("Enter date(YYYY-MM-DD):")
            type = input("Enter workout type:")
            duration = int(input("Enter duration in minutes:"))
            calories = int(input("Enter calories burned:"))
            new_workout = Workout(date, type, duration,calories)
            tracker.add_workout(new_workout)
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            tracker.save_data()
            break
        else:
            print("Invalid choice.please try again.")

            




                      
                      
                      
                      


