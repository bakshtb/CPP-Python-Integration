%module cpp_wrapper

%{
#include "../include/Shape.h"
#include "../include/Circle.h"
#include "../include/Rectangle.h"
#include "../include/ShapeManager.h"
#include "../include/DataStreamExample.h"
#define SWIG_FILE_WITH_INIT
%}

%include <std_shared_ptr.i>
%shared_ptr(Shape);
%shared_ptr(Circle);
%shared_ptr(Rectangle);
%shared_ptr(ShapeManager);

%include "numpy.i"
%init %{
import_array();
%}

%include "../include/Shape.h"
%include "../include/Circle.h"
%include "../include/Rectangle.h"
%include "../include/ShapeManager.h"
%include "../include/DataStreamExample.h"

// Extend the DataStreamExample class to override `getDataBuffer`
%extend DataStreamExample {
    // Override `getDataBuffer` for Python
    PyObject* getDataBuffer() {
        npy_intp dims[1] = { static_cast<npy_intp>(self->getBufferSize()) };
        return PyArray_SimpleNewFromData(1, dims, NPY_UINT32, self->getDataBuffer());
    }
}
