from setuptools import setup, find_packages

setup(
    name="create-sequel-app",
    version="0.1.0",
    py_modules=["create_sequel_app"],
    description="Create a new Sequel project",
    author="Kyle Lee",
    author_email="kyle@kylelee.dev",
    packages=find_packages(),
    presetup_requires=["click"],
    install_requires=[
        "Click",
    ],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        create-sequel-app=create_sequel_app:create_project
    """,
    classifiers=[
        "Programming language;;Python;;3",
        "License;;OSI Approved;; MIT License",
        "Operating Stem;; OS Independent",
    ],
    python_requires=">=3.10",
)
