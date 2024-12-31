# CPP-Python-Integration

This repository compares different tools used for integrating C++ with Python.

## Overview

Integrating C++ with Python allows developers to leverage the performance of C++ within Python applications. This repository explores various tools that facilitate this integration, providing examples and comparisons to guide developers in choosing the appropriate tool for their needs.

## Tools Compared

The following tools are included in this comparison:

- **Boost.Python**: A part of the Boost libraries, Boost.Python enables seamless interoperability between C++ and Python. It allows wrapping C++ classes and functions to be used in Python. [Learn more](https://www.boost.org/doc/libs/release/libs/python/)

- **pybind11**: A lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code. [Learn more](https://github.com/pybind/pybind11)

- **SWIG (Simplified Wrapper and Interface Generator)**: A tool that connects programs written in C and C++ with various high-level programming languages, including Python. [Learn more](http://www.swig.org/)

- **cppyy**: An automatic, run-time, Python-C++ bindings generator, which uses just-in-time compilation to provide fast and dynamic bindings. [Learn more](https://cppyy.readthedocs.io/)

## Repository Structure

The repository is organized as follows:

- `boost/`: Contains examples and setup for Boost.Python integration.
- `pybind11/`: Contains examples and setup for pybind11 integration.
- `swig/`: Contains examples and setup for SWIG integration.
- `cppyy/`: Contains examples and setup for cppyy integration.
- `include/`: Header files used across different integration examples.
- `src/`: Source files implementing the C++ functionalities.
- `main.py`: Python script demonstrating the usage of integrated C++ modules.

## Getting Started

To explore the examples:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bakshtb/CPP-Python-Integration.git
   cd CPP-Python-Integration
   ```

2. **Set up the environment**:
   Ensure you have Python installed along with the necessary build tools (e.g., CMake, a C++ compiler). Specific setup instructions for each tool are provided in their respective directories.

3. **Build and run examples**:
   Navigate to the directory of the tool you're interested in (e.g., `pybind11/`) and follow the instructions in the `README.md` or `BUILD.md` file to build and run the examples.

## Contributing

Contributions are welcome! If you'd like to add examples for other tools or improve existing ones, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pybind11](https://github.com/pybind/pybind11)
- [cppyy](https://cppyy.readthedocs.io/)
- [SWIG](http://www.swig.org/)
- [Boost.Python](https://www.boost.org/doc/libs/release/libs/python/)

