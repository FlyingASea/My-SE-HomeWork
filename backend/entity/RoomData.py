from main import db


class RoomData(db.Model):
    id = db.Column("id", db.String(80), primary_key=True, nullable=False)
    temperature = db.Column("temperature", db.String(255), nullable=False)
    wind_speed = db.Column("wind_speed", db.String(255), nullable=False)
    mode = db.Column("mode", db.String(255), nullable=False)
    sweep = db.Column("sweep", db.String(255), nullable=False)
    is_on = db.Column("is_on", db.String(255), nullable=False)
    last_update = db.Column("last_update", db.String(255), nullable=False)

    def __init__(self, id, temperature, wind_speed, mode, sweep, is_on, last_update):
        self.id = id
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.mode = mode
        self.sweep = sweep
        self.is_on = is_on
        self.last_update = last_update

    def setTemperature(self, temperature):
        self.temperature = temperature

    def setWindSpeed(self, wind_speed):
        self.wind_speed = wind_speed

    def setMode(self, mode):
        self.mode = mode

    def setSweep(self, sweep):
        self.sweep = sweep

    def setIsOn(self, is_on):
        self.is_on = is_on

    def setLastUpdate(self, last_update):
        self.last_update = last_update
