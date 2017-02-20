from setuptools import setup

def main():
    setup(
        name='agent-adcf',
        decription="Journal de bord de l'agent zip",
        author='Alexandre Boucaud',
        author_email='boucaud.alexandre@gmail.com',
        license='BSD',
        entry_points={
            'console_scripts': [
                'adcf=cypher:main',
                ],
            },
        install_requires=['tqdm'],
        )


if __name__ == '__main__':
    main()
