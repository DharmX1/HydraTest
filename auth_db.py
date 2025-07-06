# auth_db.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://dharmgodarax1:<2UpNzcLwgv33jADm>@cluster0.urxkl26.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URI)
db = client["saini_bot"]
auth_users_col = db["authorized_users"]

async def add_auth_user(user_id: int):
    await auth_users_col.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def remove_auth_user(user_id: int):
    await auth_users_col.delete_one({"user_id": user_id})

async def is_user_authorized(user_id: int) -> bool:
    return await auth_users_col.find_one({"user_id": user_id}) is not None

async def get_all_user_ids() -> list[int]:
    cursor = auth_users_col.find({}, {"_id": 0, "user_id": 1})
    return [doc["user_id"] async for doc in cursor]