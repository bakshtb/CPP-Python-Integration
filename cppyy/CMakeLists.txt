cmake_minimum_required(VERSION 3.10)

project(cppyy_example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

execute_process(COMMAND cling-config --cmake OUTPUT_VARIABLE CPPYY_MODULE_PATH OUTPUT_STRIP_TRAILING_WHITESPACE)
message("CPYY_MODULE_PATH: " ${CPPYY_MODULE_PATH})
list(INSERT CMAKE_MODULE_PATH 0 ${CPPYY_MODULE_PATH})

find_package(Cppyy)

set(SOURCES 
../src/Circle.cpp
../src/Rectangle.cpp
../src/ShapeManager.cpp
../src/DataStreamExample.cpp
)
set(HEADERS
../include/Circle.h
../include/Rectangle.h
../include/ShapeManager.h
../include/DataStreamExample.h
../include/Shape.h
)

include_directories(../include)

# It seems like this library has to be shared...
add_library(knn_lib SHARED ${SOURCES})
# Note this is a necessary compile flag for cppyy bindings to work.
set_target_properties(knn_lib PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(knn_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set(version "0.0.1")
cppyy_add_bindings(
   "cpp_wrapper"
   "1.0"
   "Baruch"
   "bakshtb@gmail.com"
   LANGUAGE_STANDARD "17"
   GENERATE_OPTIONS "-D__PIC__;-Wno-macro-redefined"
   INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   LINK_LIBRARIES knn_lib
   H_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   H_FILES ${HEADERS})

   
set(SOURCE_DIR "${CMAKE_SOURCE_DIR}/build/cpp_wrapper")
set(DEST_DIR "${CMAKE_SOURCE_DIR}/cpp_wrapper")


add_custom_command(TARGET knn_lib POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${SOURCE_DIR} ${DEST_DIR}
    COMMENT "Copying folder after build"
)