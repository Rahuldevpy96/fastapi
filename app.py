import json
import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import StudyCreate,StudyUpdate
from schema.studies import Base,Studies
# DEFINE THE DATABASE CREDENTIALS
# user = 'davide'
# password = 'jw8s0F4'
# host = '127.0.0.1'
# port = 5432
# database = 'testt'
# DATABASE_URI="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT

# Set up database
DATABASE_URI = os.environ.get("DATABASE_URI")
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# Define API endpoint for creating a new study
@app.post("/studies")
def create_study(study: StudyCreate):
    db = SessionLocal()
    print(study)
    new_study = Studies(**study.dict())
    db.add(new_study)
    db.commit()
    db.refresh(new_study)
    return new_study

# Define API endpoint for reading a study by ID
@app.get("/studies/{study_id}")
def read_study(study_id: int):
    db = SessionLocal()
    study = db.query(Studies).get(study_id)
    if study is None:
        raise HTTPException(status_code=404, detail="Study not found")
    return study


@app.put("/studies/{study_id}")
def update_study(study_id: int, study: StudyUpdate):
    db = SessionLocal()
    update_study = db.query(Studies).get(study_id)
    if update_study is None:
        raise HTTPException(status_code=404, detail="Study not found")
    update_data = study.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(update_study, key, value)
    db.add(update_study)
    db.commit()
    return update_study

@app.delete("/studies/{study_id}")
def delete_study(study_id: int):
    db = SessionLocal()
    study = db.query(Studies).get(study_id)
    if study is None:
        raise HTTPException(status_code=404, detail="Study not found")
    db.delete(study)
    db.commit()
    return {"study_id": study_id}



@app.patch("/studies/{study_id}")
def update_study(study_id: int, study: StudyUpdate):
    db = SessionLocal()
    update_study = db.query(Studies).get(study_id)
    if update_study is None:
        raise HTTPException(status_code=404, detail="Study not found")
    update_data = study.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(update_study, key, value)
    db.add(update_study)
    db.commit()
    return update_study