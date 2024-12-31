cmake_minimum_required(VERSION 3.10)
project(boost_integration)

# Find Boost and Python
find_package(Boost REQUIRED COMPONENTS python3 numpy)  # Adjust for your Python version
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Define the source files for the project
set(SOURCES 
    bindings.cpp
    ../../shared/src/Circle.cpp
    ../../shared/src/Rectangle.cpp
    ../../shared/src/ShapeManager.cpp
    ../../shared/src/DataStreamExample.cpp
)

# Define target
add_library(boost_integration MODULE ${SOURCES})

set(LIBRARY_DESTINATION "${CMAKE_SOURCE_DIR}/../../libs")
message(STATUS "Libraries will be stored in: ${LIBRARY_DESTINATION}")

# Set Python module install location to the root folder
set_target_properties(boost_integration PROPERTIES
    PREFIX ""  # Remove the default "lib" prefix for shared libraries
    LIBRARY_OUTPUT_DIRECTORY ${LIBRARY_DESTINATION}
    SUFFIX ".so"                   # Shared library suffix
)

# Link libraries
target_include_directories(boost_integration PRIVATE 
    ${Boost_INCLUDE_DIRS} 
    ${Python3_INCLUDE_DIRS} 
    ../../shared/include  # Include path for header files
)

target_link_libraries(boost_integration PRIVATE 
    ${Boost_LIBRARIES} 
    ${Python3_LIBRARIES}
    ${Boost_NUMPY_LIBRARY}
)
