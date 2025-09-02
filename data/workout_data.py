from models.workout import WorkoutModel

def create_test_workouts():
    workouts = []
    
    # Workouts for Program 1: Beginner Full Body (program_id=1)
    workouts.extend([
        WorkoutModel(name="Full Body Workout A", day_of_week=1, program_id=1, exercise_ids=[1, 7, 14]),  # Push-ups, Squats, Bench Press
        WorkoutModel(name="Rest Day", day_of_week=2, program_id=1, exercise_ids=[10]),  # Light Stretching
        WorkoutModel(name="Full Body Workout B", day_of_week=3, program_id=1, exercise_ids=[4, 8, 15]),  # Pull-ups, Lunges, Bent-over Rows
        WorkoutModel(name="Rest Day", day_of_week=4, program_id=1, exercise_ids=[11]),  # Mobility Work
        WorkoutModel(name="Full Body Workout C", day_of_week=5, program_id=1, exercise_ids=[2, 9, 6]),  # Chest Press, Calf Raises, Bicep Curls
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=1, exercise_ids=[12]),  # Light Walk
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=1, exercise_ids=[13]),  # Yoga
    ])
    
    # Workouts for Program 2: Push Pull Legs (program_id=2)
    workouts.extend([
        WorkoutModel(name="Push Day", day_of_week=1, program_id=2, exercise_ids=[1, 2, 3]),  # Push-ups, Chest Press, Shoulder Press
        WorkoutModel(name="Pull Day", day_of_week=2, program_id=2, exercise_ids=[4, 5, 6]),  # Pull-ups, Lat Pulldown, Bicep Curls
        WorkoutModel(name="Leg Day", day_of_week=3, program_id=2, exercise_ids=[7, 8, 9]),  # Squats, Lunges, Calf Raises
        WorkoutModel(name="Push Day", day_of_week=4, program_id=2, exercise_ids=[1, 2, 3]),  # Push-ups, Chest Press, Shoulder Press
        WorkoutModel(name="Pull Day", day_of_week=5, program_id=2, exercise_ids=[4, 5, 6]),  # Pull-ups, Lat Pulldown, Bicep Curls
        WorkoutModel(name="Leg Day", day_of_week=6, program_id=2, exercise_ids=[7, 8, 9]),  # Squats, Lunges, Calf Raises
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=2, exercise_ids=[13]),  # Yoga
    ])
    
    # Workouts for Program 3: Upper Lower Split (program_id=3)
    workouts.extend([
        WorkoutModel(name="Upper Body", day_of_week=1, program_id=3, exercise_ids=[14, 15, 16]),  # Bench Press, Bent-over Rows, Overhead Press
        WorkoutModel(name="Lower Body", day_of_week=2, program_id=3, exercise_ids=[17, 18, 19]),  # Deadlifts, Leg Press, Leg Curls
        WorkoutModel(name="Rest Day", day_of_week=3, program_id=3, exercise_ids=[26]),  # Active Recovery
        WorkoutModel(name="Upper Body", day_of_week=4, program_id=3, exercise_ids=[20, 21, 22]),  # Incline Dumbbell Press, Cable Rows, Lateral Raises
        WorkoutModel(name="Lower Body", day_of_week=5, program_id=3, exercise_ids=[23, 24, 25]),  # Bulgarian Split Squats, Romanian Deadlifts, Walking Lunges
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=3, exercise_ids=[27]),  # Swimming
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=3, exercise_ids=[28]),  # Foam Rolling
    ])
    
    # Workouts for Program 4: 5x5 Strength (program_id=4)
    workouts.extend([
        WorkoutModel(name="Squat, Bench, Row", day_of_week=1, program_id=4, exercise_ids=[29, 14, 15]),  # Barbell Squats, Bench Press, Bent-over Rows
        WorkoutModel(name="Rest Day", day_of_week=2, program_id=4, exercise_ids=[26]),  # Active Recovery
        WorkoutModel(name="Squat, Press, Deadlift", day_of_week=3, program_id=4, exercise_ids=[29, 16, 17]),  # Barbell Squats, Overhead Press, Deadlifts
        WorkoutModel(name="Rest Day", day_of_week=4, program_id=4, exercise_ids=[26]),  # Active Recovery
        WorkoutModel(name="Squat, Bench, Row", day_of_week=5, program_id=4, exercise_ids=[29, 14, 15]),  # Barbell Squats, Bench Press, Bent-over Rows
        WorkoutModel(name="Rest Day", day_of_week=6, program_id=4, exercise_ids=[27]),  # Swimming
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=4, exercise_ids=[35]),  # Meditation
    ])
    
    # Workouts for Program 5: HIIT Cardio (program_id=5)
    workouts.extend([
        WorkoutModel(name="HIIT Circuit A", day_of_week=1, program_id=5, exercise_ids=[30, 31]),  # HIIT Cardio, Bodyweight Squats
        WorkoutModel(name="Active Recovery", day_of_week=2, program_id=5, exercise_ids=[26]),  # Active Recovery
        WorkoutModel(name="HIIT Circuit B", day_of_week=3, program_id=5, exercise_ids=[30, 33]),  # HIIT Cardio, Plank Variations
        WorkoutModel(name="Active Recovery", day_of_week=4, program_id=5, exercise_ids=[32]),  # Yoga Flow
        WorkoutModel(name="HIIT Circuit C", day_of_week=5, program_id=5, exercise_ids=[30, 8]),  # HIIT Cardio, Lunges
        WorkoutModel(name="Long Cardio", day_of_week=6, program_id=5, exercise_ids=[34]),  # Dancing
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=5, exercise_ids=[35]),  # Meditation
    ])
    
    # Workouts for Program 6: Arjun's Custom Split (program_id=6)
    workouts.extend([
        WorkoutModel(name="Chest & Triceps", day_of_week=1, program_id=6, exercise_ids=[14, 2, 1]),  # Bench Press, Chest Press, Push-ups
        WorkoutModel(name="Back & Biceps", day_of_week=2, program_id=6, exercise_ids=[15, 4, 6]),  # Bent-over Rows, Pull-ups, Bicep Curls
        WorkoutModel(name="Shoulders", day_of_week=3, program_id=6, exercise_ids=[3, 16, 22]),  # Shoulder Press, Overhead Press, Lateral Raises
        WorkoutModel(name="Legs", day_of_week=4, program_id=6, exercise_ids=[17, 7, 8]),  # Deadlifts, Squats, Lunges
        WorkoutModel(name="Arms & Core", day_of_week=5, program_id=6, exercise_ids=[6, 33, 9]),  # Bicep Curls, Plank Variations, Calf Raises
        WorkoutModel(name="Cardio", day_of_week=6, program_id=6, exercise_ids=[30]),  # HIIT Cardio
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=6, exercise_ids=[13]),  # Yoga
    ])
    
    # Workouts for Program 7: Emma's Powerlifting (program_id=7)
    workouts.extend([
        WorkoutModel(name="Squat Day", day_of_week=1, program_id=7, exercise_ids=[29, 7]),  # Barbell Squats, Squats
        WorkoutModel(name="Bench Press Day", day_of_week=2, program_id=7, exercise_ids=[14, 2]),  # Bench Press, Chest Press
        WorkoutModel(name="Rest Day", day_of_week=3, program_id=7, exercise_ids=[26]),  # Active Recovery
        WorkoutModel(name="Deadlift Day", day_of_week=4, program_id=7, exercise_ids=[17, 24]),  # Deadlifts, Romanian Deadlifts
        WorkoutModel(name="Accessory Work", day_of_week=5, program_id=7, exercise_ids=[15, 16, 22]),  # Bent-over Rows, Overhead Press, Lateral Raises
        WorkoutModel(name="Light Recovery", day_of_week=6, program_id=7, exercise_ids=[12]),  # Light Walk
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=7, exercise_ids=[35]),  # Meditation
    ])
    
    # Workouts for Program 8: Fatima's Bodybuilding (program_id=8)
    workouts.extend([
        WorkoutModel(name="Chest & Back", day_of_week=1, program_id=8, exercise_ids=[14, 20, 15, 21]),  # Bench Press, Incline Dumbbell Press, Bent-over Rows, Cable Rows
        WorkoutModel(name="Shoulders & Arms", day_of_week=2, program_id=8, exercise_ids=[3, 22, 6]),  # Shoulder Press, Lateral Raises, Bicep Curls
        WorkoutModel(name="Legs & Glutes", day_of_week=3, program_id=8, exercise_ids=[17, 18, 23, 25]),  # Deadlifts, Leg Press, Bulgarian Split Squats, Walking Lunges
        WorkoutModel(name="Push Focus", day_of_week=4, program_id=8, exercise_ids=[14, 1, 3]),  # Bench Press, Push-ups, Shoulder Press
        WorkoutModel(name="Pull Focus", day_of_week=5, program_id=8, exercise_ids=[4, 5, 15]),  # Pull-ups, Lat Pulldown, Bent-over Rows
        WorkoutModel(name="Legs & Core", day_of_week=6, program_id=8, exercise_ids=[7, 33, 9]),  # Squats, Plank Variations, Calf Raises
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=8, exercise_ids=[34]),  # Dancing
    ])
    
    # Workouts for Program 9: Lucas's Crossfit (program_id=9)
    workouts.extend([
        WorkoutModel(name="WOD - Strength", day_of_week=1, program_id=9, exercise_ids=[29, 14, 17]),  # Barbell Squats, Bench Press, Deadlifts
        WorkoutModel(name="WOD - Metcon", day_of_week=2, program_id=9, exercise_ids=[30, 31, 33]),  # HIIT Cardio, Bodyweight Squats, Plank Variations
        WorkoutModel(name="WOD - Gymnastics", day_of_week=3, program_id=9, exercise_ids=[4, 1]),  # Pull-ups, Push-ups
        WorkoutModel(name="WOD - Heavy", day_of_week=4, program_id=9, exercise_ids=[17, 16]),  # Deadlifts, Overhead Press
        WorkoutModel(name="WOD - Endurance", day_of_week=5, program_id=9, exercise_ids=[12, 27]),  # Light Walk, Swimming
        WorkoutModel(name="WOD - Partner", day_of_week=6, program_id=9, exercise_ids=[8, 7, 33]),  # Lunges, Squats, Plank Variations
        WorkoutModel(name="Rest Day", day_of_week=7, program_id=9, exercise_ids=[13]),  # Yoga
    ])
    
    # Workouts for Program 10: Elena's Yoga Flow (program_id=10)
    workouts.extend([
        WorkoutModel(name="Morning Vinyasa", day_of_week=1, program_id=10, exercise_ids=[32]),  # Yoga Flow
        WorkoutModel(name="Power Yoga", day_of_week=2, program_id=10, exercise_ids=[32, 33]),  # Yoga Flow, Plank Variations
        WorkoutModel(name="Gentle Hatha", day_of_week=3, program_id=10, exercise_ids=[13]),  # Yoga
        WorkoutModel(name="Ashtanga Flow", day_of_week=4, program_id=10, exercise_ids=[32]),  # Yoga Flow
        WorkoutModel(name="Yin Yoga", day_of_week=5, program_id=10, exercise_ids=[13, 35]),  # Yoga, Meditation
        WorkoutModel(name="Hot Yoga", day_of_week=6, program_id=10, exercise_ids=[32]),  # Yoga Flow
        WorkoutModel(name="Meditation & Rest", day_of_week=7, program_id=10, exercise_ids=[35]),  # Meditation
    ])
    
    return workouts

workout_list = create_test_workouts()
