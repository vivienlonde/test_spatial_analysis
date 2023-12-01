import cv2

def extract_frame_from_time(time, video_path):
    frame = 24 * time
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    while success:
        if count == frame:
            cv2.imwrite("data/frame%d.jpg" % count, image)     # save frame as JPEG file    
        success, image = vidcap.read()
        count += 1

def extract_frames_from_interval(start, end, video_path, nb_frames):
    start_frame = 24 * start
    end_frame = 24 * end
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    length = end_frame - start_frame # nb of frames in the interval
    step = int(length/(nb_frames+1)) # nb of frames to skip
    while success:
        if count > start_frame and count < (end_frame - step/2) and (count - start_frame) % step == 0:
            cv2.imwrite("data/frame%d.jpg" % count, image)     # save frame as JPEG file    
        success, image = vidcap.read()
        count += 1


if __name__ == "__main__":

    extract_frame_from_time(3, 'data/videoRabbitOneMinute.mp4')
    # extract_frames_from_interval(2, 60, 'data/videoRabbitOneMinute.mp4', 10)