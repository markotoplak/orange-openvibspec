#!/usr/bin/env python
import setuptools

if __name__ == '__main__':
    setuptools.setup(
        use_scm_version=True,
        setup_requires=['setuptools-scm', 'setuptools>=40.0'],
        install_requires=[
            'Orange3>=3.25.0',
            # Versions are determined by Orange
            'numpy',
            'scipy',
            'keras',
        ],
        extras_require={
            'doc': ['sphinx', 'recommonmark'],
            'test': [
                'flake8',
                'flake8-comprehensions',
                'flake8-black',
                'pep8-naming',
                'isort',
                'pre-commit',
                'pytest',
                'coverage',
                'codecov',
            ],
        },
    )
