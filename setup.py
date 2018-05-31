from setuptools import setup


setup(
    name='python-cli',
    version='0.1',
    url='https://github.com/fidding/python-cli.git',
    py_modules=['python-cli'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fidding-cli=python_cli:cli
    ''',
)
