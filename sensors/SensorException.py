class SensorError(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class SensorReadError(SensorError):
    """
    When something happens with the sensor.
    """

    def __init__(self, message):
        pass

    @property
    def message(self):
        return self.__message

    def get_message(self):
        return self.__message