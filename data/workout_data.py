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
    
    # Workouts for Program 6: Arjun's Custom Split (program_id=6)
    workouts.extend([
        WorkoutModel(name="Chest & Triceps", day_of_week=1, program_id=6),
        WorkoutModel(name="Back & Biceps", day_of_week=2, program_id=6),
        WorkoutModel(name="Shoulders", day_of_week=3, program_id=6),
        WorkoutModel(name="Legs", day_of_week=4, program_id=6),
        WorkoutModel(name="Arms & Core", day_of_week=5, program_id=6),
        WorkoutModel(name="Cardio", day_of_week=6, program_id=6),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=6),
    ])
    
    # Workouts for Program 7: Emma's Powerlifting (program_id=7)
    workouts.extend([
        WorkoutModel(name="Squat Day", day_of_week=1, program_id=7),
        WorkoutModel(name="Bench Press Day", day_of_week=2, program_id=7),
        WorkoutModel(name="Rest Day", day_of_week=3, program_id=7),
        WorkoutModel(name="Deadlift Day", day_of_week=4, program_id=7),
        WorkoutModel(name="Accessory Work", day_of_week=5, program_id=7),
        WorkoutModel(name="Light Recovery", day_of_week=6, program_id=7),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=7),
    ])
    
    # Workouts for Program 8: Fatima's Bodybuilding (program_id=8)
    workouts.extend([
        WorkoutModel(name="Chest & Back", day_of_week=1, program_id=8),
        WorkoutModel(name="Shoulders & Arms", day_of_week=2, program_id=8),
        WorkoutModel(name="Legs & Glutes", day_of_week=3, program_id=8),
        WorkoutModel(name="Push Focus", day_of_week=4, program_id=8),
        WorkoutModel(name="Pull Focus", day_of_week=5, program_id=8),
        WorkoutModel(name="Legs & Core", day_of_week=6, program_id=8),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=8),
    ])
    
    # Workouts for Program 9: Lucas's Crossfit (program_id=9)
    workouts.extend([
        WorkoutModel(name="WOD - Strength", day_of_week=1, program_id=9),
        WorkoutModel(name="WOD - Metcon", day_of_week=2, program_id=9),
        WorkoutModel(name="WOD - Gymnastics", day_of_week=3, program_id=9),
        WorkoutModel(name="WOD - Heavy", day_of_week=4, program_id=9),
        WorkoutModel(name="WOD - Endurance", day_of_week=5, program_id=9),
        WorkoutModel(name="WOD - Partner", day_of_week=6, program_id=9),
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=9),
    ])
    
    # Workouts for Program 10: Elena's Yoga Flow (program_id=10)
    workouts.extend([
        WorkoutModel(name="Morning Vinyasa", day_of_week=1, program_id=10),
        WorkoutModel(name="Power Yoga", day_of_week=2, program_id=10),
        WorkoutModel(name="Gentle Hatha", day_of_week=3, program_id=10),
        WorkoutModel(name="Ashtanga Flow", day_of_week=4, program_id=10),
        WorkoutModel(name="Yin Yoga", day_of_week=5, program_id=10),
        WorkoutModel(name="Hot Yoga", day_of_week=6, program_id=10),
        WorkoutModel(name="Meditation & Rest", day_of_week=7, program_id=10),
    ])
    
    return workouts

workout_list = create_test_workouts()
