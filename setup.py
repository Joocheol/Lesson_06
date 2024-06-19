from setuptools import setup, find_packages

setup(
    name='deepheage',  # The name of your package
    version='0.1.0',  # The initial release version
    description='A stock simulation package',  # A short description of your package
    long_description=open('README.md').read(),  # Long description read from the readme file
    long_description_content_type='text/markdown',  # The format of the long description (use 'text/x-rst' if using reStructuredText)
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email address
    url='https://github.com/yourusername/mystock',  # URL to your package's homepage or repository
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',  # The programming language and version supported
        'License :: OSI Approved :: MIT License',  # The license type
        'Operating System :: OS Independent',  # The operating systems supported
    ],
    python_requires='>=3.6',  # The minimum Python version required
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy', 'pandas'
    ],
    include_package_data=True,  # Include package data specified in MANIFEST.in
    entry_points={
        'console_scripts': [
            # Add any console scripts if your package includes command-line scripts
            # e.g., 'mycommand=mystock.module:function'
        ],
    },
)