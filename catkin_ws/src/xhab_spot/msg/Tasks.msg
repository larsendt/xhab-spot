# possible values for type: battery, camera, curtain, ec, fan, humidity, lights, ph, pump, rotation, scheduler, temperature, water
string type

# possible values for spot_id: spot1, spot2, spot3, spot4
string spot_id

# if type == 'curtain'
bool curtain_open

# if type == 'fan'
bool fan_on

# if type == 'lights'
float32 light_intensity
bool reds_on
bool whites_on

# if type == 'pump'
bool pump_on
bool pump_temporary_disable

# if type == 'rotation'
float32 rotation_angle

# if type == 'scheduler'
# schedule_task can have the same values as 'type', except for 'scheduler'
string schedule_task
time schedule_time
