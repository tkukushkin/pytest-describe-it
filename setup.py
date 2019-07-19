import os

from setuptools import find_packages, setup


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pytest-describe-it',
    version='0.1.0',
    url='https://github.com/tkukushkin/pytest-describe-it',
    author='Timofey Kukushkin',
    author_email='tima@kukushkin.me',
    description='plugin for rich text descriptions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'pytest11': [
            'describe-it = pytest_describe_it._plugin',
        ],
    },
    install_requires=[
        'pytest',
        'typing;python_version<"3"',
    ],
    extras_require={
        'test': [
            'pycodestyle',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    project_urls={
        'Source': 'https://github.com/tkukushkin/pytest-describe-it',
    },
)
