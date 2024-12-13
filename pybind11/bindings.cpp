#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "Shape.h"
#include "Circle.h"
#include "Rectangle.h"
#include "ShapeManager.h"
#include "DataStreamExample.h"

namespace py = pybind11;

PYBIND11_MODULE(cpp_wrapper, m)
{
    py::class_<Shape, std::shared_ptr<Shape>>(m, "Shape")
        .def("area", &Shape::area);

    py::class_<Circle, Shape, std::shared_ptr<Circle>>(m, "Circle")
        .def(py::init<double>());

    py::class_<Rectangle, Shape, std::shared_ptr<Rectangle>>(m, "Rectangle")
        .def(py::init<double, double>());

    py::class_<ShapeManager>(m, "ShapeManager")
        .def(py::init<>())
        .def("addShape", &ShapeManager::addShape)
        .def("totalArea", &ShapeManager::totalArea)
        .def("getShape", &ShapeManager::getShape);

    py::class_<DataStreamExample>(m, "DataStreamExample")
        .def(py::init<size_t>())
        .def("getDataBuffer", [](DataStreamExample &self)
             { return py::array_t<uint32_t>(
                   {self.getBufferSize()}, {sizeof(uint32_t)},
                   self.getDataBuffer(), py::cast(&self)); })
        .def("getBufferSize", &DataStreamExample::getBufferSize)
        .def("printDataBuffer", &DataStreamExample::printDataBuffer);
}
