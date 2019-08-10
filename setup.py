from setuptools import setup

setup(
    name="tljh-tfx",
    author="Yajun Wang",
    version="0.1",
    license="3-clause BSD",
    entry_points={"tljh": ["tfx = tljh_tfx"]},
    py_modules=["tljh_tfx"],
)
