QT5 configuration:
./configure -opensource \
-confirm-license \
-nomake examples \
-nomake tests \
-sqlite \
-skip webengine \
-skip webchannel \
-skip websockets \
-skip webview \
-skip wayland \
-skip winextras \
-skip multimedia \
-skip sensors \
-skip networkauth \
-skip purchasing \
-silent

OPENCV build with CUDA CODEC:
cmake ../ (sth else but gstreamer seem fucking delay)

Installation packages:
- QT5default + QTcreator
- Cuda 10.1 (deb)
- TensorRT 6 (deb) (bonus cudnn7)

Communication modules:
- OpenCV with CUDA and NVCODEC
- MQTT & MONGODB (CXX)
- MAVSDK

Problems:
- WTH with FFMPEG default + NVCodec -> OK!

FFMPEG configuration:
./configure --enable-cuda-nvcc \
--enable-cuvid \
--enable-nvenc \
--enable-nonfree \
--enable-libnpp \
--enable-pic \
--enable-shared \
--extra-cflags=-I/usr/local/cuda/include \
--extra-ldflags=-L/usr/local/cuda/lib64

DeepStream:
- https://docs.nvidia.com/metropolis/deepstream/dev-guide/index.html
- https://www.deeplearning-blog.com/2020/02/03/how-to-detect-objects-with-nvidia-deepstream-4-0-and-yolo-in-5-minutes/
- https://www.deeplearning-blog.com/2020/02/11/video-optical-flow-using-nvidia-deepstream-4-0/

References:
- https://github.com/onnx/onnx-tensorrt
- https://github.com/NVIDIA-AI-IOT/torch2trt
- https://github.com/NVIDIA/TensorRT/tree/release/7.0/samples
- https://github.com/NVIDIA/tensorrt-laboratory
- https://docs.nvidia.com/deeplearning/sdk/tensorrt-developer-guide/index.html
