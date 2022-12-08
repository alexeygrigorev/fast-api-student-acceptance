## Student Acceptance Prediction

In this project, we develop a model for predicting if a student
will be admitted to college or not. We use FastAPI for serving
this model

This project is done as a part of [Project of the Week at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-12-07-fastapi.md).
It's a continuation of [another project](https://github.com/alexeygrigorev/student-acceptance-project)
where we used streamlit for creating the UI for the model


Dataset: https://www.kaggle.com/datasets/mahwiz/school-data



## Setup 

Install the devependencies 

```bash
pipenv install --dev
```

## Run

Train the model:

```bash
pipenv run python train.py
```

Serve it

```bash
pipenv run uvicorn predict:app --reload
```

Navigate to http://localhost:8000/docs to see the docs

Test request:

```json
{
    "type_school": "Academic",
    "school_accreditation": "A",
    "gender": "Male",
    "interest": "Uncertain",
    "residence": "Rural",
    "parent_age": 48,
    "parent_salary": 7160000,
    "house_area": 71.0,
    "average_grades": 88.46,
    "parent_was_in_college": true
}
```