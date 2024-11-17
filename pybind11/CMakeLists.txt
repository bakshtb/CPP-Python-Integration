cmake_minimum_required(VERSION 3.0)
project(cpp_wrapper)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

include_directories(../include)

add_library(cpp_wrapper MODULE
    bindings.cpp
    ../src/Circle.cpp
    ../src/Rectangle.cpp
    ../src/ShapeManager.cpp
    ../src/DataStreamExample.cpp
)

target_link_libraries(cpp_wrapper PRIVATE pybind11::module)

# Set Python module install location to the root folder
set_target_properties(cpp_wrapper PROPERTIES
    PREFIX ""  # Remove the default "lib" prefix for shared libraries
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/../"  # Output to the root directory
)

# Set Python module output name (optional)
set_target_properties(cpp_wrapper PROPERTIES
    OUTPUT_NAME "cpp_wrapper"
)

# Enable C++14 (or higher if necessary)
target_compile_features(cpp_wrapper PRIVATE cxx_std_14)
