from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.workout import WorkoutModel
from models.program import ProgramModel
from models.user import UserModel
from models.exercise import ExerciseModel
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from serializers.workout import WorkoutSchema, WorkoutCreateSchema, WorkoutUpdateSchema
from serializers.exercise import ExerciseSchema

router = APIRouter()

# Get all workouts for a specific program
@router.get('/programs/{program_id}/workouts', response_model=List[WorkoutSchema])
def get_workouts_by_program(program_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only view workouts in your own programs or default programs")
    
    workouts = db.query(WorkoutModel).filter(WorkoutModel.program_id == program_id).order_by(WorkoutModel.day_of_week).all()
    return workouts

# Get a single workout for a specific program
@router.get('/programs/{program_id}/workouts/{workout_id}', response_model=WorkoutSchema)
def get_single_workout(program_id: int, workout_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only view workouts in your own programs or default programs")
    
    workout = db.query(WorkoutModel).filter(
        WorkoutModel.id == workout_id,
        WorkoutModel.program_id == program_id
    ).first()
    
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found in this program")
    
    return workout

# Create a workout in a program
@router.post('/programs/{program_id}/workouts', response_model=WorkoutSchema)
def create_workout(program_id: int, workout: WorkoutCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only add workouts to your own programs")
    
    workout.program_id = program_id
    
    existing_workout = db.query(WorkoutModel).filter(
        WorkoutModel.program_id == program_id,
        WorkoutModel.day_of_week == workout.day_of_week
    ).first()
    
    if existing_workout:
        raise HTTPException(status_code=400, detail=f"A workout already exists for day {workout.day_of_week} in this program")
    
    new_workout = WorkoutModel(**workout.dict())
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout

# update a workout in a program
@router.put("/programs/{program_id}/workouts/{workout_id}", response_model=WorkoutSchema)
def update_workout(program_id: int, workout_id: int, workout: WorkoutUpdateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only modify workouts in your own programs")
    
    db_workout = db.query(WorkoutModel).filter(
        WorkoutModel.id == workout_id,
        WorkoutModel.program_id == program_id
    ).first()
    
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found in this program")
    
    if workout.day_of_week is not None and workout.day_of_week != db_workout.day_of_week:
        existing_workout = db.query(WorkoutModel).filter(
            WorkoutModel.program_id == program_id,
            WorkoutModel.day_of_week == workout.day_of_week,
            WorkoutModel.id != workout_id
        ).first()
        
        if existing_workout:
            raise HTTPException(status_code=400, detail=f"A workout already exists for day {workout.day_of_week} in this program")
    
    workout_data = workout.dict(exclude_unset=True)
    for key, value in workout_data.items():
        setattr(db_workout, key, value)
        
    db.commit()
    db.refresh(db_workout)
    return db_workout

# Delete a workout from a program
@router.delete("/programs/{program_id}/workouts/{workout_id}")
def delete_workout(program_id: int, workout_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete workouts from your own programs")
    
    db_workout = db.query(WorkoutModel).filter(
        WorkoutModel.id == workout_id,
        WorkoutModel.program_id == program_id
    ).first()
    
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found in this program")
    
    db.delete(db_workout)
    db.commit()
    return {"message": f"Workout {workout_id} has been deleted from program {program_id}"}
