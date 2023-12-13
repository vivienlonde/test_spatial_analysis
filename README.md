# Workflow


- search for interesting time interval in video (.mp4):
    - input : text search
    - output: time interval  
-> *video_retrieval.py*

- extract video from time interval:
    - input : time interval
    - output: frames (.jpg)  
-> *extract_frames.py*    

- analyse frame:
    - input : frame
    - output: captions, objects, bounding boxes, tags, ...  
-> *analyse_frame.py*

# Azure services requirement

- Azure Vision service : https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/

In a .env file, add the following variables:

```bash
AZURE_VISION_ENDPOINT=https://<your-custom-subdomain>.cognitiveservices.azure.com/
AZURE_VISION_KEY=<your-key>
``` 

- Azure storage

# Video input file

- Upload a video file (mp4) in Azure storage.  
-> input to *video_retrieval.py* (with SAS token)

- In a local data folder, add the same video file (mp4).    
Update filenames in *extract_frame.py*.  
-> input to *extract_frame.py*

- the output of *extract_frame.py* is the input of *image_analysis.py*.  
-> Update filenames accordingly.

