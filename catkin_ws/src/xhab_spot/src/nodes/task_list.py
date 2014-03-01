#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String

class Task(object):
    def __init__(self, name, start_time):        
        self.name = name
        self.time = start_time

    def __hash__(self):
        return hash(self.name + "::" + str(self.time))

    def __eq__(self, other):
        return (self.name == other.name) and (self.time == other.time)


class TaskList(object):
    def __init__(self):
        self.pub = rospy.Publisher("spot_tasks", String)
        self.sub = rospy.Subscriber("scheduled_tasks", String, self.schedule_callback)
        rospy.init_node("TaskList")
        self.tasks = set()

    def schedule_callback(self, data):
        print "got a task from the scheduler:", data.data
        t = Task(data.data, time.time() + 15)
        self.tasks.add(t)

    def maybe_broadcast_task(self):
        if not self.tasks:
            print "No tasks to schedule at", time.time()
            return
        else:
            print "%d tasks in the queue" % len(self.tasks)

        ready_tasks = set()
        for task in self.tasks:
            now = time.time()
            if now > task.time:
                ready_tasks.add(task)
                print "Task '%s' is ready" % task.name
            else:
                print "Task '%s' is not due for another %.1f seconds" % (task.name, task.time - now)

        for task in ready_tasks:
            self.pub.publish(String("task: " + task.name))
            self.tasks.remove(task)
            print "Published task '%s'" % task.name

    def spin(self):
        while not rospy.is_shutdown():
            self.maybe_broadcast_task()
            time.sleep(1)

        print "rospy shut down!"
                

if __name__ == "__main__":
    try:
        t = TaskList()
        t.spin()
    except rospy.ROSInterruptException:
        pass
            
