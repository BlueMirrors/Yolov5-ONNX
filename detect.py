import argparse
import os
import time
import numpy as np
import cv2
from cvu.detector.yolov5 import Yolov5 as Yolov5Onnx
from vidsz.opencv import Reader, Writer
from cvu.utils.google_utils import gdrive_download


def detect_video(device, weight, input_video, output_video=None):
    model = Yolov5Onnx(classes="coco",
                       backend="onnx",
                       weight=weight,
                       device=device)
    reader = Reader(input_video)
    writer = Writer(reader,
                    name=output_video) if output_video is not None else None

    # warmup
    warmup = np.random.randint(0, 255, reader.read().shape).astype("float")
    for i in range(100):
        model(warmup)

    inference_time = 0
    for frame in reader:
        # inference
        start = time.time()
        preds = model(frame)
        inference_time += time.time() - start

        # draw on frame
        if writer is not None:
            preds.draw(frame)
            writer.write(frame)

    print("\nModel Inference FPS: ",
          round(reader.frame_count / inference_time, 3))
    print("Output Video Saved at: ", writer.name)
    writer.release()
    reader.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights',
                        type=str,
                        default='yolov5s',
                        help='onnx weights path')

    parser.add_argument('--input',
                        type=str,
                        default='people.mp4',
                        help='path to input video or image file')

    parser.add_argument('--output',
                        type=str,
                        default='people_out.mp4',
                        help='name of output video or image file')

    parser.add_argument('--device', type=str, default='cpu', help='cpu or gpu')

    opt = parser.parse_args()

    if not os.path.exists(opt.input) and opt.input == 'people.mp4':
        gdrive_download("1rioaBCzP9S31DYVh-tHplQ3cgvgoBpNJ", "people.mp4")
        detect_video(opt.device, opt.weights, opt.input, opt.output)
