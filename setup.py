from setuputil import *

setuptools.setup(
    name=projectname,
    version=version,
    author="k. goger",
    author_email=f"k.r.goger+{projectname}@gmail.com",
    url=f"https://github.com/kr-g/{projectname}",
    packages=setuptools.find_packages(exclude=[]),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=python_requires,
)
