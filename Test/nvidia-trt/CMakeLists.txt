cmake_minimum_required(VERSION 3.1.0)

project(nvidia-trt)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
if(CMAKE_VERSION VERSION_LESS "3.10.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()

# Enable OpenCV
find_package(OpenCV 4.2 REQUIRED)
#message(STATUS "OpenCV library status:")
#message(STATUS "    config: ${OpenCV_DIR}")
#message(STATUS "    version: ${OpenCV_VERSION}")
#message(STATUS "    libraries: ${OpenCV_LIBS}")
#message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# Enable TensorRT CXX
list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
find_package(TensorRT REQUIRED)
message("${TensorRT_LIBRARY}")

# Enable TensorRT Plugins: FUCK!
list(APPEND PLUGINS "nvinfer")
list(APPEND PLUGINS "nvonnxparser")
list(APPEND PLUGINS "nvparsers")
list(APPEND PLUGINS "nvinfer_plugin")
foreach(libName ${PLUGINS})
    find_library(${libName}_lib NAMES ${libName} "/usr" PATH_SUFFIXES lib)
    list(APPEND PLUGIN_LIBS "${${libName}_lib}")
endforeach()
message("${PLUGIN_LIBS}")

# Enable CUDA
find_package(CUDA REQUIRED)
message(STATUS "Found CUDA ${CUDA_VERSION_STRING} at ${CUDA_TOOLKIT_ROOT_DIR}")
# set(CUDA_NVCC_FLAGS "-gencode arch=compute_75,code=sm_75;-rdc=true;-use_fast_math")
include_directories(${CUDA_INCLUDE_DIRS})


file(GLOB common_src    "common/*.h"    "common/*.cpp")
# message("${common_src}")
include_directories("common")

# Add Executable
add_executable(testTRT
	${common_src}
	main.cpp)

target_link_libraries(testTRT ${OpenCV_LIBS} ${TensorRT_LIBRARY} ${CUDA_LIBRARIES} ${PLUGIN_LIBS})
