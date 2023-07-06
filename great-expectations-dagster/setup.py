from setuptools import find_packages, setup

setup(
    name="great_expectations_dagster",
    packages=find_packages(exclude=["great_expectations_dagster_tests"]),
    install_requires=[
        "dagster",
        # "dagster-cloud",
        "dagster-ge",
        "great-expectations"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
