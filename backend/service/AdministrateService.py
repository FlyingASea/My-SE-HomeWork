import json

from backend.entity.RoomEntity import Room
from backend.main import db


def getRoomById(id):
    result = Room.query.filter_by(id=id).first()
    if result is None:
        return None
    else:
        return result


def newRoom(id, public_key):
    try:
        room = Room(id=id, public_key=public_key)
        db.session.add(room)
        db.session.commit()
        return True
    except Exception:
        return False


def delRoomById(id):
    try:
        Room.query.filter_by(id=id).delete()
        db.session.commit()
    except Exception:
        return False


def getAllRoomId():
    try:
        result = Room.query.with_entities(Room.id).all()
        res = []
        for row in result:
            print(row)
            step = {'id': row[0]}
            res.append(step)
        return json.dumps(res)
    except Exception:
        return None


def checkInRoom(room):
    result = room


def checkOutRoom(room):
    result = room
