from setuptools import setup, find_packages
setup(
    name="chamfer-distance",
    version="0.1.0",
    description="Chamfer Distance PyTorch extension (minimal packaging)",
    packages=find_packages(include=["chamfer_distance", "chamfer_distance.*"]),
    include_package_data=True,
    package_data={"chamfer_distance": ["*.cpp", "*.cu"]},
    python_requires=">=3.8",
)