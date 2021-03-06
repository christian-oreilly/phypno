from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'phypno', 'VERSION')) as f:
    VERSION = f.read().strip('\n')  # editors love to add newline

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='phypno',
    version=VERSION,
    description='Tools for EEG, ECoG, iEEG, especially for sleep',
    long_description=long_description,
    url='https://github.com/gpiantoni/phypno',
    author='Gio Piantoni',
    author_email='phypno@gpiantoni.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='neuroscience analysis sleep EEG ECoG',
    packages=find_packages(exclude=('test', )),
    install_requires=['numpy', 'scipy'],
    extras_require={
        'gui': ['scipy', 'pyqt5'],
        'viz': ['plotly', 'vispy'],
        'all': ['scipy',
                'mne',
                'nibabel',
                'python-vlc',  # for videos, to avoid problems with backends
                'request',  # to read ieeg.org dataset
                ]
    },
    package_data={
        'phypno': ['widgets/icons/oxygen/*.png',
                   'VERSION',
                   ],
    },

    entry_points={
        'console_scripts': [
            'scroll_data=phypno.scroll_data:main',
        ],
    },
)
