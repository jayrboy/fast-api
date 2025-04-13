from sqlalchemy.future import select
from database import SessionLocal
from models import User, Conversation, Message
from datetime import datetime


async def save_conversation(username: str, user_msg: str, assistant_msg: str):
    async with SessionLocal() as db:
        user = await get_or_create_user(username, db)
        conversation = await create_conversation(user.id, db)

        user_message = Message(convo_id=conversation.id, sender="user", content=user_msg)
        assistant_message = Message(convo_id=conversation.id, sender="assistant", content=assistant_msg)

        db.add_all([user_message, assistant_message])
        conversation.updated_at = datetime.utcnow()
        await db.commit()

async def get_or_create_user(username: str, db):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()
    if not user:
        user = User(username=username)
        db.add(user)
        await db.commit()
        await db.refresh(user)
    return user

async def create_conversation(user_id: int, db):
    conversation = Conversation(user_id=user_id, title="New Chat", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    db.add(conversation)
    await db.commit()
    await db.refresh(conversation)
    return conversation
