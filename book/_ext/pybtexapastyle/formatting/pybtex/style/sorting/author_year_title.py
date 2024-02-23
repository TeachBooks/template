from __future__ import unicode_literals

from pybtex.style.sorting import BaseSortingStyle

class SortingStyle(BaseSortingStyle):

    def sorting_key(self, entry):
        if entry.type in ('book', 'inbook'):
            author_key = self.author_editor_key(entry)
        elif 'author' in entry.persons:
            author_key = self.persons_key(entry.persons['author'])
        else:
            author_key = ''
        return (author_key, entry.fields.get('year', ''), entry.fields.get('title', ''))

    def persons_key(self, persons):
        return '   '.join(self.person_key(person) for person in persons)

    def person_key(self, person):
        if person.prelast_names[0] != '{' and person.last_names[0] != '{' and person.first_names[0] != '{':
            return '  '.join((
                ' '.join(person.prelast_names + person.last_names),
                ' '.join(person.first_names + person.middle_names),
                ' '.join(person.lineage_names),
            )).lower()
        else:
            return '  '.join((
                ' '.join(person.first_names + person.middle_names),
                ' '.join(person.prelast_names + person.last_names),
                ' '.join(person.lineage_names),
            )).lower()

    def author_editor_key(self, entry):
        if entry.persons.get('author'):
            return self.persons_key(entry.persons['author'])
        elif entry.persons.get('editor'):
            return self.persons_key(entry.persons['editor'])
        else:
            return ''
