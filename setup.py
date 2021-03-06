from setuptools import setup, find_packages

setup(
    name='forklib',
    version='0.1.0',
    platforms="posix",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    maintainer="Dmitry Orlov",
    maintainer_email="me@mosquito.su",
    description="Fork the single process easily",
    packages=find_packages(exclude='tests'),
    license="Apache 2",
    long_description=open('README.rst').read(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
    ],
)
