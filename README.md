Simple frame extractor for video dataset
=======================================

[notice]
--------------
-2020.09.22
My Dataset is 2.33Tb. Using OpenCV is too slow. 
So I use ffmpeg instead. you need to install below 

    pip install ffmpeg


-2020.09.19

This is simple frame extractor 

I use it for our lab's dataset but this is not public yet.

So I tested on one of the famouse and light benchmark dataset for human action recognition (HMDB-51 dataset). 

https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/#Downloads

And it worked well.

FPS option will be added soon

[how to use]
---------------

If you follow the details below, the extractor will work on any dataset.

input format :

    The dataset must be in one folder.

output foramt : 

    output folder will be generated like this.
    destination_dir/video_name/frame000001.jpg 
    
    If you want to create a folder by label, just change this code line in extract_frame()
    
        if not(os.path.isdir(dst+label+video_name)):
            os.makedirs(os.path.join(dst+label+video_name))
        cv2.imwrite(dst+label+video_name+"\\"+fr_name,image)
    
![캡처](output.PNG)

