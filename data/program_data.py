from models.program import ProgramModel

def create_test_programs():
    # Default programs that can be used by any user
    program1 = ProgramModel(name="Beginner Full Body", is_default=True, user_id=None)
    program2 = ProgramModel(name="Push Pull Legs", is_default=True, user_id=None)
    program3 = ProgramModel(name="Upper Lower Split", is_default=True, user_id=None)
    program4 = ProgramModel(name="5x5 Strength", is_default=True, user_id=None)
    program5 = ProgramModel(name="HIIT Cardio", is_default=True, user_id=None)
    
    # User-specific custom programs (assuming user IDs 1-5 from user_data)
    program6 = ProgramModel(name="Arjun's Custom Split", is_default=False, user_id=1)
    program7 = ProgramModel(name="Emma's Powerlifting", is_default=False, user_id=2)
    program8 = ProgramModel(name="Fatima's Bodybuilding", is_default=False, user_id=3)
    program9 = ProgramModel(name="Lucas's Crossfit", is_default=False, user_id=4)
    program10 = ProgramModel(name="Elena's Yoga Flow", is_default=False, user_id=5)
    
    return [program1, program2, program3, program4, program5, program6, program7, program8, program9, program10]

program_list = create_test_programs()
