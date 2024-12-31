# Set the minimum required version of CMake.
cmake_minimum_required(VERSION 3.13)

if(POLICY CMP0078)
  cmake_policy(SET CMP0078 NEW)
endif()

if(POLICY CMP0086)
  cmake_policy(SET CMP0086 NEW)
endif()

project(cpp_wrapper)

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
    ../src/Circle.cpp
    ../src/Rectangle.cpp
    ../src/ShapeManager.cpp
    ../src/DataStreamExample.cpp
)

# Define the include files for the project
set(includes
    cpp_wrapper.i
    ../include/Circle.h
    ../include/Rectangle.h
    ../include/ShapeManager.h
    ../include/DataStreamExample.h
    ../include/Shape.h
)

# Include directories
include_directories(${Python3_INCLUDE_DIRS} ${NUMPY_INCLUDE_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Set the SWIG module name
set_property(SOURCE ${includes} PROPERTY SWIG_MODULE_NAME cpp_wrapper)

# Generate the SWIG wrapper.
set(CMAKE_SWIG_OUTDIR ${CMAKE_CURRENT_SOURCE_DIR})
set_source_files_properties(${includes} PROPERTIES CPLUSPLUS ON)
swig_add_library(cpp_wrapper LANGUAGE python SOURCES ${src} ${includes})
swig_link_libraries(cpp_wrapper Python3::Python)

# Define the installation rules.
install(TARGETS cpp_wrapper DESTINATION ${CMAKE_SWIG_OUTDIR})

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
