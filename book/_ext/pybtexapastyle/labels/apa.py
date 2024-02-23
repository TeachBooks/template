# -*- coding:Utf-8 -*-
from __future__ import unicode_literals

from collections import Counter
import re
import unicodedata

from pybtex.style.labels import BaseLabelStyle


_nonalnum_pattern = re.compile('[^A-Za-z0-9 \-]+', re.UNICODE)


def _strip_accents(s):
    return "".join(
        (c for c in unicodedata.normalize('NFD', s)
            if not unicodedata.combining(c)))


def _strip_nonalnum(parts):
    """Strip all non-alphanumerical characters from a list of strings.

    >>> print(_strip_nonalnum([u"ÅA. B. Testing 12+}[.@~_", u" 3%"]))
    AABTesting123
    """
    s = "".join(parts)
    return _nonalnum_pattern.sub("", _strip_accents(s))


class LabelStyle(BaseLabelStyle):
    def format_labels(self, sorted_entries):
        labels = [self.format_label(entry) for entry in sorted_entries]
        count = Counter(labels)
        counted = Counter()
        for label in labels:
            if count[label] == 1:
                yield label
            else:
                yield label # + chr(ord('a') + counted[label])
                # counted.update([label])

    def format_label(self, entry):
        label = "Anonymous"
        if 'author' in entry.persons:
            label = self.format_author_or_editor_names(entry.persons['author'])
        elif 'editor' in entry.persons:
            label = self.format_author_or_editor_names(entry.persons['editor'])
        elif 'organization' in entry.fields:
            label = entry.fields['organization']
            if label.startswith("The "):
                label = label[4:]
        return ''
        # if 'year' in entry.fields:
        #     return "{}, {}".format(label, entry.fields['year'])
        # else:
        #     return "{}, n.d.".format(label)

    def format_author_or_editor_names(self, persons):
        if len(persons) is 1:
            return _strip_nonalnum(persons[0].last_names)
        elif len(persons) is 2:
            return "{} & {}".format(
                _strip_nonalnum(persons[0].last_names),
                _strip_nonalnum(persons[1].last_names))
        else:
            return "{} et al.".format(
                _strip_nonalnum(persons[0].last_names))
