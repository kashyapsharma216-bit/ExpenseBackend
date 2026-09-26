# db.py
from motor.motor_asyncio import AsyncIOMotorClient

mongoURL = "mongodb+srv://Tirth27:admin@cluster0.g8flz10.mongodb.net/?appName=Cluster0"

client = AsyncIOMotorClient(mongoURL, tls=True,
    tlsAllowInvalidCertificates=True)

database = client["ExpenseDB"]

user_collection = database["users"]
expense_collection = database["expenses"]
