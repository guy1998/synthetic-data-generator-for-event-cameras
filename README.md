# Synthetic data generator for event cameras
I am providing this workflow for those that need a light weight option for generating synthetic data as opposed to traditional options such as V2E or ESIM. These platforms are great and I invite you to have a look at them. However, if you are like me and cannot get your hands on a very advanced setup that can support such high end platforms you could use this code snippet. 

<hr>

The code is pretty easy to understand. We can run the file <b>event_camera_sim.py</b> to generate the coordinates, timestamps and polarities of the events (movements) happing in a certain video which we can provide as an argument. The results are stored in a .txt file the path of which we can also specify as an argument. To run this file you can use the following command: <br>
```
python event_camera_sim.py input_video.avi --threshold 30 --output events.txt
```
Of course the output path can be chosen at your will. You can either use the .txt file which already contains the coordinate. Or you can run the <b>coordinates-to-video.py</b> to generate a synthetic data video. Make sure to update the path of the .txt on the line 5 of this file. To illustrate I am providing an example below using the video that features in the V2E tutorial. 

<br>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
  <img src="/media/image1.png" alt="Image 1" style="width: 200px; max-width: 200px;">
  <img src="/media/image2.png" alt="Image 2" style="width: 200px; max-width: 200px;">
  <img src="/media/image3.png" alt="Image 3" style="width: 200px; max-width: 200px;">
  <img src="/media/image4.png" alt="Image 4" style="width: 200px; max-width: 200px;">
  <img src="/media/image5.png" alt="Image 5" style="width: 200px; max-width: 200px;">
  <img src="/media/image6.png" alt="Image 6" style="width: 200px; max-width: 200px;">
  <img src="/media/image7.png" alt="Image 7" style="width: 200px; max-width: 200px;">
  <img src="/media/image8.png" alt="Image 8" style="width: 200px; max-width: 200px;">
</div>

<hr>

Do not forget to run check the <b>requirements.txt</b> for the libraries you need to have. Hope this code will help you with your work! Happy innovation!
