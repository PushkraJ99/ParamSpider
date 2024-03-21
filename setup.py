from setuptools import setup, find_packages

setup(
    name='paramspider',
    version='2.0.0',
    author='Devansh Batham',
    author_email='devanshbatham009@gmail.com',
    description='Mining Parameters from Dark Corners of Web Archives',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'paramspider = paramspider.main:main'
        ]
    },
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
