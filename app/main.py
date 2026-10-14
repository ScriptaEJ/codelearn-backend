from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'status_api': 'active'}

