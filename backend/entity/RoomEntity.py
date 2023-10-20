from backend.main import db


class RoomEntity(db.Model):
    id = db.Column("id", db.String(80), primary_key=True, nullable=False)
    public_key = db.Column("public_key", db.String(255), nullable=False)

    def __init__(self, id, public_key):
        self.id = id
        self.public_key = public_key