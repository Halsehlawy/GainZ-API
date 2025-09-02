from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.program import ProgramModel
from models.user import UserModel
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user
from serializers.program import ProgramSchema, ProgramCreateSchema

router = APIRouter()

# view all default programs and programs you own  
@router.get('/programs',response_model=List[ProgramSchema])
def get_programs(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    programs = db.query(ProgramModel).filter(
        (ProgramModel.user_id == None) | (ProgramModel.user_id == current_user.id)
    ).all()
    return programs

# get a specific program
@router.get('/programs/{program_id}',response_model=ProgramSchema)
def get_single_program(program_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if program.user_id is not None and program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only view your own programs or default programs")
    
    return program

# create a program
@router.post('/programs', response_model=ProgramSchema)
def create_program(program: ProgramCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_program = ProgramModel(**program.dict(), user_id = current_user.id)
    db.add(new_program)
    db.commit()
    db.refresh(new_program)
    return new_program

# update program
@router.put("/programs/{program_id}", response_model=ProgramSchema)
def update_program(program_id: int, program: ProgramCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_program = db.query(ProgramModel).filter(ProgramModel.id==program_id).first()
    
    if not db_program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if db_program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    program_data = program.dict(exclude_unset=True)
    for key,value in program_data.items():
        setattr(db_program,key,value)
        
    db.commit()
    db.refresh(db_program)
    return db_program

# delete programs you own
@router.delete("/programs/{program_id}")
def delete_program(program_id:int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_program = db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
    
    if not db_program:
        raise HTTPException(status_code=404, detail="Program not found")
    
    if db_program.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    db.delete(db_program)
    db.commit()
    return {"message": f"Program {program_id} has been deleted"}
