import cpp_wrapper

circle = cpp_wrapper.Circle(5)
rectangle = cpp_wrapper.Rectangle(4, 6)

shape_manager = cpp_wrapper.ShapeManager()
shape_manager.addShape(circle)
shape_manager.addShape(rectangle)

print(f"Area of shape at index 0 (Circle): {shape_manager.getShape(0).area():.2f}")
print(f"Area of shape at index 1 (Rectangle): {shape_manager.getShape(1).area():.2f}")
print(f"Total area of shapes: {shape_manager.totalArea():.2f}")

data_stream = cpp_wrapper.DataStreamExample(3)
print("Data Stream Buffer (Initial):", data_stream.getDataBuffer())

buffer = data_stream.getDataBuffer()
buffer[0] = 30 
print("Data Stream Buffer (After Modification):", data_stream.getDataBuffer())
