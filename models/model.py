from pydantic import BaseModel

# Define request and response models for API
class StudyCreate(BaseModel):
    user_id: str
    referring_physician_name: str
    study_id: str
    study_instance_uid: str
    patient_name: str
    patient_age: str
    patient_sex: str
    patient_mrn: str
    bodypart_examined: str
    findings: str
    infer_status: str
    infer_date: str

class StudyUpdate(BaseModel):
    user_id: str = None
    referring_physician_name: str = None
    study_id: str = None
    study_instance_uid: str = None
    patient_name: str = None
    patient_age: str = None
    patient_sex: str = None
    patient_mrn: str = None
    bodypart_examined: str = None
    findings: str = None
    infer_status: str = None
    infer_date: str = None