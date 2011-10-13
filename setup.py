from setuptools import setup

from mkmod import __version__

setup(name="mkmod",
      version=__version__,
      description="Makes Python modules.",
      long_description="You can stop touching __init__.py now.",
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.1',
      ],
      keywords='modules',
      author='Noah Seger',
      author_email='nosamanuel@gmail.com',
      url='http://github.com/nosamanuel/mkmod',
      license='MIT',
      py_modules=['mkmod'],
      entry_points=dict(console_scripts=['mkmod=mkmod:main']))
