cmake_minimum_required(VERSION 3.1.0)

project(nvidia-jetson)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
if(CMAKE_VERSION VERSION_LESS "3.10.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()

# Enable OpenCV
find_package(OpenCV 4.1 REQUIRED)
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# Add Executable
add_executable(testIPCam
	testIPCam.cpp
)

target_link_libraries(testIPCam ${OpenCV_LIBS})
