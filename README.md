# Yolov5-ONNX

[made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

YOLOv5 inference using ONNX, with no complicated installations setup and zero precession loss!

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
