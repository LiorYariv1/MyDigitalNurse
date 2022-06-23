import sys
import argparse
import os
import cv2

def extractImages(pathIn, pathOut, camera_name):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    while success:
        cv2.imwrite(pathOut + f"/{count}_{camera_name}.jpg", image)  # save frame as JPEG file
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count = count + 1


if __name__ == "__main__":
    avis_path = '/data/shared-data/scalpel/kristina/Algs/YOLOV5/data/video/video as avi'
    dest_path = '/data/shared-data/scalpel/MyDigitalNurse2/all_data'
    videos = os.listdir(avis_path)

    for sur in videos:
        sur_name = sur.split('.')[0]
        sur_path  = os.path.join(dest_path,sur_name)
        os.makedirs(sur_path,exist_ok=True)
        camera_name = 1 if sur.split('.')[1]=='Camera1' else 2
        extractImages(os.path.join(avis_path,sur),sur_path, camera_name)
