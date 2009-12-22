#! /usr/bin/env python

import sys

from pybindgen import Module, retval, param, FileCodeSink


def my_module_gen(out_file):

    mod = Module('testapi_pybindgen')
    mod.add_include('"testapi.h"')

    mod.add_function('func1', None, [])
    mod.add_function('func2', 'double', [param('double', 'x'),
                                         param('double', 'y'),
                                         param('double', 'z'),
                                         ])

    Multiplier = mod.add_class('Multiplier', allow_subclassing=True)
    Multiplier.add_constructor([])
    Multiplier.add_constructor([param('double', 'factor')])

    Multiplier.add_method('GetFactor', 'double', [], is_const=True)
    Multiplier.add_method('Multiply', 'double', [param('double', 'value')], is_virtual=True, is_const=True)
    

    mod.generate(FileCodeSink(out_file))

if __name__ == '__main__':
    my_module_gen(sys.stdout)
