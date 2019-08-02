from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Aniket Shah',
    author_email='ans8146@g.harvard.edu',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Aniket02/pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['google-cloud-storage'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ],
    }
)
