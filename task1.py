import sys
from pathlib import Path
import shutil


def sorting(dir_sorting: Path, dir_sorted: Path):
    for item in dir_sorting.iterdir():
        if item.is_dir():
            # print(f'[{item.name}]')
            sorting(item, dir_sorted)
            continue
        suffix = item.name.split('.')[-1]
        while not (dir_sorted / suffix).exists():
            (dir_sorted / suffix).mkdir(parents=True, exist_ok=True)
        shutil.copy(dir_sorting / item.name, dir_sorted / suffix / item.name)
        # print(f'[{item.name}]')
  

try:
    sorting(Path(sys.argv[1]), Path(sys.argv[2]))
except:
    try:
        sorting(Path(sys.argv[1]), Path(sys.argv[1]) / 'dist')
    except:
        print('Usage: python task1.py <source_directory> <destination_directory>')

