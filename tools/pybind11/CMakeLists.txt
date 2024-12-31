cmake_minimum_required(VERSION 3.0)
project(pybind11_integration)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

include_directories(../../shared/include)

add_library(pybind11_integration MODULE
    bindings.cpp
    ../../shared/src/Circle.cpp
    ../../shared/src/Rectangle.cpp
    ../../shared/src/ShapeManager.cpp
    ../../shared/src/DataStreamExample.cpp
)

target_link_libraries(pybind11_integration PRIVATE pybind11::module)

set(LIBRARY_DESTINATION "${CMAKE_SOURCE_DIR}/../../libs")
message(STATUS "Libraries will be stored in: ${LIBRARY_DESTINATION}")

# Set Python module install location to the root folder
set_target_properties(pybind11_integration PROPERTIES
    PREFIX ""  # Remove the default "lib" prefix for shared libraries
    LIBRARY_OUTPUT_DIRECTORY ${LIBRARY_DESTINATION}
    SUFFIX ".so"                   # Shared library suffix
)

# Enable C++14 (or higher if necessary)
target_compile_features(pybind11_integration PRIVATE cxx_std_14)
