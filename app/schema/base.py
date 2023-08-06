from datetime import datetime

import ormar
import databases
import sqlalchemy

from app.internal.drivers.database import AsyncPg


naming_convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(all_column_names)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}
metadata = sqlalchemy.MetaData(naming_convention=naming_convention)
database = AsyncPg.database()


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
