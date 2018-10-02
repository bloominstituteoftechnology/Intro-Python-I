# Implement a class to hold room information. This should have name and
# description attributes.

# applicant = input("Enter the applicant's name: ")
# interviewer = input("Enter the interviewer's name: ")
# time = input("Enter the appointment time: ")
# print(interviewer, "will interview", applicant, "at", time)

class Room():
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
    def __str__(self):
        return f"\n{self.name}\n{self.wins} - {self.losses} - {self.ties}\n"
    def addResult(self, result):
        if result == 1:
            self.wins += 1
        elif result == 0:
            self.ties += 1
        elif result == -1:
            self.losses += 1