# SPOT Topics

## Conventions

* always lower case, even with things like pH (would be ph)
* use underscores instead of spaces

## Topic format

There are three top level topics:

    /data
    /tasks
    /alerts

Underneath each of those is the SPOT ID

    /data/spot1
    /data/spot2
    ...
    /tasks/spot1
    ...
    /alerts/spot1
    ...

For the data topics, we have the following (where X is 1-4).
This list should be exhaustive. If something is missing, let
Dane know, or add it yourself. 

    /data/spotX/battery
    /data/spotX/camera
    /data/spotX/door
    /data/spotX/ec
    /data/spotX/fan
    /data/spoyX/humidity
    /data/spotX/lights
    /data/spotX/ph
    /data/spotX/pump
    /data/spotX/rotation
    /data/spotX/air_temperature
    /data/spotX/water_temperature
    /data/spotX/water_level
    /data/spotX/valve

For the task topics:

    /tasks/spotX/battery
    /tasks/spotX/camera
    /tasks/spotX/door
    /tasks/spotX/ec
    /tasks/spotX/fan
    /tasks/spotX/humidity
    /tasks/spotX/lights
    /tasks/spotX/ph
    /tasks/spotX/pump
    /tasks/spotX/rotation
    /tasks/spotX/air_temperature
    /tasks/spotX/water_temperature
    /tasks/spotX/water_level
    /tasks/spotX/valve

The alerts have not been completely defined yet, so this section may change.
    
    /alerts/spotX/


## Messages

The messages can be found in the `xhab-spot` repo under:

    catkin_ws/src/xhab_spot/msg/

There are Task messages for each task topic, but Data and Alerts only have one message each (with the exception of CameraData.msg):

Data.msg looks like the following:

    string source
    string property
    time timestamp
    float32 value

`source` is one of `spot1`, `spot2`, `spot3`, `spot4` or `rogr`
For `value`, booleans should be stored as 1.0 and 0.0
`property` can be one of the following (again, if any are missing, feel free to add them)

    battery_charging
    battery_level
    battery_full
    door_status
    ec_reading
    fan_on
    humidity_reading
    lights_brightness
    lights_whites_on
    lights_reds_on
    ph_reading
    pump_on
    rotation_angle
    air_temperature
    water_temperature
    water_level
    valve_status

Note that camera is missing from this list. It has its own message: CameraData.msg



