from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Well done! You called the API!"}

@app.get("/faketimesheet")
async def get_fake_timesheet():
    return {
        "timesheet": {
            "Job 1": {
                "Monday": 8.0,
                "Tuesday": 0.0,
                "Wednesday": 0.0,
                "Thursday": 8.0,
                "Friday": 8.0,
                "Saturday": 0.0,
                "Sunday": 0.0,
            },
            "Job 2": {
                "Monday": 0.0,
                "Tuesday": 8.0,
                "Wednesday": 0.0,
                "Thursday": 0.0,
                "Friday": 0.0,
                "Saturday": 0.0,
                "Sunday": 0.0,
            },
            "Job 3": {
                "Monday": 0.0,
                "Tuesday": 0.0,
                "Wednesday": 8.0,
                "Thursday": 0.0,
                "Friday": 0.0,
                "Saturday": 0.0,
                "Sunday": 0.0,
            }
        }
    }