# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _swig_integration
else:
    import _swig_integration

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


SHARED_PTR_DISOWN = _swig_integration.SHARED_PTR_DISOWN
class Shape(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _swig_integration.delete_Shape

    def area(self):
        return _swig_integration.Shape_area(self)

# Register Shape in _swig_integration:
_swig_integration.Shape_swigregister(Shape)

class Circle(Shape):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, radius):
        _swig_integration.Circle_swiginit(self, _swig_integration.new_Circle(radius))

    def area(self):
        return _swig_integration.Circle_area(self)
    __swig_destroy__ = _swig_integration.delete_Circle

# Register Circle in _swig_integration:
_swig_integration.Circle_swigregister(Circle)

class Rectangle(Shape):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, width, height):
        _swig_integration.Rectangle_swiginit(self, _swig_integration.new_Rectangle(width, height))

    def area(self):
        return _swig_integration.Rectangle_area(self)
    __swig_destroy__ = _swig_integration.delete_Rectangle

# Register Rectangle in _swig_integration:
_swig_integration.Rectangle_swigregister(Rectangle)

class ShapeManager(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def addShape(self, shape):
        return _swig_integration.ShapeManager_addShape(self, shape)

    def totalArea(self):
        return _swig_integration.ShapeManager_totalArea(self)

    def getShape(self, index):
        return _swig_integration.ShapeManager_getShape(self, index)

    def __init__(self):
        _swig_integration.ShapeManager_swiginit(self, _swig_integration.new_ShapeManager())
    __swig_destroy__ = _swig_integration.delete_ShapeManager

# Register ShapeManager in _swig_integration:
_swig_integration.ShapeManager_swigregister(ShapeManager)

class DataStreamExample(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, size):
        _swig_integration.DataStreamExample_swiginit(self, _swig_integration.new_DataStreamExample(size))

    def printDataBuffer(self):
        return _swig_integration.DataStreamExample_printDataBuffer(self)

    def getBufferSize(self):
        return _swig_integration.DataStreamExample_getBufferSize(self)
    __swig_destroy__ = _swig_integration.delete_DataStreamExample

    def getDataBuffer(self, *args):
        return _swig_integration.DataStreamExample_getDataBuffer(self, *args)

# Register DataStreamExample in _swig_integration:
_swig_integration.DataStreamExample_swigregister(DataStreamExample)


