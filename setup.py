from setuptools import setup, find_packages


setup(
    name='mirrors-pyspelling-for-pre-commit',
    version='0.0.0',
    install_requires=['pyspelling==2.6'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points = {
        'console_scripts': ['wraps_pyspelling=mirrors_pyspelling.wraps_pyspelling:entrypoint'],
    }
)
