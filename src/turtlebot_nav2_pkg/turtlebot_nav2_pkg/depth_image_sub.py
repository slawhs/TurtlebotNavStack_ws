#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan

import numpy as np

class DepthSub(Node):
    def __init__(self):
        super().__init__("DepthSub")
        self.depth_sub = self.create_subscription(Image, "/depth/image_raw", depth_cb 10)

    def depth_cb(self, Image):
        print(Image)


     