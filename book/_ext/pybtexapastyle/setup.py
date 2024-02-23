import setuptools


setuptools.setup(
    name='pybtex-apa-style',
    version='1.3',
    author='Naeka',
    author_email='contact@naeka.fr',
    description='Pybtex APA-like style',
    url='https://github.com/naeka/pybtex-apa-style',
    py_modules=['formatting.apa', 'labels.apa', 'names.firstlast'],
    entry_points={
        'pybtex.style.formatting': 'apa = formatting.apa:APAStyle',
        'pybtex.style.labels': 'apa = labels.apa:LabelStyle',
        'pybtex.style.names': 'firstlast = names.firstlast:NameStyle',
    },
    classifiers=(
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Markup',
        'Topic :: Utilities',
    ),
)
