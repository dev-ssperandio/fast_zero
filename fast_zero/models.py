from datetime import datetime
from sqlalchemy.orm import registry

table_registry = registry()


class User:
    id: int
    username: str
    password: str
    email: str
    created_at: datetime
