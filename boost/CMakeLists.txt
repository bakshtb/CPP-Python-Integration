cmake_minimum_required(VERSION 3.10)
project(cpp_wrapper)

# Find Boost and Python
find_package(Boost REQUIRED COMPONENTS python3 numpy)  # Adjust for your Python version
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Define the source files for the project
set(SOURCES 
    bindings.cpp
    ../src/Circle.cpp
    ../src/Rectangle.cpp
    ../src/ShapeManager.cpp
    ../src/DataStreamExample.cpp
)

# Define target
add_library(cpp_wrapper MODULE ${SOURCES})

# Set Python module install location to the root folder
set_target_properties(cpp_wrapper PROPERTIES
    PREFIX ""  # Remove the default "lib" prefix for shared libraries
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/../"  # Output to the root directory
)

# Set properties for the shared library
set_target_properties(cpp_wrapper PROPERTIES
    PREFIX ""                      # No "lib" prefix
    SUFFIX ".so"                   # Shared library suffix
)

# Link libraries
target_include_directories(cpp_wrapper PRIVATE 
    ${Boost_INCLUDE_DIRS} 
    ${Python3_INCLUDE_DIRS} 
    ../include  # Include path for header files
)

target_link_libraries(cpp_wrapper PRIVATE 
    ${Boost_LIBRARIES} 
    ${Python3_LIBRARIES}
    ${Boost_NUMPY_LIBRARY}
)
