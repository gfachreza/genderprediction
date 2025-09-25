# GenderPrediction

A simple Python library to predict gender from Indonesian names using a pre-trained **Logistic Regression** model with character n-grams.

## Installation

You can install directly from GitHub:

```bash
pip install git+https://github.com/gfachreza/genderprediction.git
```

## Usage

```python
from genderpredictor import GenderPrediction

gp = GenderPrediction()

print(gp("Andi Ahmad"))   # ('Laki-Laki', 99.93)
print(gp("Siti Ayu"))   # ('Perempuan', 99.99)
```

The model returns a tuple:
(predicted gender, confidence in %)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

💡 Note: If you are using this library in a company with a large employee base or significant annual revenue, I would appreciate it if you could kindly inform me via email at **gfachreza@gmail.com**.  
I will not request any fees or impose restrictions — I’m simply interested in knowing if this project is helpful for businesses. 🙂
