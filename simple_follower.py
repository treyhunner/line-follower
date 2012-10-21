DEFINE LIGHT_THRESHOLD=35
DEFINE LIGHT_SENSOR=IN_3
DEFINE SENSOR_COLOR=0x0E


def sensor_on():
    """Enable light sensor and turn on red light"""
    SetSensorLight(LIGHT_SENSOR)
    SetSensorType(LIGHT_SENSOR, SENSOR_COLOR)
    SetSensorMode(LIGHT_SENSOR, IN_MODE_PCTFULLSCALE)
    ResetSensor(LIGHT_SENSOR)


def get_sensor():
    """Return value of light sensor"""
    s = Sensor(IN_3)
    return s


def turn_on_black():
    """Turn because we've seen black"""
    OnRev(OUT_B, 50)
    Off(OUT_C)


def turn_on_white():
    """Turn because we've seen white"""
    OnRev(OUT_C, 50)
    Off(OUT_B)


def main():
    sensor_on()
    turn_on_black()
    while True:
        NumOut(60, LCD_LINE1, Sensor(IN_3))
        if Sensor(IN_3) > LIGHT_THRESHOLD:
            turn_on_white()
            Wait(10)
        else:
            turn_on_black()
        ClearScreen()
