import setuptools

# pipenv install -e '.[dev,test]'
tests_require = [
    'pytest',
]

setuptools.setup(
    name="triangle_numbers_app",
    packages=setuptools.find_packages(),
    python_requires='>=3.7.0',
    install_requires=[
        "console-menu",
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=tests_require,
    scripts=['bin/triangle_numbers_app']
)