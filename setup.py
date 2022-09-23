import setuptools


from setuptools import setup


setup(
    name='falcon-utils',
    version='1.0',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    package_dir={'': 'src'},
    packages=['falcon_utils'],
    py_modules=['falcon_utils']
)
