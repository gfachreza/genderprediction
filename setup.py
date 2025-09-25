from setuptools import setup, find_packages


setup(
    name="GenderPredictor",
    version="0.0.7",
    description="Library to predict gender from their name",
    author=["Fachreza"],
    author_email=["gfachreza@gmail.com"],
    packages=find_packages(),
    url="https://github.com/gfachreza/genderprediction",
    maintainer="Fachreza",
    zip_safe=False,
    package_data={
        "gender_predictor": ["*.pkl"],
    },
    install_requires=[
        "scikit-learn",
        "pandas",
    ],
)