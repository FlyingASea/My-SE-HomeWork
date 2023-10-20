import json
import time

from entity.RoomEntity import Room
from main import db
from service.AdministrateService import getRoomById
from service.SHA256withRSA import verifyWithPkcs1Pss


def certificateData(data):
    room = getRoomById(data['room'])
    key = room.public_key
    sign_text = data['room'] + data['operation'] + data['time'] + data['unique_id']
    signature = data['signature']
    return verifyWithPkcs1Pss(sign_text=sign_text, sign=signature, key=key)


def EntryToData(data):
    tempData = {'room': data['room']}
    return tempData


def recordRoomData(data):
    if not certificateData(data):
        return None

    data = EntryToData(data)

    Room.query.filter(Room.id == data['id']).update({'temperature': data['temperature'],
                                                     'wind_speed': data['wind_speed'], 'mode': data['mode'],
                                                     'sweep': data['sweep'], 'is_on': data['is_on'],
                                                     'last_update': str(
                                                         time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime()))})

    db.session.commit()
    return json.dumps({})
