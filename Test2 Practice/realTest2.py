# Carson Chadwick 
# Section 04
# Import data from excel about gym members and trainers to set up workout routines.

# Imports
import pandas as pd
import random

# Standard Member Class
class StandardMember ():
    # Constructor
    def __init__(self, name, gender, num_days_member, num_gym_visits, favorite_workout, membership_type):
        self.gender = gender
        self.num_days_member = num_days_member
        self.num_gym_visits = num_gym_visits
        self.favorite_workout = favorite_workout
        self.membership_type = membership_type
        self.name = name
    # recommended_action method based on raio of vists/number_days_member
    def recommended_action(self):
        ratio = self.num_gym_visits/self.num_days_member
        if ratio >= .5:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Keep ut the routine!")
        elif ratio >= .3:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Slightly increase visits.")
        else:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Increase your frequency.")
# Premium Member class inherits from StandardMember but has a trainer     
class PremiumMember(StandardMember):
    # Constructor
    def __init__(self, name, gender, num_days_member, num_gym_visits, favorite_workout, membership_type):
        super().__init__(name, gender, num_days_member, num_gym_visits, favorite_workout, membership_type)
        self.trainer = None
    # recommended_action methodsame as parent class but with addtional text from trainer
    def recommended_action(self):
        ratio = self.num_gym_visits/self.num_days_member
        if ratio >= .5:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Keep ut the routine! " + self.trainer.name + "(" + self.trainer.gender +  ") is proud!")
        elif ratio >= .3:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Slightly increase visits. "  + self.trainer.name + "(" + self.trainer.gender + ") is encouraging you!")
        else:
            print("Recommended Action for " + self.name + "(" + self.gender + "): Increase your frequency. "  + self.trainer.name + "(" + self.trainer.gender + ") still believes in you!")
# Trainer class
class Trainer ():
    # Constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
# import the members excel file as a pd and create an empty list of members
dfImportedMembers = pd.read_excel("gym_members.xlsx")
memberList = []
# for each row in the datafram create an object
for index, row in dfImportedMembers.iterrows():
    # Creates object based upon membership type
    if row["membership_type"] == "Standard" :
        oMember = StandardMember(row['name'], row['gender'], row['num_days_member'], row['num_gym_visits'], row['favorite_workout'], row['membership_type'])
    else:
        oMember = PremiumMember(row['name'], row['gender'], row['num_days_member'], row['num_gym_visits'], row['favorite_workout'], row['membership_type'])
    # add the member to the member list
    memberList.append(oMember)
# import the trainers excel file as a pd and create an empty list of trainers.
dfImportedTrainers = pd.read_excel("gym_trainers.xlsx")
trainerList = []
# for each row in the dataframe make a trainer object and store it to the trainers list.
for index, row in dfImportedTrainers.iterrows():
    oTrainer = Trainer(row['Name'], row['Gender'])
    trainerList.append(oTrainer)
# Assign trainers to each Premium member
for oMember in memberList:
    # only premium members have trainers
    if hasattr(oMember, 'trainer'):
        # assigm members a random trainer that matches their gender. Use while loop to ensure that genders match.
        if oMember.gender == "M" :
            choiceTrainer = random.choice(trainerList)
            while choiceTrainer.gender != 'M':
                choiceTrainer = random.choice(trainerList)
            oMember.trainer = choiceTrainer
        else:
            choiceTrainer = random.choice(trainerList)
            while choiceTrainer.gender != 'F':
                choiceTrainer = random.choice(trainerList)
            oMember.trainer = choiceTrainer
    # run recommended_action method for each member
    oMember.recommended_action()