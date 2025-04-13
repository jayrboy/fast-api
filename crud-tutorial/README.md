# Virtual Environment (venv)

- เพื่อไม่ให้ไลบรารีแต่ละโปรเจกต์ชนกัน (เช่น โปรเจกต์ A ใช้ FastAPI 0.95 แต่ B ใช้ 0.110)
- ง่ายต่อการจัดการ requirements.txt และปลอดภัยและเหมาะสำหรับทำงานเป็นทีม

```bash
$ python3 -m venv venv
$ source venv/bin/activate  # สำหรับ macOS/Linux
$ venv\Scripts\activate     # สำหรับ Windows

(venv) $ deactivate
```

# Install Package

```bash
$ pip3 install -r requirements.txt
```

# Fast API Framework

```bash
$ pip3 install "fastapi[standard]"
$ pip3 install pydantic sqlalchemy
$ touch main.py
```

- initial FastAPI (main.py)

```py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}
```

# Run Dev

```bash
$ fastapi dev
$ fastapi dev main.py
```

# Test API docs/redoc

Now go to http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

# Deploy (Manual)

```bash
$ fastapi run main.py
```

หลังจากนั้น โดยทั่วไปจะมีการใช้ reverse proxy เช่น Nginx เพื่อรับคำขอ (requests) จากผู้ใช้งานและส่งต่อไปยัง Uvicorn
