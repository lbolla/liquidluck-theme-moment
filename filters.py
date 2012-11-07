#!/usr/bin/env python


def description(key):
    from liquidluck.options import settings
    dct = settings.theme['vars'].get('descriptions')
    if not isinstance(dct, dict):
        return ''
    if key not in dct:
        return ''
    return dct[key]


def tagcloud_size(tags):
    w_min = min(len(items) for items in tags.itervalues())
    w_max = max(len(items) for items in tags.itervalues())
    return w_min, w_max
