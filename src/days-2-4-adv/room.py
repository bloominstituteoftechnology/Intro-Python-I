# Implement a class to hold room information. This should have name and
# description attributes.

# applicant = input("Enter the applicant's name: ")
# interviewer = input("Enter the interviewer's name: ")
# time = input("Enter the appointment time: ")
# print(interviewer, "will interview", applicant, "at", time)


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
