import os

def lower_the_extension():
    path = input("Enter the path: ")
    path_exists = os.path.exists(path)

    if (path_exists):
        total = 0

        for (dirpath, _, filenames) in os.walk(path):
            for filename in filenames:
                filename_path = os.path.join(dirpath, filename)
                name, extension = os.path.splitext(filename_path)
                if filename.endswith(extension.upper()):
                    lowered_extension_filename_path = name + extension.lower()
                    os.rename(filename_path, lowered_extension_filename_path)
                    total += 1
                    print("{} => {}".format(filename_path, lowered_extension_filename_path))

        if (total > 0):
            print("Total lowered files extension: {}.".format(total))
        else:
            print("No files extension were lowered.")
    else:
        print("Path is not exists.")

if __name__ == "__main__":
    lower_the_extension()
