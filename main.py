from fastapi import FastAPI  # core framework
from pydantic import BaseModel #help in validation jo bhi python file m jo bhi web request aayegi ya fir send karenge uske structure syntax ke guidlines ko define krne k liye pydantic ka use krenge & basemodel m define model ke upar hi overwrite karte hain
from typing import List

app = FastAPI()  # create an instance of FastAPI
# Define a Pydantic model for the item class Item(BaseModel):
class Tea(BaseModel):
    id: int
    name: str
    origin: str
    price: float
    ingredients: List[str]

# In-memory storage for teas
teas: List[Tea] = [] #ye list m sare tea objects store krenge

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")#decorator jo define krta hai ki ye function kis endpoint pr accessible hoga means superpower deta hai function ko
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):#ye function ek tea object lega as input jo ki request body m hoga
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):#ye function ek tea object ko update krne k liye hai pydantic model ka use krke jo request body m hoga and help krta hai validation m
    for index, tea in enumerate(teas):#enumerate function index or value dono provide krta hai and hum uske basis pr update kr skte hain 
        if tea.id == tea_id:#check kr rhe hain ki jo tea id humne url m di hai wo list m exist krti hai ya nahi and fir usko update kr rhe hain
            teas[index] = updated_tea#update kr rhe hain list m check krke ki id match krti hai ya nahi and fir us index pr updated tea object dal rhe hain
            return updated_tea#return kr rhe hain updated tea object kuoki wo successful operation hai
    return {"error": "Tea not found"}#agar tea id match nahi krti to error message return kr denge

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):#ye function ek tea object ko delete krne k liye hai jo request body m hoga
    for index, tea in enumerate(teas):#enumerate function index or value dono provide krta hai and hum uske basis pr delete kr skte hain 
        if tea.id == tea_id:#check kr rhe hain ki jo tea id humne url m di hai wo list m exist krti hai ya nahi and fir usko delete kr rhe hain
            deleted_tea = teas.pop(index)#pop function use krke us index pr jo tea object hai usko delete kr denge and usko ek variable m store kr lenge
            return deleted_tea#return kr rhe hain deleted tea object kuoki wo successful operation hai
    return {"error": "Tea not found"}#agar tea id match nahi krti to error message return kr denge
