FFMPEG configuration:
--enable-cuda-nvcc --enable-cuvid --enable-nvenc --enable-nonfree --enable-libnpp --enable-pic --enable-shared --extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64

QT5 configuration:
./configure -opensource -confirm-license -nomake examples -nomake tests -sqlite -skip webengine -skip multimedia -skip tools -skip sensors -skip networkauth -skip purchasing -silent

OPENCV build with CUDA CODEC:
...

Installation packages:
- QT5default + QTcreator
- Cuda 10.1 (deb)
- TensorRT 6 (deb) (bonus cudnn7)

Communication modules:
- OpenCV with CUDA and NVCODEC
- MQTT & MONGODB (CXX)
- MAVSDK

Problems:
- WTH with FFMPEG default + NVCodec?

References:
- https://github.com/onnx/onnx-tensorrt
- https://github.com/NVIDIA-AI-IOT/torch2trt
- https://github.com/NVIDIA/TensorRT/tree/release/7.0/samples
- https://github.com/NVIDIA/tensorrt-laboratory
- https://docs.nvidia.com/deeplearning/sdk/tensorrt-developer-guide/index.html
