import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hangman-game",
    version="1.0.5",
    author="Christopher Enytc",
    author_email="chris@enytc.com",
    description="A CLI game built with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrisenytc/hangman",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hangman = hangman_game.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
