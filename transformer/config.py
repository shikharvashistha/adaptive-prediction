# This file is to define the configuration of the transformer model
# The configuration will be used to fuse multi sensor data using transformer model for trajectory prediction

import os


class TransformerConfig:
    """ Configuration of the transformer model """

    sensor_num = 3 # number of sensors
    sensor_dim = 3 # dimension of each sensor

    class_num = 7 # number of classes
    dropout = 0.5 # dropout rate
    
    class_list = [
        
    ]
