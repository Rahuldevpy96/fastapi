from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the 'studies' table
class Studies(Base):
    __tablename__ = 'studies'
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(String)
    referring_physician_name = Column(String)
    study_id = Column(String)
    study_instance_uid = Column(String)
    patient_name = Column(String)
    patient_age = Column(String)
    patient_sex = Column(String)
    patient_mrn = Column(String)
    bodypart_examined = Column(String)
    findings = Column(String)
    infer_status = Column(String)
    infer_date = Column(String)
