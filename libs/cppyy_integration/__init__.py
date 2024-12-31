import os
import cppyy
from .initializor import initialise
initialise('cppyy_integration', 'libcppyy_integrationCppyy.so', 'cppyy_integration.map')
del initialise


