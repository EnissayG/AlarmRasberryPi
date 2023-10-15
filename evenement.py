class Evenement:
    def __init__(self, new_pin, new_temps) -> None:
        self._pin = new_pin
        self._temps = new_temps

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, new_pin):
        self._pin = new_pin

    @property
    def temps(self):
        return self._temps

    @temps.setter
    def temps(self, new_temps):
        self._temps = new_temps
