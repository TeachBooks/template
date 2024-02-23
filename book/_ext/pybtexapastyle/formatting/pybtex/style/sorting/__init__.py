from __future__ import unicode_literals


from pybtex.plugin import Plugin


class BaseSortingStyle(Plugin):
    def sorting_key(self, entry):
        raise NotImplementedError

    def sort(self, entries):
        return sorted(entries, key=self.sorting_key)