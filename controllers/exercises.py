from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.exercise import ExerciseModel
from models.program import ProgramModel
from models.workout import WorkoutModel
from models.user import UserModel
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from serializers.exercise import ExerciseSchema, ExerciseCreateSchema, ExerciseUpdateSchema
from serializers.workout import WorkoutSchema

router = APIRouter()

# Get all exercises
@router.get('/exercises', response_model=List[ExerciseSchema])
def get_all_exercises(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    exercises = db.query(ExerciseModel).all()
    return exercises

# Get signle exercise
@router.get('/exercises/{exercise_id}', response_model=ExerciseSchema)
def get_single_exercise(exercise_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    exercise = db.query(ExerciseModel).filter(ExerciseModel.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

# Create exercise
@router.post('/exercises', response_model=ExerciseSchema)
def create_exercise(exercise: ExerciseCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_exercise = ExerciseModel(**exercise.dict())
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)
    return new_exercise

# Update exercise
@router.put("/exercises/{exercise_id}", response_model=ExerciseSchema)
def update_exercise(exercise_id: int, exercise: ExerciseUpdateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_exercise = db.query(ExerciseModel).filter(ExerciseModel.id == exercise_id).first()
    
    if not db_exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    exercise_data = exercise.dict(exclude_unset=True)
    for key, value in exercise_data.items():
        setattr(db_exercise, key, value)
        
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

# Delete exercise from the exercise list
@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_exercise = db.query(ExerciseModel).filter(ExerciseModel.id == exercise_id).first()
    
    if not db_exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    
    db.delete(db_exercise)
    db.commit()
    return {"message": f"Exercise {exercise_id} has been deleted"}

# Get exercise specific to a workout
@router.get('/programs/{program_id}/workouts/{workout_id}/exercises', response_model=List[ExerciseSchema])
def get_exercises_by_workout(program_id: int, workout_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only view exercises in your own workouts or default programs")
    
    workout = db.query(WorkoutModel).filter(
        WorkoutModel.id == workout_id,
        WorkoutModel.program_id == program_id
    ).first()
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found in this program")
    
    if not workout.exercise_ids:
        return []
    
    exercises = db.query(ExerciseModel).filter(ExerciseModel.id.in_(workout.exercise_ids)).all()
    return exercises
