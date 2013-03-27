from setuptools import setup, find_packages


version = '1.0'

install_requires = [
    # List your project dependencies here.
]


setup(name='python_package_templete',
    version=version,
    description="A simple templete for packages written in python. It contains src directory as the root for the modules. The test directory includes all the unit tests.",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='python package templete',
    author='Faris Mohammed',
    author_email='farismosman@gmail.com',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['python_templete=python_templete:main']
    }
)
