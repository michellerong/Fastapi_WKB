import uvicorn
from fastapi import FastAPI
from homework import homework

app = FastAPI()


@app.get("/homework")
def get_homeworks() -> dict:
    return homework

@app.get('/school')
def get_homeworks_by_school(school: str = "") -> dict:
    return homework[school]
    


@app.get('/semester')
def get_homeworks_by_semester(semester: str = "") -> list:
    ntue = homework["ntue"][semester]
    ntut = homework["ntut"][semester]

    return [*ntue, *ntut]

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)
