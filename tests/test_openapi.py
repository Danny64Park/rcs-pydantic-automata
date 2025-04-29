from fastapi import FastAPI

from rcs_pydantic_automata import SendInfo

app = FastAPI()


@app.post("/")
def read_root(request, payload: SendInfo):
    return {"Hello": "World"}


def test_openapi():
    assert app.openapi()
