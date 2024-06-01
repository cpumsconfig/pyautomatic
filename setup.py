import setuptools

def check_pip_installed():
    try:
        import pip
        return True
    except ImportError:
        return False

if not check_pip_installed():
    print("Please install pip to proceed:")
    print("  https://pip.pypa.io/en/stable/installation/")
    exit(1)

setuptools.setup(
    name="pyautomatic",
    version="1.0",
    author="Moni Studios",
    author_email="monios114514@outlook.com/253517776@qq.com",
    description="pyautomatic",
    packages=setuptools.find_packages(),
    package_dir={'pyautomatic': 'pyautomatic'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
