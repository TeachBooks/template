# -*- coding:Utf-8 -*-
from __future__ import unicode_literals

from pybtex.style.names import BaseNameStyle, name_part
from pybtex.style.template import join


class NameStyle(BaseNameStyle):

    def format(self, person, abbr=False):
        r"""
        Format names similarly to {vv~}{ll}{, jj}{, f.} in BibTeX.

        >>> from pybtex.database import Person
        >>> name = Person(string=r"Charles Louis Xavier Joseph de la Vall{\'e}e Poussin")
        >>> firstlast = NameStyle().format

        >>> print(firstlast(name).format().render_as('latex'))
        Charles Louis Xavier~Joseph de~la Vall{é}e~Poussin
        >>> print(firstlast(name).format().render_as('html'))
        Charles Louis Xavier&nbsp;Joseph de&nbsp;la Vall<span class="bibtex-protected">é</span>e&nbsp;Poussin

        >>> print(firstlast(name, abbr=True).format().render_as('latex'))
        C.~L. X.~J. de~la Vall{é}e~Poussin
        >>> print(firstlast(name, abbr=True).format().render_as('html'))
        C.&nbsp;L. X.&nbsp;J. de&nbsp;la Vall<span class="bibtex-protected">é</span>e&nbsp;Poussin

        >>> name = Person(first='First', last='Last', middle='Middle')
        >>> print(firstlast(name).format().render_as('latex'))
        First~Middle Last
        >>> print(firstlast(name, abbr=True).format().render_as('latex'))
        F.~M. Last

        """
        return join[
            name_part(abbr=abbr)[person.rich_first_names + person.rich_middle_names],
            name_part(before=' ')[person.rich_prelast_names],
            name_part(before=' ')[person.rich_last_names],
        ]
