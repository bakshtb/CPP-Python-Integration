
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

### C++ Code Overview

The C++ code is broken down into two main components:

1. **Inheritance and Smart Pointers**:
   - Defines classes for geometric shapes (`Circle` and `Rectangle`) and their management through a `ShapeManager`. Here's how it's organized:
     - **Base Class `Shape`**: Acts as an abstract base class with a pure virtual `area()` method, demonstrating **inheritance**. 
     - **Derived Classes**:
       - **`Circle`**: Inherits from `Shape`, implements `area()` to compute the area of a circle using the formula πr².
       - **`Rectangle`**: Also inherits from `Shape`, implementing `area()` for rectangle area calculation (length × width).
     - **`ShapeManager`**:
       - Utilizes **smart pointers** (`std::shared_ptr<Shape>`) for managing a collection of shapes. This ensures automatic memory management, preventing memory leaks by leveraging the shared ownership model of `std::shared_ptr`.
       - The class provides methods to add shapes, calculate the total area of all managed shapes, and other utility functions for shape manipulation.

2. **Raw Pointers**:
   - **`DataStreamExample`**:
     - Showcases the use of **raw pointers** for direct memory manipulation. It allocates a buffer using `new[]` and deallocates it with `delete[]`, emphasizing manual memory management which is less common in modern C++ but still useful in specific scenarios.

This structure provides a blend of modern C++ practices for memory safety and efficient shape management, alongside traditional memory handling, enabling smooth integration with Python.

---

### Test Cases Overview

We've included comprehensive test cases to ensure both the C++ functionality and its integration with Python are functioning correctly:

- **`test_shape_manager`**:
  - Checks that `ShapeManager` can manage both `Circle` and `Rectangle` instances correctly, including accurate area calculations for individual shapes and the sum of all shapes.

- **`test_data_stream_init`**:
  - Ensures that the `DataStreamExample` class initializes its buffer correctly, where each element should be `index * 10`.

- **`test_data_stream_modification`**:
  - Confirms that changes made to the buffer (`uint32_t*`) within `DataStreamExample` are correctly reflected when the buffer is subsequently accessed, validating the integrity of memory operations.

These tests are crucial for verifying the seamless interaction between C++ and Python, focusing on both shape management and data stream operations.
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
