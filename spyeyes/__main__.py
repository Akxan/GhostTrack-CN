"""让 `python -m spyeyes` work（pip install 后等同于 `spyeyes` 命令）。"""
import sys
from spyeyes import main

if __name__ == '__main__':
    sys.exit(main())
