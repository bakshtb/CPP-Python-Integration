# Set the minimum required version of CMake.
cmake_minimum_required(VERSION 3.13)

if(POLICY CMP0078)
  cmake_policy(SET CMP0078 NEW)
endif()

if(POLICY CMP0086)
  cmake_policy(SET CMP0086 NEW)
endif()

project(swig_integration)

# Set the build type to Release
set(CMAKE_BUILD_TYPE "Release")

# Find Python and SWIG.
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Find numpy
execute_process(
    COMMAND python3 -c "import numpy; print(numpy.get_include())"
    OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

include_directories(${NUMPY_INCLUDE_DIR})

# Define the source files for the project
set(src
    ../../shared/src/Circle.cpp
    ../../shared/src/Rectangle.cpp
    ../../shared/src/ShapeManager.cpp
    ../../shared/src/DataStreamExample.cpp
)

# Define the include files for the project
set(includes
    swig_integration.i
    ../../shared/include/Circle.h
    ../../shared/include/Rectangle.h
    ../../shared/include/ShapeManager.h
    ../../shared/include/DataStreamExample.h
    ../../shared/include/Shape.h
)

# Include directories
include_directories(${Python3_INCLUDE_DIRS} ${NUMPY_INCLUDE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/../../shared/include)

# Set the SWIG module name
set_property(SOURCE ${includes} PROPERTY SWIG_MODULE_NAME swig_integration)

# Set output directory for the generated files
set(CMAKE_SWIG_OUTDIR ${CMAKE_SOURCE_DIR}/../../libs)

# Generate the SWIG wrapper and build the shared library
set_source_files_properties(${includes} PROPERTIES CPLUSPLUS ON)
swig_add_library(swig_integration LANGUAGE python SOURCES ${src} ${includes})

# Link the SWIG-generated library to Python
swig_link_libraries(swig_integration Python3::Python)

# Set the output directory for the shared library (.so or .pyd)
set_target_properties(swig_integration PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../../libs
)

# Print Python version in green, if found
if(Python3_FOUND)
    # Define ANSI color escape codes
    string(ASCII 27 Esc)
    set(Green "${Esc}[32m")
    set(Red "${Esc}[31m")
    set(Reset "${Esc}[0m")

    # Print the Python version in green
    message("-- ${Green}${Bold}Python Found:${Reset} Python Version ${Python3_VERSION}")
else()
    # Print "Python3 not found" in red
    message("-- ${Red}Python3 not found${Reset}")
endif()
