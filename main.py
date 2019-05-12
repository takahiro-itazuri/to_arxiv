import os
import sys
import shutil

def move_files_to_root(root, directory):
    files = os.listdir(directory)
    for f in files:
        path = os.path.join(directory, f)
        if os.path.isdir(path):
            move_files_to_root(root, path)
            shutil.rmtree(path)
        elif os.path.isfile(path):
            if not os.path.exists(os.path.join(root, f)):
                shutil.move(path, root)

def convert_path(filename):
    output = ''
    with open(filename, 'r') as f:
        for line in f:
            # detect escape
            if '\includegraphics' in line or '\input' in line:
                start = 0
                pos = line.find('{', start)
                while pos != -1:
                    start = pos + 1
                    lastslash = pos + 1
                    end = pos + 1
                    while line[end] != '}':
                        if line[end] == '/':
                            lastslash = end
                        end += 1
                    before = line[start:end]
                    after = line[lastslash+1:end]
                    line = line.replace(before, after)
                    pos = line.find('{', start)

            output += line

    os.remove(filename)
    with open(filename, 'w') as f:
        f.write(output)

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    shutil.copytree(src, dst)
    move_files_to_root(dst, dst)

    files = os.listdir(dst)
    for f in files:
        if '.tex' in f:
            convert_path(os.path.join(dst, f))
