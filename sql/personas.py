import random
import numpy as np

class Person:
    names = ["Olivia", "Liam", "Sophia", "Noah", "Ava", "Jackson", "Mia", "Lucas", "Isabella", "Ethan"]

    def __init__(self):
        self.name = random.choice(self.names)
        self.age = random.randint(18, 50)
        self.skill_level = max(1, min(int(np.random.normal(5, 2)), 10))
        self.winning_count = random.randint(0, 10)

    def add_skill(self, n):
        self.skill_level = max(1, min(self.skill_level + n, 10))

    def add_winning(self):
        self.winning_count += 1

    def play_against(self, opponent):
        skill_diff = abs(self.skill_level - opponent.skill_level)
        probability = 100 if skill_diff > 4 else (75 if skill_diff > 2 else 50)
        winner = self if random.randint(1, 100) < probability else opponent
        winner.add_winning()

def simulate_tournament(people):
    for iteration in range(20):
        print(f"Tournament Round {iteration + 1}")
        for i, player1 in enumerate(people):
            for player2 in people[i + 1:]:
                player1.play_against(player2)

def display_results(people):
    for person in people:
        print(f"{person.name} - Winning Count: {person.winning_count}")

if __name__ == "__main__":
    participants = [Person() for _ in range(10)]

    simulate_tournament(participants)
    display_results(participants)
