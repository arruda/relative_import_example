#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys



if __name__ == "__main__" and __package__ is None:

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(1, parent_dir)


    mod = __import__('my_package')
    sys.modules["my_package"] = mod
    # or just import it:
    # import fast_vagrant_django

    __package__='my_package'

    from .submodule1.something import *

    print "done"
