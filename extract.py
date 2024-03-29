### https://github.com/khm159/simple_frame_extractor_for_video_dataset
### originally codded by https://github.com/khm159

import os
import cv2
import argparse
from tqdm import tqdm

dataset_path = "YOUR_DATASET_PATH" #dataset directory 
dst = "FRAME_DIR_DST_PATH"

## argparser 
parser = argparse.ArgumentParser()
parser.add_argument('--fps', required=True, help='set sampling rate')
args = parser.parse_args()
fps = args.fps

def main(path):
    print("Searching video clips... ")
    video_list, dir_list = search(path)
    print(len(dir_list),"label, ",len(video_list)," video clips founded!", )
    print("Extracting Video frames...")
    for vid in tqdm(video_list):
        _ = vid.split("/")
        name = _[-1]
        label = _[-2]
        tgt_path = os.path.isdir(dst,name)
        if not(tgt_path):
            os.makedirs(tgt_path)
        os.system("ffmpeg -i "+vid+" "+"-r "+str(fps)+" "+ "-start_number 1 "+tgt_path+"/frame%6d.jpg")

def extract_frame(video_path, video_name, label, dst):
    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        if success == False:
            break
        fr_name = "frame"+str(count).zfill(6)+".jpg"
        if not(os.path.isdir(dst+label+video_name)):
            os.makedirs(os.path.join(dst+label+video_name))
        cv2.imwrite(dst+label+video_name+"\\"+fr_name,image)
        count += 1
    
def search(path):
    video_list = []
    dir_list = []
    file_list = os.listdir(path)

    for f in file_list:
        nextfile = os.path.join(path,f)

        if os.path.isdir(nextfile):
            dir_list.append(nextfile)
            _v ,_d = search(nextfile)
            video_list += _v
            dir_list += _d
            
        else:
            video_list.append(nextfile)
            
    return video_list, dir_list        

if __name__=="__main__"():
    main(dataset_path)

