cmake_minimum_required(VERSION 3.1.0)

project(mosquittopp-test)

list(APPEND CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake")

find_package(Mosquitto)
if(MOSQUITTO_FOUND)
  include_directories(${MOSQUITTO_INCLUDE_DIRS})
#  target_link_libraries (${PROJECT_NAME} ${MOSQUITTO_LIBRARIES})
endif (MOSQUITTO_FOUND)

find_package(Mosquittopp)
if(MOSQUITTOPP_FOUND)
  include_directories(${MOSQUITTOPP_INCLUDE_DIRS})
#  target_link_libraries (${PROJECT_NAME} ${MOSQUITTOPP_LIBRARIES})
endif (MOSQUITTOPP_FOUND)

# Add Executable
add_executable(test_cplus	test_cplus.cpp  temperature_conversion.h  temperature_conversion.cpp)
target_link_libraries(test_cplus ${MOSQUITTOPP_LIBRARIES})


