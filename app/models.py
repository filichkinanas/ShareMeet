from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from app import db


class Comments(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(256), index=True)
    contact: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    comment: so.Mapped[str] = so.mapped_column(sa.String(1000))
    create_date: so.Mapped[datetime] = so.mapped_column(default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Post {self.comment}'