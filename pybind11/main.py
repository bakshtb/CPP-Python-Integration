import datastream_example

# Initialize shapes
circle = datastream_example.Circle(5)
rectangle = datastream_example.Rectangle(4, 6)

# Manage shapes
shape_manager = datastream_example.ShapeManager()
shape_manager.addShape(circle)
shape_manager.addShape(rectangle)

print(f"Area of shape at index 0 (Circle): {shape_manager.getShape(0).area()}")
print(f"Area of shape at index 1 (Rectangle): {shape_manager.getShape(1).area()}")
print(f"Total area of shapes: {shape_manager.totalArea()}")

# Initialize data stream example
data_stream = datastream_example.DataStreamExample(10)
print("Data Stream Buffer (Initial):", data_stream.getDataBuffer())

# Modify buffer in Python
buffer = data_stream.getDataBuffer()
buffer[3] = 100  # Example modification
print("Data Stream Buffer (After Modification):", data_stream.getDataBuffer())
