from fastapi import FastAPI
from typing import List
from .optimisation_algorithm import optimize
from .models import Contract, Solution


app = FastAPI()


@app.post("/spaceship/optimize", response_model=Solution)
def spaceship_optimisation(contracts: List[Contract]):
    return optimize(contracts)


def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)