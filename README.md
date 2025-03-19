# Synthetic data generator for event cameras
I am providing this workflow for those that need a light weight option for generating synthetic data as opposed to traditional options such as V2E or ESIM. These platforms are great and I invite you to have a look at them. However, if you are like me and cannot get your hands on a very advanced setup that can support such high end platforms you could use this code snippet. 
<hr>
The code is pretty easy to understand. We can run the file <b>event_camera_sim.py</b> to generate the coordinates, timestamps and polarities of the events (movements) happing in a certain video which we can provide as an argument. The results are stored in a .txt file the path of which we can also specify as an argument. To run this file you can use the following command: <br>
```
python event_camera_sim.py input_video.avi --threshold 30 --output events.txt
```
