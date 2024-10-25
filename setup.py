from setuptools import setup

setup(
    name='Task-CLI',  # The name of your package
    version='0.1',
    py_modules=['main'],  # Points to your single Python file (main.py)
    install_requires=[],  # Add dependencies here if needed
    entry_points={
        'console_scripts': [
            'task-cli = main:main',
        ],
    },
)
