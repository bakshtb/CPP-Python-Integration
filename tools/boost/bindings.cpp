#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/python/numpy.hpp>
#include "Shape.h"
#include "Circle.h"
#include "Rectangle.h"
#include "ShapeManager.h"
#include "DataStreamExample.h"

using namespace boost::python;

namespace py = boost::python;
namespace np = boost::python::numpy;

np::ndarray getBufferAsNumpyArray(const DataStreamExample& obj) {
    uint32_t* buffer = obj.getDataBuffer();
    size_t bufferSize = obj.getBufferSize();

    // Convert the raw buffer to a NumPy array
    py::tuple shape = py::make_tuple(bufferSize);
    py::tuple stride = py::make_tuple(sizeof(uint32_t));
    np::dtype dtype = np::dtype::get_builtin<uint32_t>();

    return np::from_data(buffer, dtype, shape, stride, py::object());
}

// Module initialization function for Python
BOOST_PYTHON_MODULE(boost_integration) {
    register_ptr_to_python<std::shared_ptr<Shape>>();
    register_ptr_to_python<std::shared_ptr<ShapeManager>>();
    
    // Expose the Shape class
    class_<Shape, boost::noncopyable>("Shape", no_init)
        .def("area", &Shape::area, "Returns the area of the shape");

    // Expose the Circle class, inheriting from Shape
    class_<Circle, bases<Shape>>("Circle", init<double>())
        .def("area", &Circle::area, "Returns the area of the circle");

    // Expose the Rectangle class, inheriting from Shape
    class_<Rectangle, bases<Shape>>("Rectangle", init<double, double>())
        .def("area", &Rectangle::area, "Returns the area of the rectangle");

    class_<ShapeManager, std::shared_ptr<ShapeManager>>("ShapeManager")
        .def("addShape", &ShapeManager::addShape)
        .def("totalArea", &ShapeManager::totalArea)
        .def("getShape", &ShapeManager::getShape);


    // Initialize NumPy
    np::initialize();

    py::class_<DataStreamExample>("DataStreamExample", py::init<size_t>())
        .def("getDataBuffer", &getBufferAsNumpyArray)  // Return as NumPy array
        .def("printDataBuffer", &DataStreamExample::printDataBuffer)
        .def("getBufferSize", &DataStreamExample::getBufferSize);
}
