I have used a simple approach for finding whether the face has blood or not.

FIrst use face detection to crop the part of image other than face.(face_detect.py)
then using python red_level.py to detect the amount  of red in the image

if amount of red is greater then threshold then we say that Image has blood 

Run the code like this:
```console
$ python face_detect.py
$ python red_level.py
```
