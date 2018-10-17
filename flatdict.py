#!/usr/bin/env python2

import json
import sys

class FlatDict(object):
    def __init__(self, prefix, obj):
        self.flat_list = self._process_node(prefix, obj)

    def out(self):
        out_dict = {}

        for elem in self.flat_list:
            key = elem.keys()[0]
            out_dict[key] = elem[key]

        return out_dict

    def _process_node(self, prefix, obj):
        rs = []

        if isinstance(obj, (int, float, str, unicode, bool, type(None))):
            return [ {prefix: obj} ]
        elif isinstance(obj, dict):
            rs = self._process_dict_node(prefix, obj)
        elif isinstance(obj, list):
            rs = self._process_list_node(prefix, obj)
        else:
            sys.stderr.write('unhandled object: %s' % (json.dumps(obj,
                                                       indent=4)))
            sys.stderr.write('      its type  : %s' % (type(obj)))
            raise ValueError

        upd = []
        for elem in rs:
            key = elem.keys()[0]
            val = elem[key]
            newkey = '{}.{}'.format(prefix, key)
            upd += [{newkey: elem[key]}]

        return upd

    def _process_dict_node(self, prefix, obj):
        ans = []
        for key in obj:
            ans += self._process_node(key, obj[key])
        return ans

    def _process_list_node(self, prefix, obj):
        ans = []
        for (idx, elem) in enumerate(obj):
            ans += self._process_node(str(idx), elem)
        return ans

