import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shypan",
    version="0.0.1.4",
    author="ShypanLib",
    author_email="shypanlib@gmail.com",
    description="Librairie Shypan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShypanLib/Shypan",
    project_urls={
        "Bug Tracker": "https://github.com/ShypanLib/Shypan/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    python_requires=">=3.10",
)