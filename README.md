# **C++ and Python Integration Tools Comparison**

## **Overview**

This repository compares different tools used for integrating C++ with Python, with a focus on:

1. **Inheritance and Polymorphism**: The ability to expose C++ class hierarchies to Python, supporting polymorphic behavior.
2. **Use of Pointers**: Efficient handling of C++ pointers and memory management from Python.

The tools we are testing include:

- **Pybind11**
- **SWIG (Simplified Wrapper and Interface Generator)**
- **Boost.Python**
- **cppyy**

Each tool is tested with C++ classes that demonstrate inheritance, polymorphism, and pointer usage. The goal is to evaluate which tool provides the best integration between C++ and Python.

---

## **C++ Code Implementation**

The core C++ code defines several classes and their functionalities:

- **Shape Class**: A base class with a virtual `area()` method.
- **Circle Class**: A derived class from `Shape` that implements `area()` to compute the area of a circle.
- **Rectangle Class**: A derived class from `Shape` that implements `area()` to compute the area of a rectangle.
- **ShapeManager Class**: Manages a collection of shapes and computes the total area.
- **DataStreamExample Class**: Demonstrates pointer usage by managing a dynamic array and exposing it to Python.

Each tool's implementation folder contains the necessary bindings and setup files for building and using the C++ code from Python.

---

## **Tool Implementations**

### **1. Pybind11**

The **Pybind11** folder contains the implementation for integrating C++ with Python using the **Pybind11** library. 

To build and test the project using Pybind11, follow these steps:

#### **Build Instructions**

```bash
# Navigate to the pybind11/ folder
cd pybind11/

# Create a build directory
mkdir build
cd build/

# Run CMake to configure the build
cmake ..

# Build the project
make

# Run the Python script to test the integration
cd ..
python main.py
```

### Expected Output
After running the above commands, you should see the following output:

```console
Area of shape at index 0 (Circle): 78.54
Area of shape at index 1 (Rectangle): 24.00
Total area of shapes: 102.54
Data Stream Buffer (Initial): [ 0 10 20]
Data Stream Buffer (After Modification): [30 10 20]
```

## **Proof of Task Success**

- The object-oriented principles of **inheritance** and **polymorphism** are evident in how the `Circle` and `Rectangle` inherit from the `Shape` class and override the `area()` method.
  
- **Pointer usage** is demonstrated through the `DataStreamExample` class, which uses a dynamically allocated buffer (`new uint32_t[bufferSize]`) and allows its manipulation from Python.

- The successful execution of the Python code, including the correct area calculations and the ability to modify the buffer, proves that the task of integrating C++ with Python has been accomplished effectively.

This demonstrates the integration of C++ functionality into Python, showing that we can handle complex C++ concepts like inheritance, polymorphism, and pointers within Python seamlessly.
