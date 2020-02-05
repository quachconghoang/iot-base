cmake_minimum_required(VERSION 3.1.0)

project(MultiCamera)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
IF(NOT APPLE AND NOT MSVC)
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")
ENDIF()

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

# Enable TensorRT CXX
# list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")
# find_package(TensorRT REQUIRED)

# Add Executable
add_executable(multistream
	multistream.cpp
    VideosManager.cpp VideosManager.h VideoSession.cpp VideoSession.h)

target_link_libraries(multistream ${OpenCV_LIBS})
