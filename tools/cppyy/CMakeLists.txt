cmake_minimum_required(VERSION 3.10)

project(cppyy_example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

execute_process(COMMAND cling-config --cmake OUTPUT_VARIABLE CPPYY_MODULE_PATH OUTPUT_STRIP_TRAILING_WHITESPACE)
message("CPYY_MODULE_PATH: " ${CPPYY_MODULE_PATH})
list(INSERT CMAKE_MODULE_PATH 0 ${CPPYY_MODULE_PATH})

find_package(Cppyy)

set(SOURCES 
../../shared/src/Circle.cpp
../../shared/src/Rectangle.cpp
../../shared/src/ShapeManager.cpp
../../shared/src/DataStreamExample.cpp
)
set(HEADERS
../../shared/include/Circle.h
../../shared/include/Rectangle.h
../../shared/include/ShapeManager.h
../../shared/include/DataStreamExample.h
../../shared/include/Shape.h
)

include_directories(../../shared/include)

# It seems like this library has to be shared...
add_library(cpp_wrapper_lib SHARED ${SOURCES})
# Note this is a necessary compile flag for cppyy bindings to work.
set_target_properties(cpp_wrapper_lib PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(cpp_wrapper_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set(version "0.0.1")
cppyy_add_bindings(
   "cppyy_integration"
   "1.0"
   "Baruch"
   "bakshtb@gmail.com"
   LANGUAGE_STANDARD "17"
   GENERATE_OPTIONS "-D__PIC__;-Wno-macro-redefined"
   INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   LINK_LIBRARIES cpp_wrapper_lib
   H_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   H_FILES ${HEADERS})

   
set(SOURCE_DIR "${CMAKE_SOURCE_DIR}/build/cppyy_integration")
set(DEST_DIR "${CMAKE_SOURCE_DIR}/../../libs/cppyy_integration")


add_custom_target(copy_folder_after_build ALL
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${SOURCE_DIR} ${DEST_DIR}
    COMMENT "Copying folder after build"
)