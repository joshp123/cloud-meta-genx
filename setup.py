from distutils.core import setup

setup(
    name='CloudGenX',
    version='0.1.0',
    author='J. J Palmer',
    author_email='josh@joshpalmer.co.uk',
    packages=['cloudgenx', 'genx'],
    // scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://joshpalmer.co.uk/GenX/',
    license='LICENSE.txt',
    description='XRay Diffraction analysis in the cloud.',
    long_description=open('README.txt').read(),
    install_requires=[
        "SciPy >= 0.0.5",
        "numpy >= 1.0",
    ],
)
