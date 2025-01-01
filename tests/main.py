import pytest
import math

def test_shape_manager(cpp_wrapper_module):
    circle_radius = 7
    rectangle_length = 5
    rectangle_width = 8

    circle_area = math.pi * circle_radius**2
    rectangle_area = rectangle_length * rectangle_width
    total_area = circle_area + rectangle_area

    shape_manager = cpp_wrapper_module.ShapeManager()
    circle = cpp_wrapper_module.Circle(circle_radius)
    rectangle = cpp_wrapper_module.Rectangle(rectangle_length, rectangle_width)

    shape_manager.addShape(circle)
    shape_manager.addShape(rectangle)

    assert shape_manager.getShape(0).area() == pytest.approx(circle_area, 0.01), "ShapeManager failed to retrieve correct Circle area"
    assert shape_manager.getShape(1).area() == pytest.approx(rectangle_area, 0.01), "ShapeManager failed to retrieve correct Rectangle area"
    assert shape_manager.totalArea() == pytest.approx(total_area, 0.01), "ShapeManager total area calculation is incorrect"



def test_data_stream_init(cpp_wrapper_module):
    data_stream = cpp_wrapper_module.DataStreamExample(3)
    buffer = data_stream.getDataBuffer()

    for i in range(data_stream.getBufferSize()):
        assert buffer[i] == i * 10, f"Buffer value at index {i} is incorrect"

def test_data_stream_modification(cpp_wrapper_module):
    data_stream = cpp_wrapper_module.DataStreamExample(3)
    buffer = data_stream.getDataBuffer()

    buffer[0] = 30
    assert data_stream.getDataBuffer()[0] == 30, "DataStream buffer modification failed"



if __name__ == "__main__":
    pytest.main([__file__])
