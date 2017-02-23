from setuptools import setup


setup(
    name='adcf',
    decription="Journal de bord de l'agent Z",
    author='Alexandre Boucaud',
    author_email='boucaud.alexandre@gmail.com',
    license='BSD',
    version='0.1.0',
    packages=["adcf"],
    entry_points={
        'console_scripts': [
            'adcf=adcf:main',
            ],
        },
    install_requires=['tqdm'],
    )
