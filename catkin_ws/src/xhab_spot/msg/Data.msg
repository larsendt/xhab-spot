# type can be one of: battery, camera, curtain, ec, fan, humidity, lights, ph, pump, rotation, temperature, water
string type
time timestamp

# if type == 'battery'
bool battery_charging
float32 battery_level

# if type == 'camera'
string camera_encoding = JPG
uint8[] camera_data

# if type == 'curtain'
bool curtain_open

# if type == 'ec'
float32 ec_value

# if type == 'fan'
bool fan_on

# if type == 'humidity'
float32 humidity_value

# if type == 'lights'
float32 lights_value
bool lights_red_on
bool lights_white_on

# if type == 'ph'
float32 ph_value

# if type == 'pump'
bool pump_on
bool pump_temporarily_disabled

# if type == 'rotation'
float32 rotation_angle

# if type == 'temperature'
float32 temperature_value

# if type == 'water'
float32 water_level_value
