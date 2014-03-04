# possible values for type: battery, camera, curtain, ec, fan, humidity, lights, ph, pump, rotation, scheduler, temperature, water
string type

# possible values for spot_id: spot1, spot2, spot3, spot4
string spot_id

# timestamp!
time timestamp

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

# scheduler options - the validity of these depends on the value of 'schedule_task'
bool sched_curtain_open
bool sched_fan_on
bool sched_lights_white_on
bool sched_lights_red_on
float32 sched_lights_brightness # 0-1 range
bool sched_pump_on
bool sched_pump_temporary_disable
float32 sched_pump_temporary_disable_time
float32 sched_rotation_angle

