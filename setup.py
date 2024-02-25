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
    url="https://github.com/kylelee95/create_sequel_app",
    install_requires=[
        "Click",
    ],
    include_package_data=True,
    entry_points="""
        [console_scripts]
        create-sequel-app=create_sequel_app:create_project
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
    python_requires=">=3.10",
)
