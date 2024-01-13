from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import model 
from db import engine, SessionLocal
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from rectangle_solver import largest_rectangle
import copy




# Fast API setup
app = FastAPI()
model.Base.metadata.create_all(bind = engine)

class MatrixRequest(BaseModel):
    matrix: List[List[int]]

@app.post("/largest_rectangle")
async def get_largest_rectangle(matrix_request: MatrixRequest):
    start_time = datetime.utcnow()

    matrix = matrix_request.matrix
    matrix_1 = copy.deepcopy(matrix)
    
    #print(matrix_1)
    result = largest_rectangle(matrix)

    end_time = datetime.utcnow()
    turnaround_time = (end_time - start_time).total_seconds()

    # Log the request and response
    log_entry = model.Log(request=str(matrix_1), response=str(result), turnaround_time=int(turnaround_time))
    print(matrix_1)
    db = SessionLocal()
    db.add(log_entry)
    db.commit()
    db.close()

    return result
