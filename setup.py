from setuptools import setup


setup(
    name='mirrors-pyspelling-for-pre-commit',
    version='0.0.0',
    install_requires=['pyspelling==2.6'],
    entry_points = {
        'console_scripts': ['wraps_pyspelling=wraps_pyspelling:entrypoint'],
    }
)
