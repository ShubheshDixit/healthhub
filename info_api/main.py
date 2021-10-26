from fastapi import FastAPI,HTTPException
from requests import status_codes

from utils.Doctor import doctors_nearby
from utils.wikiapi import wiki
from utils.Hospital import hospital_nearby
from utils.Labs import labs_nearby

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to HealthHub"}


@app.get("/doctor/{keyword}")
async def get_doctors(keyword: str):
    try: 
        res = doctors_nearby(keyword)
        return {"message": res}
    except:
        raise HTTPException(status_code = 404, detail="Doctor Not Found")

@app.get("/hospital")
async def get_hospital():
    try:
        res = hospital_nearby()
        return {"message": res}
    except:
        raise HTTPException(status_code = 404, detail="Hospital Not Found")

@app.get("/labs/{keyword}")
async def get_labs(keyword: str):
    try:
        res = labs_nearby(keyword)
        return {"message": res}
    except:
        raise HTTPException(status_code = 404, detail="Labs Not Found")

@app.get("/wiki/{keyword}")
async def get_info(keyword:str):
    try:
    
        info = wiki(keyword)
        return {"message": info }
    
    except:
        raise HTTPException(status_code = 404, detail="Disease Information Not Found")
