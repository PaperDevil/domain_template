from logging.config import fileConfig

from sqlalchemy import create_engine
from alembic import context

from app.schema.base import *
from app.schema.models import *
from app.conf.database import get_db_url

config = context.config
fileConfig(config.config_file_name)
target_metadata = metadata


def run_migrations_offline():
    context.configure(
        url=get_db_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(get_db_url())
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
