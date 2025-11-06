#  FastAPI 
A simple CRUD (Create, Read, Update, Delete) API built using **FastAPI**.  
This project demonstrates how to build and manage RESTful APIs in Python with FastAPI using a Tea store example.  

---

## 🚀 Features  

✅ `GET /` — Welcome message  
✅ `GET /teas` — Retrieve all teas  
✅ `POST /teas` — Add a new tea  
✅ `PUT /teas/{tea_id}` — Update a tea by its ID  
✅ `DELETE /teas/{tea_id}` — Delete a tea by its ID  

---

## 🧠 Tech Stack  

- **Python 3.10+**  
- **FastAPI** — Core backend framework  
- **Uvicorn** — ASGI web server for running FastAPI  
- **Pydantic** — For request validation and data modeling  

---

## ⚙️ Setup Instructions  

### 1️⃣ Create and Activate Virtual Environment  

**Windows:**
```bash
python -m venv fastenv
fastenv\Scripts\activate
````

**Mac/Linux:**

```bash
python3 -m venv fastenv
source fastenv/bin/activate
```

---

### 2️⃣ Install Dependencies

Create a `requirements.txt` file (if not already present) and add:

```
fastapi
uvicorn
```

Then install them:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Server

Run the FastAPI server with:

```bash
uvicorn main:app --reload
```

✅ You’ll see output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Now open the browser and visit:

```
http://127.0.0.1:8000
```

You should get:

```json
{"message": "Welcome to the Tea API!"}
```

---

### 4️⃣ Open Swagger UI

FastAPI provides a built-in interactive API documentation.

Go to:

```
http://127.0.0.1:8000/docs
```

Here, you can test all endpoints (`GET`, `POST`, `PUT`, `DELETE`) easily.

---

## 📜 API Endpoints

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| GET    | `/`              | Welcome message    |
| GET    | `/teas`          | Retrieve all teas  |
| POST   | `/teas`          | Add a new tea      |
| PUT    | `/teas/{tea_id}` | Update a tea by ID |
| DELETE | `/teas/{tea_id}` | Delete a tea by ID |

---

## 🧾 Example Request (POST /teas)

**Request Body:**

```json
{
  "id": 1,
  "name": "Masala Chai",
  "origin": "India",
  "price": 50.0,
  "ingredients": ["Tea leaves", "Milk", "Spices"]
}
```

**Response:**

```json
{
  "id": 1,
  "name": "Masala Chai",
  "origin": "India",
  "price": 50.0,
  "ingredients": ["Tea leaves", "Milk", "Spices"]
}
```

---

## 🧩 Code Overview

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define model using Pydantic
class Tea(BaseModel):
    id: int
    name: str
    origin: str
    price: float
    ingredients: List[str]

# In-memory storage
teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}
```

---

## 📁 Folder Structure

```
FastApi/
│
├── fastenv/             # Virtual environment
├── __pycache__/         # Cache files
├── main.py              # Main FastAPI application
├── requirements.txt     # Project dependencies
└── README.md            # Documentation file
```

---

## 📚 Learn More

* FastAPI Docs → [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
* Uvicorn Docs → [https://www.uvicorn.org](https://www.uvicorn.org)

---

## 💡 Author

👩‍💻 **Riti Rai**
Simple CRUD API using FastAPI for learning and demonstration.

