
# CPP-Python-Integration

This project demonstrates the integration of C++ code with Python, combining Python's simplicity with the high performance of C++. The study evaluates multiple tools and techniques to achieve seamless interoperability between the two languages.

## Overview

Four tools were analyzed for their ability to expose C++ code to Python:

- **SWIG**
- **pybind11**
- **cppyy**
- **Boost.Python**

The project tests each tool’s capability to handle advanced C++ features:

- **Inheritance**
- **Smart Pointers**
- **Raw Pointers**

### Study Findings

All tools successfully integrated C++ with Python while supporting the tested advanced C++ features. The project leverages `CMake` to build Python libraries for each tool, ensuring a modular and maintainable structure.

**Note**: This project has been tested on Linux. All commands provided in the documentation are specific to Linux environments.

---

## Project Structure

The repository is organized as follows:

- **`shared/`**: Contains the C++ code. This directory is further divided into:
  - **`include/`**: Header files for the C++ code.
  - **`src/`**: Source files for the C++ code.
  
- **`libs/`**: Directory where `CMake` outputs the built Python libraries for each tool.

- **`tests/`**: Contains Python scripts executed via `pytest` to validate the functionality of the libraries. The Python tests interact with the C++ code integrated via the chosen tools. Tests accept a `--tool-name` argument to specify the integration tool being tested.

---

## Installation

Before building any tool, ensure it is installed on your system. Installation instructions are not provided here as they vary by operating system. Refer to the official documentation for guidance:

- [SWIG](http://www.swig.org)
- [pybind11](https://pybind11.readthedocs.io)
- [cppyy](https://cppyy.readthedocs.io)
- [Boost.Python](https://www.boost.org/doc/libs/release/libs/python/)

---

## Building Libraries

To build the Python library for a specific tool:

```bash
cd <tool_folder>
mkdir build
cd build
cmake ..
make
```

The generated library will be placed in the `libs/` directory.

---

## Running Tests

Automated tests ensure the correctness of the integrations. Tests are executed using `pytest` and can target a specific integration tool. For example:

```bash
python3 -m pytest -v --tb=short tests/main.py --tool-name=boost_integration
```

This example command runs all tests using the library built with Boost.Python (from `/libs/boost_integration`).


### C++ Code Overview

The C++ code consists of classes that model geometric shapes (`Circle` and `Rectangle`) and manage them (`ShapeManager`). The `Shape` class serves as a base class with a virtual `area()` method, showcasing **inheritance** as `Circle` and `Rectangle` inherit from `Shape` and implement the `area()` method to calculate their respective areas. The `ShapeManager` class manages a collection of shapes, using **smart pointers** (specifically `std::shared_ptr<Shape>`) to store and handle shapes dynamically, ensuring safe memory management. The `DataStreamExample` class demonstrates the use of **raw pointers**, where a buffer is allocated using `new` and deallocated with `delete[]`, showcasing manual memory management.

This integration of inheritance, smart pointers, and raw pointers ensures a blend of modern C++ practices for memory safety and efficient shape management, allowing smooth interaction with Python.

---

### Test Cases Overview

The project includes the following test cases to validate the C++ and Python integration:

- **`test_shape_manager`**: Validates that the `ShapeManager` correctly manages `Circle` and `Rectangle` objects, and ensures the area calculations (individual and total) are accurate.
  
- **`test_data_stream_init`**: Verifies that the `DataStreamExample` correctly initializes the buffer, with values equal to `index * 10`.
  
- **`test_data_stream_modification`**: Ensures that modifications to the `DataStreamExample` buffer are properly reflected when accessed later.

These tests ensure that the integration between C++ and Python works as expected, particularly when managing shapes and manipulating data buffers.
