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
    # return {
    #     "timesheet": {
    #         "Job 1": {
    #             "Monday": 8.0,
    #             "Tuesday": 0.0,
    #             "Wednesday": 0.0,
    #             "Thursday": 8.0,
    #             "Friday": 8.0,
    #             "Saturday": 0.0,
    #             "Sunday": 0.0,
    #         },
    #         "Job 2": {
    #             "Monday": 0.0,
    #             "Tuesday": 8.0,
    #             "Wednesday": 0.0,
    #             "Thursday": 0.0,
    #             "Friday": 0.0,
    #             "Saturday": 0.0,
    #             "Sunday": 0.0,
    #         },
    #         "Job 3": {
    #             "Monday": 0.0,
    #             "Tuesday": 0.0,
    #             "Wednesday": 8.0,
    #             "Thursday": 0.0,
    #             "Friday": 0.0,
    #             "Saturday": 0.0,
    #             "Sunday": 0.0,
    #         }
    #     }
    # }
    return {
        "timesheet": [
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Monday, 2022, 08, 01, Job 1, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Tuesday, 2022, 08, 02, Job 2, 1"},
            {"Wednesday, 2022, 08, 03, Job 1, 1"},
            {"Wednesday, 2022, 08, 03, Job 1, 1"},
            {"Wednesday, 2022, 08, 03, Job 1, 1"},
            {"Wednesday, 2022, 08, 03, Job 1, 1"},
            {"Wednesday, 2022, 08, 03, Job 2, 1"},
            {"Wednesday, 2022, 08, 03, Job 2, 1"},
            {"Wednesday, 2022, 08, 03, Job 2, 1"},
            {"Wednesday, 2022, 08, 03, Job 2, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Thursday, 2022, 08, 04, Job 3, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"},
            {"Friday, 2022, 08, 05, Job 4, 1"}
        ]
    }

@app.get("/user/{user_id}")
async def get_user_info(user_id: str):
    print(type(user_id))
    database = {
        "1": {
            "timesheets": []
        },
        "2": {
            "timesheets": []
        }
    }
    return {"userInfo": database[user_id]}