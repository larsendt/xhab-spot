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
    /data/spotX/curtain
    /data/spotX/ec
    /data/spotX/fan
    /data/spoyX/humidity
    /data/spotX/lights
    /data/spotX/ph
    /data/spotX/pump
    /data/spotX/rotation
    /data/spotX/temperature
    /data/spotX/water

For the task topics:

    /tasks/spotX/battery
    /tasks/spotX/camera
    /tasks/spotX/curtain
    /tasks/spotX/ec
    /tasks/spotX/fan
    /tasks/spotX/humidity
    /tasks/spotX/lights
    /tasks/spotX/ph
    /tasks/spotX/pump
    /tasks/spotX/rotation
    /tasks/spotX/temperature
    /tasks/spotX/water

The alerts have not been completely defined yet, so this section may change.
    
    /alerts/spotX/


## Messages

The messages can be found in the `xhab-spot` repo under:

    catkin_ws/src/xhab_spot/msg/

