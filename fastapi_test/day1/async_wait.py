from fastapi import FastAPI

app = FastAPI()

def some_library():
    return 'hello world'

@app.get('/')
def results():
    results = some_library()
    return results

@app.get('/async')
async def get_results():
    results = await some_library()
    return results

import asyncio
import time
@app.get('/async2')
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

@app.get('/asyncmain')
async def main():
    print(f"started at {time.str}")

