import setuptools

install_requires = [
   'pyjwt>=2.0.0',
   'pandas',
   'requests',
   'websockets'
]

setuptools.setup(
    name='pybithumb2',
    version='0.1',
    author='Dongoo Lee',
    author_email='ldg810@gmail.com',
    description='python wrapper for Bithumb API v2.0',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
