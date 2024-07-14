from setuptools import setup, find_packages

setup(
    name="ninja-authtoken",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Django",
        "django-ninja"
    ],
    author="MoriZoki",
    author_email="morizoki.django@gmail.com",
    description="A simple Django app for django-ninja authentication tokens",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MoriZoki/ninja-authtoken",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
