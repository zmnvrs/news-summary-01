"""
This script copies the contents of summary.txt to /output/entry.txt.
"""
import os

def main():
    # Determine the path to summary.txt relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(base_dir, 'summary.txt')
    
    # Define the output destination
    output_dir = '/output'
    target_path = os.path.join(output_dir, 'entry.txt')
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the summary in binary mode and write it to the target
    # Binary mode is used to ensure exact byte-for-byte replication of the input file.
    with open(source_path, 'rb') as f_in:
        content = f_in.read()
        
    with open(target_path, 'wb') as f_out:
        f_out.write(content)

if __name__ == "__main__":
    main()
