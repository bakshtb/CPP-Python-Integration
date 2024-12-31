import sys
import os
import pytest
import importlib

def import_cpp_wrapper(tool_name):

    if '../libs' not in sys.path:
        sys.path.insert(0, '../libs')

    try:
        module = importlib.import_module(tool_name)
        return module
    except ImportError as e:
        raise ImportError(f"Failed to import '{tool_name}' from /libs. Error: {e}")

def pytest_addoption(parser):
    parser.addoption(
        "--tool-name", 
        action="store", 
        default=None, 
        help="Specify the tool name to import"
    )

@pytest.fixture(scope="session", autouse=True)
def init_cpp_wrapper(request):
    folder_name = request.config.getoption("--tool-name")
    if not folder_name:
        raise ValueError("You must provide --tool-name when running pytest.")

    import_cpp_wrapper(folder_name)

@pytest.fixture(scope="module")
def cpp_wrapper_module(request):
    folder_name = request.config.getoption("--tool-name")
    if not folder_name:
        raise ValueError("You must provide --tool-name when running pytest.")

    cpp_wrapper = import_cpp_wrapper(folder_name)
    return cpp_wrapper
