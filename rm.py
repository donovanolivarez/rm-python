
import os
import shutil
import sys
import glob

home_directory = os.path.expanduser('~')
home_files = os.listdir(home_directory)
trash_directory = home_directory + "/" + "rm_trash"


"""
makes the home directory if it doesn't exist.
"""
if "rm_trash" not in home_files:
    os.mkdir(trash_directory)

"""
Check for recursion flag   
"""
if "-r" in sys.argv:
    recurse = True
else:
    recurse = False



"""
check for recursion, run program based on recurse flag.
"""
if recurse is False:
    for arg in sys.argv[1:]:
        """
        if a wildcard is found, we remove only certain files.
        """
        if "*" or "?" in arg:
            glob_files = glob.glob(arg)
            if len(glob_files) == 0:
                sys.stderr.write("rm.py: cannot remove '" + arg + "' : No such file or directory.\n")
            else:
                for f in glob_files:
                    if os.path.basename(arg) in os.listdir(trash_directory):
                        count = 1;
                        """
                        the file is already in the trash bin.
                        update the name.
                        """
                        file_name, ext = os.path.splitext(os.path.basename(arg))
                        new_file_name = file_name + "-" + str(count) + ext
                        for trash_file in os.listdir(trash_directory):
                            if trash_file == new_file_name:
                                count = count + 1
                                new_file_name = file_name + "-" + str(count) + ext
                        shutil.copy2(arg, new_file_name)
                        shutil.move(new_file_name, trash_directory)
                        os.remove(arg)
                    else:
                        shutil.move(arg, trash_directory)
        else:
            if os.path.isfile(arg):
                if os.path.basename(arg) in os.listdir(trash_directory):
                    count = 1;
                    """
                    the file is already in the trash bin.
                    update the name.
                    """
                    file_name, ext = os.path.splitext(os.path.basename(arg))
                    new_file_name = file_name + "-" + str(count) + ext
                    for trash_file in os.listdir(trash_directory):
                        if trash_file == new_file_name:
                            count = count + 1
                            new_file_name = file_name + "-" + str(count) + ext
                    shutil.copy2(arg, new_file_name)
                    shutil.move(new_file_name, trash_directory)
                    os.remove(arg)
                else:
                    shutil.move(arg, trash_directory)
            elif os.path.isdir(arg):
                sys.stderr.write("rm.py: cannot remove '" + arg + "': Is a directory.\n")
            else:
                sys.stderr.write("rm.py: cannot remove '" + arg + "' : No such file or directory.\n")
else:
    for arg in sys.argv[1:]:
        if arg == "-r":
            continue
        elif "*" or "?" in arg:
            glob_files = glob.glob(arg)
            if len(glob_files) == 0:
                sys.stderr.write("rm.py: cannot remove '" + arg + "' : No such file or directory.\n")
            else:
                for f in glob_files:
                    if os.path.basename(arg) in os.listdir(trash_directory):
                        count = 1;
                        """
                        the file is already in the trash bin.
                        update the name.
                        """
                        file_name, ext = os.path.splitext(os.path.basename(arg))
                        new_file_name = file_name + "-" + str(count) + ext
                        for trash_file in os.listdir(trash_directory):
                            if trash_file == new_file_name:
                                count = count + 1
                                new_file_name = file_name + "-" + str(count) + ext
                        shutil.copy2(arg, new_file_name)
                        shutil.move(new_file_name, trash_directory)
                        os.remove(arg)
                    else:
                        shutil.move(arg, trash_directory)
        else:
            if os.path.isfile(arg):
                if os.path.basename(arg) in os.listdir(trash_directory):
                    count = 1;
                    """
                    the file is already in the trash bin.
                    update the name.
                    """
                    file_name, ext = os.path.splitext(os.path.basename(arg))
                    new_file_name = file_name + "-" + str(count) + ext
                    for trash_file in os.listdir(trash_directory):
                        if trash_file == new_file_name:
                            count = count + 1
                            new_file_name = file_name + "-" + str(count) + ext
                    shutil.copy2(arg, new_file_name)
                    shutil.move(new_file_name, trash_directory)
                    os.remove(arg)
                else:
                    shutil.move(arg, trash_directory)
            elif os.path.isdir(arg):
                if os.path.dirname(arg) in os.listdir(trash_directory) or os.path.basename(arg) in os.listdir(trash_directory):
                    """
                    handle input that has a slash
                    """
                    if "/" in arg:
                        d_name = os.path.dirname(arg)
                        d_name.rstrip("/")
                        print(d_name)
                    else:
                        d_name = arg
                        print(d_name)

                    count = 1
                    new_dir = d_name + "-" + str(count)
                    for td in os.listdir(trash_directory):
                        if td == new_dir:
                            count = count + 1
                            new_dir = d_name + "-" + str(count)
                    shutil.copytree(arg, new_dir)
                    shutil.move(new_dir, trash_directory)
                    shutil.rmtree(arg)
                else:
                    shutil.move(arg, trash_directory)
            else:
                sys.stderr.write("rm.py: cannot remove '" + arg + "' : No such file or directory.\n")
