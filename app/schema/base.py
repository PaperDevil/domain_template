import ormar
import sqlalchemy
import databases

from datetime import datetime

from app.conf.database import get_db_url


metadata = sqlalchemy.MetaData()
database = databases.Database(get_db_url())


class BaseModel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        abstract = True

    id: int = ormar.Integer(primary_key=True)
    created_at: datetime = ormar.DateTime(default=datetime.now)
    updated_at: datetime = ormar.DateTime(default=datetime.now)

    async def save(self):
        self.updated_at = datetime.now()
        return await super().save()
