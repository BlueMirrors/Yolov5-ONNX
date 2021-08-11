# Yolov5-ONNX

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1h2Nv9DA4X0bgCnoF0nCVEwKAatptezNk?usp=sharing)

YOLOv5 inference using ONNX, with no complicated installations setup and zero precession loss!

- [Google-Colab](https://colab.research.google.com/drive/1h2Nv9DA4X0bgCnoF0nCVEwKAatptezNk?usp=sharing)

- [FPS-Accuracy-CPU](#fps-and-accuracy-info-cpu)

- [FPS-Accuracy-GPU](#fps-and-accuracy-info-gpu)

## Inference with ONNX

Tested with Linux based systems (Colab T4/P4/K80, AWS t2.micro (Intel Xeon), Ubuntu-GTX 1650)

```bash
$ git clone https://github.com/BlueMirrors/Yolov5-ONNX.git
$ cd Yolov5-ONNX
$ pip install -r requirements.txt
```

Now run inference on video or image file (with pretrained weights).

```bash
python detect.py --input $PATH_TO_INPUT_FILE --output $OUTPUT_FILE_NAME
```

<br>

You can also pass ```--weights``` to use your own custom onnx weight file.

For pretrained default weights (```--weights yolov5s```), scripts will download the weights file automatically. 

## Convert to ONNX

If you want to run the inference for your custom weights, simply do the following:

- [Train Yolov5 on your custom dataset](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)
- [Export Weights PyTorch weights to ONNX](https://github.com/ultralytics/yolov5/blob/master/export.py)

Make sure you use the `---dynamic` flag while exporting your custom weights.

```bash
python export.py --weights $PATH_TO_PYTORCH_WEIGHTS --dynamic --include onnx
```
<br> 

## FPS and Accuracy Info (CPU)
***In our tests, ONNX had identical outputs as original pytorch weights.***

Based on 500-700 inference iterations after 50 iterations of warmups. Includes Image Preprocessing (letterboxing etc.), Model Inference and Output Postprocessing (NMS, Scale-Coords, etc.) time only.  

| Hardware    | FPS     |
| ---------- | ------- |
| AWS T2.Micro   | 5.0-5.5 |
| Colab-CPU Runtime (Intel(R) Xeon(R) CPU @ 2.20GHz) | 5.1-5.7|
| MacBook Pro (13-inch, 2016, Four Thunderbolt 3 Ports) Processor: 2.9 GHz Intel Core i5 | 10-11 | 

<br> 

## FPS and Accuracy Info (GPU)
***In our tests, ONNX had identical outputs as original pytorch weights.***

Based on 5000 inference iterations after 100 iterations of warmups. Includes Image Preprocessing (letterboxing etc.), Model Inference and Output Postprocessing (NMS, Scale-Coords, etc.) time only.  

| Hardware    | FPS     |
| ---------- | ------- |
| T4   | 83-89 |
| P4   | 62-65 |
| K80 | 31-34 | 

<br>

## Notes
- Batch support will be added next week (after 15th August)


## References
- [Yolov5](https://github.com/ultralytics/yolov5)
- [CVU](https://github.com/BlueMirrors/cvu)
