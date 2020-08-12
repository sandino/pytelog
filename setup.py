import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytelog',
    version="0.1",
    author="sandino",
    author_email='vladts77@gmail.com',
    description='Python telegram logger',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandino/pytelog',
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ]
)