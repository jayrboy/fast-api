from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import ItemDB
from app.schemas import ItemCreate, ItemResponse


# Create SQLite database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# http://127.0.0.1:8000/

@app.get("/")
def read_root():
    print("Hello World")
    return {"framework": "FastAPI", "version": "0.115.12", "sql_alchemy": "2.0.40"}

# ✅ Create Item
@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    # print(item.name, item.price, item.is_offer)
    db_item = ItemDB(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 📚 Read All Items
@app.get("/items", response_model=List[ItemResponse])
async def read_items(db: Session = Depends(get_db)):
    return db.query(ItemDB).all()

# 📚 Read Page + All Items v2 (เพิ่มลูกเล่นใส่ query parameter เช่น filter, pagination)
@app.get("/items/")
async def read_page_items(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    items = db.query(ItemDB).offset(skip).limit(limit).all()
    return items

# 📖 Read Item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# 📝 Update Item
@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# ❌ Delete Item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}