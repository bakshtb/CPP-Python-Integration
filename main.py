import sys
import os
import argparse

def import_cpp_wrapper(folder_name):
    if not os.path.isdir(folder_name):
        raise ValueError(f"The provided folder '{folder_name}' does not exist or is not a directory.")
    
    if folder_name not in sys.path:
        sys.path.insert(0, folder_name)

def main():
    parser = argparse.ArgumentParser(description="Import cpp_wrapper from a specified folder and demonstrate its usage.")
    parser.add_argument("folder_name", type=str, help="Path to the folder containing the cpp_wrapper module")
    args = parser.parse_args()

    import_cpp_wrapper(args.folder_name)
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

if __name__ == "__main__":
    main()
