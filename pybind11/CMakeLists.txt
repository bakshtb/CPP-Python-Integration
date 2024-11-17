cmake_minimum_required(VERSION 3.0)
project(datastream_example)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

include_directories(../include)

add_library(datastream_example MODULE
    bindings.cpp
    ../src/Circle.cpp
    ../src/Rectangle.cpp
    ../src/ShapeManager.cpp
    ../src/DataStreamExample.cpp
)

target_link_libraries(datastream_example PRIVATE pybind11::module)

# Set Python module install location to the root folder
set_target_properties(datastream_example PROPERTIES
    PREFIX ""  # Remove the default "lib" prefix for shared libraries
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/../"  # Output to the root directory
)

# Set Python module output name (optional)
set_target_properties(datastream_example PROPERTIES
    OUTPUT_NAME "datastream_example"
)

# Enable C++14 (or higher if necessary)
target_compile_features(datastream_example PRIVATE cxx_std_14)