#  file_info_extension.py
#  http://lms.10x.org.il/item/144/

import sys
from pathlib import Path
from collections import defaultdict

def files_info():
    return {
        'total_files': 0,
        'total_size': 0,
    }


if __name__ == '__main__':
    files = defaultdict(files_info)
    # print("I am:", sys.argv[0])
    if len(sys.argv) <= 1:
        print("usage: ext_info.py path")
        print("displays number of files and total size of files per extension in the specified path.")
    else:
        # for i, s in enumerate(sys.argv[1:]):
            # print("Parameter #{}: {}".format(i + 1, s))

        folder = Path(sys.argv[1])
        for p in folder.iterdir():
            if p.is_file():
                # print(p, p.is_dir(), p.is_file(), p.stat().st_size, p.suffix)
                if len(p.suffix) <= 1:
                    p.suffix = '.'
                files[p.suffix[1:]]['total_files'] += 1
                files[p.suffix[1:]]['total_size'] += p.stat().st_size

        for name, info in sorted(files.items()):
            print(name, info['total_files'], info['total_size'])
            # print(name, info['total_files'], info['total_size'])