from setuptools import setup, find_packages

setup(
    name='pythonappgitactions',  # Name of your project
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically discover and include all packages in the project
    install_requires=[],
    entry_points={  # If your project provides command-line scripts
        'console_scripts': [
            'my_project-cli=my_project.cli:main',  # Example CLI command
        ],
    },
    author='Swapnil',  # Author of the package
    author_email='swapnil_verma@outlook.com',  # Author's email address
    description='A short description of your project',  # Short project description
    long_description=open('README.md').read(),  # Long description, typically from a README file
    long_description_content_type='text/markdown',  # Format of the long description (e.g., markdown)
    url='https://github.com/swapnilverma0209/pythonappgitactions',  # URL to your project repository
    classifiers=[  # Additional metadata that categorizes your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)
