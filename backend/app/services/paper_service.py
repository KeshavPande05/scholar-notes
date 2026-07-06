from datetime import datetime

from app.db.database import db
from app.models.paper import create_paper_document


class PaperService:

    @staticmethod
    async def get_all():
        return await db.papers.find({}, {"_id": 0}).to_list(100)

    @staticmethod
    async def get_by_id(paper_id: str):
        return await db.papers.find_one(
            {"id": paper_id},
            {"_id": 0},
        )

    @staticmethod
    async def create(data: dict):
        paper = create_paper_document(data)

        result = await db.papers.insert_one(paper)

        return await db.papers.find_one(
            {"_id": result.inserted_id},
            {"_id": 0},
        )

    @staticmethod
    async def update(paper_id: str, data: dict):

        data["updated_at"] = datetime.utcnow()

        await db.papers.update_one(
            {"id": paper_id},
            {"$set": data},
        )

        return await db.papers.find_one(
            {"id": paper_id},
            {"_id": 0},
        )

    @staticmethod
    async def delete(paper_id: str):

        result = await db.papers.delete_one({"id": paper_id})

        return result.deleted_count > 0
