%module cpp_wrapper

%{
#include "../include/Shape.h"
#include "../include/Circle.h"
#include "../include/Rectangle.h"
#include "../include/ShapeManager.h"
#include "../include/DataStreamExample.h"
%}

%include <std_shared_ptr.i>
%shared_ptr(Shape);
%shared_ptr(Circle);
%shared_ptr(Rectangle);
%shared_ptr(ShapeManager);
%shared_ptr(DataStreamExample);

%include "cpointer.i"
%pointer_functions(int, intp);

%include "../include/Shape.h"
%include "../include/Circle.h"
%include "../include/Rectangle.h"
%include "../include/ShapeManager.h"
%include "../include/DataStreamExample.h"
