import sys
import os
import pytest

def import_cpp_wrapper(folder_name):
    if not os.path.isdir(folder_name):
        raise ValueError(f"The provided folder '{folder_name}' does not exist or is not a directory.")

    if folder_name not in sys.path:
        sys.path.insert(0, folder_name)

    try:
        import cpp_wrapper
        return cpp_wrapper
    except ImportError as e:
        raise ImportError(f"Failed to import cpp_wrapper from '{folder_name}'. Error: {e}")

def pytest_addoption(parser):
    parser.addoption(
        "--folder-name", 
        action="store", 
        default=None, 
        help="Specify the folder name to pass to import_cpp_wrapper"
    )

@pytest.fixture(scope="session", autouse=True)
def init_cpp_wrapper(request):
    """Session-wide fixture to initialize import_cpp_wrapper."""
    folder_name = request.config.getoption("--folder-name")
    if not folder_name:
        raise ValueError("You must provide --folder-name when running pytest.")

    # Initialize the wrapper with the provided folder name
    import_cpp_wrapper(folder_name)

@pytest.fixture(scope="module")
def cpp_wrapper_module(request):
    """Fixture to return the cpp_wrapper module imported from the given folder."""
    folder_name = request.config.getoption("--folder-name")
    if not folder_name:
        raise ValueError("You must provide --folder-name when running pytest.")

    cpp_wrapper = import_cpp_wrapper(folder_name)
    return cpp_wrapper
