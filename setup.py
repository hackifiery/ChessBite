from setuptools import setup

setup(
    name='Gambit',
    version='0.1',
    py_modules=['main', 'engine'],  # Add all your script/module names here
    install_requires=['python-chess'],
    entry_points={
        'console_scripts': [
            'chessbite=main:main',
        ],
    },
    author='hackifiery',
    url='https://github.com/hackifiery/gambit',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
