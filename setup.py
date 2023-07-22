from setuptools import setup, find_packages

setup(
    name='rink-plotly',  # Replace 'your-package-name' with the desired package name
    version='0.1.0',           # Set an appropriate version number
    packages=find_packages(),
    scripts=['rink_plotly/rink_plot.py'],
    install_requires=[
        'numpy',
        'plotly',
    ],
    author='Max Tixador',        # Replace with your name
    description='Package to help plotting a rink using Plotly',  # Add a brief description
    long_description='Package to help plotting a rink using Plotly',  # Add a detailed description
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_project_name',  # Add the URL of your repository
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
