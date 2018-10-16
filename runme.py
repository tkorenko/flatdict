#!/usr/bin/env python2

import json

from flatdict import FlatDict

def main():
    with open('input.json', 'r') as fobj:
        j_in = json.load(fobj)
    data_in = j_in

    fd = FlatDict('root', data_in)
    out = fd.out()

    print '----------------------------------------------------------------'
    print 'input:'
    print json.dumps(data_in, indent=4)
    print '----------------------------------------------------------------'
    print 'output:'
    print json.dumps(out, indent=4, sort_keys=True)
    print '---------------------------------------------------------------!'

main()
