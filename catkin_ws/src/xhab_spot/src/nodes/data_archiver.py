#!/usr/bin/env python
import rospy
import time
import sqlite3
import os
from std_msgs.msg import String
import spot_topics
import identity

DB_DIR = "/home/xhab/data"
DB_FILE = os.path.join(DB_DIR, "archive.sqlite")

def init_database():
    print "initializing database:", DB_FILE
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS spot_archive (source TEXT, property TEXT, timestamp INTEGER, value REAL)")
    conn.commit()
    conn.close()

def insert_data(source, prop, timestamp, value):
    values = (source, prop, timestamp.secs, value)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO spot_archive VALUES (?,?,?,?)", values)
    conn.commit()
    conn.close()

def store_latest(prop, value):
    path = "/home/xhab/data/" + prop + ".txt"
    with open(path, "w") as f:
        f.write(str(value) + "\n")
    print "Wrote %.1f to %s" % (value, path)

def init_latest_files():
    for prop in spot_topics.PROPERTIES:
        store_latest(prop, 0.0)

class DataArchiver(object):
    def __init__(self):
        print "DataArchiver init"
        init_database()
        rospy.init_node("DataArchiver")
        subtopic = "/data/" + identity.get_spot_name() 
        self.subscribers = spot_topics.make_data_subscribers(subtopic, self.data_callback) 
        init_latest_files()

    def data_callback(self, message):
        print "archiver got:", message.source, message.property
        insert_data(message.source, message.property, message.timestamp, message.value)
        store_latest(message.property, message.value)
        print "inserted data"

    def spin(self):
        print "DataArchiver listening"
        rospy.spin()

if __name__ == "__main__":
    try:
        d = DataArchiver()
        d.spin()
    except rospy.ROSInterruptException:
        pass
            
