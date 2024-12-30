import os
import cppyy
from .initializor import initialise
initialise('cpp_wrapper', 'libcpp_wrapperCppyy.so', 'cpp_wrapper.map')
del initialise


