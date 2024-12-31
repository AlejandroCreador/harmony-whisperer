from setuptools import setup, find_packages

setup(
    name="harmony_whisperer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',
        'librosa>=0.9.0',
        'matplotlib>=3.4.0',
        'soundfile>=0.10.3',
        'tkinter>=8.6',
        'scipy>=1.7.0'
    ],
    author="Tu Nombre",
    author_email="tu@email.com",
    description="Un analizador musical inteligente",
    long_description=open('docs/README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/harmony_whisperer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)