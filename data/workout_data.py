from models.workout import WorkoutModel

def create_test_workouts():
    workouts = []
    
    # Workouts for Program 1: Beginner Full Body (program_id=1)
    workouts.extend([
        WorkoutModel(name="Full Body Workout A", day_of_week=1, program_id=1),
        WorkoutModel(name="Rest Day", day_of_week=2, program_id=1),
        WorkoutModel(name="Full Body Workout B", day_of_week=3, program_id=1),
        WorkoutModel(name="Rest Day", day_of_week=4, program_id=1),
        WorkoutModel(name="Full Body Workout C", day_of_week=5, program_id=1),
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=1),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=1),
    ])
    
    # Workouts for Program 2: Push Pull Legs (program_id=2)
    workouts.extend([
        WorkoutModel(name="Push Day", day_of_week=1, program_id=2),
        WorkoutModel(name="Pull Day", day_of_week=2, program_id=2),
        WorkoutModel(name="Leg Day", day_of_week=3, program_id=2),
        WorkoutModel(name="Push Day", day_of_week=4, program_id=2),
        WorkoutModel(name="Pull Day", day_of_week=5, program_id=2),
        WorkoutModel(name="Leg Day", day_of_week=6, program_id=2),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=2),
    ])
    
    # Workouts for Program 3: Upper Lower Split (program_id=3)
    workouts.extend([
        WorkoutModel(name="Upper Body", day_of_week=1, program_id=3),
        WorkoutModel(name="Lower Body", day_of_week=2, program_id=3),
        WorkoutModel(name="Rest Day", day_of_week=3, program_id=3),
        WorkoutModel(name="Upper Body", day_of_week=4, program_id=3),
        WorkoutModel(name="Lower Body", day_of_week=5, program_id=3),
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=3),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=3),
    ])
    
    # Workouts for Program 4: 5x5 Strength (program_id=4)
    workouts.extend([
        WorkoutModel(name="Squat, Bench, Row", day_of_week=1, program_id=4),
        WorkoutModel(name="Rest Day", day_of_week=2, program_id=4),
        WorkoutModel(name="Squat, Press, Deadlift", day_of_week=3, program_id=4),
        WorkoutModel(name="Rest Day", day_of_week=4, program_id=4),
        WorkoutModel(name="Squat, Bench, Row", day_of_week=5, program_id=4),
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=4),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=4),
    ])
    
    # Workouts for Program 5: HIIT Cardio (program_id=5)
    workouts.extend([
        WorkoutModel(name="HIIT Circuit A", day_of_week=1, program_id=5),
        WorkoutModel(name="Active Recovery", day_of_week=2, program_id=5),
        WorkoutModel(name="HIIT Circuit B", day_of_week=3, program_id=5),
        WorkoutModel(name="Active Recovery", day_of_week=4, program_id=5),
        WorkoutModel(name="HIIT Circuit C", day_of_week=5, program_id=5),
        WorkoutModel(name="Long Cardio", day_of_week=6, program_id=5),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=5),
    ])
    
    return workouts

workout_list = create_test_workouts()
