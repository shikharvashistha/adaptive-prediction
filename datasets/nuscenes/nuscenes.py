# This file will be used to load nuscene dataset, preprocess and
# get the map, camera, lidar, radar data and the corresponding labels
# divide the dataset into train, validation and test sets


import os
import numpy as np

from nuscenes.nuscenes import NuScenes

# Load the dataset
nusc = NuScenes(version='v1.0-trainval', dataroot='/home/nuScenes_data/nuScenes/v1.0-trainval', verbose=True)

# Get the train, validation and test set
class GetTrainingSet():
    """
    This class is used to get the training, validation and test set.
    """
    def __init__(self):
        self.train_set = []
        self.val_set = []
        self.test_set = []
        self.dataset = nusc
        self.get_training_set()
        self.get_validation_set()
        self.get_test_set()

    # Create a directory to store the training, validation and test set
    def create_dir(self):
        """
        Creates a directory to store the training, validation and test set.
        """

        os.makedirs('train', exist_ok=True)
        os.makedirs('val', exist_ok=True)
        os.makedirs('test', exist_ok=True)

    def divide_dataset(self):
        """
        Divides the dataset into training, validation and test set.
        """

        self.create_dir()
        for scene in self.dataset.scene:
            if scene['name'] in self.train_set:
                self.divide_scene(scene, 'train')
            elif scene['name'] in self.val_set:
                self.divide_scene(scene, 'val')
            elif scene['name'] in self.test_set:
                self.divide_scene(scene, 'test')

    def divide_scene(self, scene, split):
        """
        Divides the scene into training, validation and test set.

        Args:
            scene (dict): The scene to be divided.
            split (str): The split to which the scene belongs to.
        """

        os.makedirs(split + '/' + scene['name'], exist_ok=True)
        for sample_token in scene['first_sample_token']:
            self.divide_sample(sample_token, split)

    def divide_sample(self, sample_token, split):
        """
        Divides the sample into training, validation and test set.

        Args:
            sample_token (str): The sample token to be divided.
            split (str): The split to which the sample belongs to.
        """

        sample = self.dataset.get('sample', sample_token)
        self.divide_sample_data(sample['data'], split)
        self.divide_sample_annotation(sample['anns'], split)

    def divide_sample_data(self, sample_data, split):
        """
        Divides the sample data into training, validation and test set.

        Args:
            sample_data (list): The sample data to be divided.
            split (str): The split to which the sample data belongs to.
        """

        for data in sample_data:
            data_record = self.dataset.get('sample_data', data)
            self.dataset.get_sample_data_path(data_record['token'], 'train/' + data_record['filename'])

    def divide_sample_annotation(self, sample_annotation, split):
        """
        Divides the sample annotation into training, validation and test set.

        Args:
            sample_annotation (list): The sample annotation to be divided.
            split (str): The split to which the sample annotation belongs to.
        """

        for annotation in sample_annotation:
            annotation_record = self.dataset.get('sample_annotation', annotation)
            self.dataset.get_sample_data_path(annotation_record['token'], 'train/' + annotation_record['filename'])

        
        def divide_sensor_data(self, sensor_data, split):
            """
            Divides the sensor data into training, validation and test set.

            Args:
                sensor_data (list): The sensor data to be divided.
                split (str): The split to which the sensor data belongs to.
            """

            for data in sensor_data:
                data_record = self.dataset.get('sample_data', data)
                self.dataset.get_sample_data_path(data_record['token'], 'train/' + data_record['filename'])


            
    
    def get_training_set(self):
        """
        Returns a list of scene names that are part of the training set.

        Returns:
            list: A list of scene names that are part of the training set.
        """
        for scene in self.dataset.scene:
            if scene['name'] in self.dataset.train:
                self.train_set.append(scene['name'])

    def get_validation_set(self):

        for scene in self.dataset.scene:
            if scene['name'] in self.dataset.val:
                self.val_set.append(scene['name'])

    def get_test_set(self):
        for scene in self.dataset.scene:
            if scene['name'] in self.dataset.test:
                self.test_set.append(scene['name'])