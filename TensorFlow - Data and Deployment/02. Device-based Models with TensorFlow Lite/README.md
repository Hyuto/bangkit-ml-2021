# Device-based Models with TensorFlow Lite

## Materi

* Week 1<br>
  1. Course Introduction
  2. Machine Learning Models in Mobile and Embedded Systems
  3. Taking a look at the saved model format
  4. First primer on running models on mobile devices
   
   **Note**

   1. [GPU delegates](https://www.youtube.com/watch?v=QSbAUxWfxQw)
   2. [Supported ops](https://www.tensorflow.org/lite/guide/ops_compatibility) and [TF-Select](https://www.tensorflow.org/lite/guide/ops_select)
   
   **Example**

   1. [Running TFLite models](Week%201/Examples/01.%20Running%20TFLite%20models.ipynb)
   2. [Transfer Learning with TensorFlow Hub for TFLite](Week%201/Examples/02.%20Transfer%20Learning%20with%20TensorFlow%20Hub%20for%20TFLite.ipynb)
   
   **Assessments**

   1. [Quiz - Week 1 Quiz](Assessment/Week_1_Quizz.md)
   2. [Lab - Train Your Own Model and Convert It to TFLite](Week%201/Train%20Your%20Own%20Model%20and%20Convert%20It%20to%20TFLite.ipynb)
* Week 2<br>
  1. Basic image classification
  2. Classifying camera images
  3. Code walkthrough - camera image classifier
  4. Object detection
  5. Code walkthrough of an object detection app
   
   **Note**

   1. [Android fundamentals](https://developer.android.com/courses) and [installation](https://developer.android.com/studio)
   
   **Example**

   1. [Cat vs Dog App](Week%202/Example/cats_vs_dogs)
   2. [Image Classification](Week%202/Exampleimage_classification)
   3. [Object Detection](Week%202/Example/object_detection)
   
   **Assessment** : [Quiz - Week 2 Quiz](Assessment/Week_2_Quizz.md)
* Week 3<br>
  1. Next steps
  2. Classification and detection
   
   **Note**

   1. [Apple’s developer's site](https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e)
   2. [Apple's API](https://developer.apple.com/documentation/accelerate/vimage)
   3. [Camera related functionalities](https://developer.apple.com/documentation/avfoundation/cameras_and_media_capture/avcam_building_a_camera_app)
   4. [VImage](https://developer.apple.com/documentation/accelerate/vimage)
   5. [Coco dataset](https://github.com/tensorflow/models/tree/master/research/object_detection)
   
   **Example**

   1. [Cat vs Dog App](Week%203/Example/cats_vs_dogs)
   2. [Image Classification](Week%203/Exampleimage_classification)
   3. [Object Detection](Week%203/Example/object_detection)
   
   **Assessment** : [Quiz - Week 3 Quiz](Assessment/Week_3_Quizz.md)
* Week 4<br>
  1. Example: Raspberry Pi
  2. Raspberry pi demo
  3. Microcontrollers
   
   **Note**

   1. Options to choose from
      * [Source for the RPI](https://www.tensorflow.org/install/source_rpi)
      * [Working on a virtual environment](https://www.tensorflow.org/install/pip)
      * [TF interpreter](https://www.tensorflow.org/lite/guide/python)
   2. [Pre optimized mobileNet](https://www.tensorflow.org/lite/models/image_classification/overview)
   3. [Object detection model trained on the coco](http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip)
   4. Further readings
      * [Sparkfun 15170](https://www.sparkfun.com/products/15170)
      * [Sparkfun 15096](https://www.sparkfun.com/products/15096)
      * [Sparkfun colab](https://codelabs.developers.google.com/codelabs/sparkfun-tensorflow/)
      * [TF on different microcontrollers](https://www.tensorflow.org/lite/microcontrollers/get_started)

   **Example**

   1. [Image Classification](Week%204/Example/image_classification)
   2. [Object Detection](Week%204/Example/object_detection)
   3. [Transfer Learning](Week%204/Example/transfer_learning)
   4. [Hyperparameter Tuning](Week%204/Example/hyperparameter_tuning)
   
   **Assessment** : [Quiz - Week 4 Quiz](Assessment/Week_4_Quizz.md)