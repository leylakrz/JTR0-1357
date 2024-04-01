from sqlalchemy import text

from models import table_names_str
from resources.postgres.test_session import get_postgres_test_sync_session


def truncate_test_db():
    session = next(get_postgres_test_sync_session())
    query = text(f"TRUNCATE TABLE {table_names_str} CASCADE")
    session.execute(query)
    session.commit()
