from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.workout import WorkoutModel
from models.program import ProgramModel
from models.user import UserModel
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from serializers.workout import WorkoutSchema, WorkoutCreateSchema, WorkoutUpdateSchema

router = APIRouter()

@router.get('/workouts', response_model=List[WorkoutSchema])
def get_workouts(db: Session = Depends(get_db)):
    workouts = db.query(WorkoutModel).all()
    return workouts

@router.get('/workouts/{workout_id}', response_model=WorkoutSchema)
def get_single_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    if workout:
        return workout
    else:
        raise HTTPException(status_code=404, detail="Workout not found")

@router.get('/programs/{program_id}/workouts', response_model=List[WorkoutSchema])
def get_workouts_by_program(program_id: int, db: Session = Depends(get_db)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    workouts = db.query(WorkoutModel).filter(WorkoutModel.program_id == program_id).order_by(WorkoutModel.day_of_week).all()
    return workouts

@router.post('/workouts', response_model=WorkoutSchema)
def create_workout(workout: WorkoutCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == workout.program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only add workouts to your own programs")
    
    existing_workout = db.query(WorkoutModel).filter(
        WorkoutModel.program_id == workout.program_id,
        WorkoutModel.day_of_week == workout.day_of_week
    ).first()
    
    if existing_workout:
        raise HTTPException(status_code=400, detail=f"A workout already exists for day {workout.day_of_week} in this program")
    
    new_workout = WorkoutModel(**workout.dict())
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout

@router.put("/workouts/{workout_id}", response_model=WorkoutSchema)
def update_workout(workout_id: int, workout: WorkoutUpdateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    program = db.query(ProgramModel).filter(ProgramModel.id == db_workout.program_id).first()
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only modify workouts in your own programs")
    
    if workout.day_of_week is not None and workout.day_of_week != db_workout.day_of_week:
        existing_workout = db.query(WorkoutModel).filter(
            WorkoutModel.program_id == db_workout.program_id,
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

@router.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    program = db.query(ProgramModel).filter(ProgramModel.id == db_workout.program_id).first()
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete workouts from your own programs")
    
    db.delete(db_workout)
    db.commit()
    return {"message": f"Workout {workout_id} has been deleted"}
