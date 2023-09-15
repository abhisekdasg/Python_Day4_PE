import sys

def process_files(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            data = input_file.read()
        
        # Process data as needed, in this example, we'll just copy it
        with open(output_file_path, 'w') as output_file:
            output_file.write(data)
        
        print(f"File '{input_file_path}' processed successfully and saved to '{output_file_path}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when writing to '{output_file_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    process_files(input_file_path, output_file_path)
