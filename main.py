"""
This program reliably reads the contents of 'summary.txt' as raw bytes and writes them
to '/output/entry.txt'. It operates deterministically to ensure that the exact byte
sequence from the source file is preserved in the destination.
"""
import os

def main():
    if not os.path.exists('/output'):
        os.makedirs('/output')
    # We copy as bytes to preserve the exact file encoding and content without any
    # potential modifications from text-mode character decoding/encoding.
    with open('summary.txt', 'rb') as f:
        content = f.read()
    with open('/output/entry.txt', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    main()
