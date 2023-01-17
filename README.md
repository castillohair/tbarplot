# tbarplot - Bar plots with improved error bars

## What is this?

``tbarplot`` replaces the error bars in ``matplotlib``'s bar plot function with literally the letter T, properly scaled according to the specified error.

## Y tho

Using the letter "T" as the error bar symbol is a standard practice accepted by a number of scientific journals (that number being [one](https://www.hindawi.com/journals/amse/2022/3802603/)).

## Installation

```
pip install tbarplot
```

## Usage
``tbarplot.bar()``  has the same signature as ``plt.bar()``.

```python
import matplotlib.pyplot as plt
import tbarplot

# Fake data, real feelings
langs = ['C', 'C++', 'R', 'Python']
values = [20, 15, -10, 35]
yerr = [2, 5, 3, 7]

# Bar plot
fig = plt.figure()
tbarplot.bar(langs, values, yerr=yerr)

# Configure plot as with any other matplotlib function
plt.xlabel("Programming language")
plt.ylabel("How much I like this language")
plt.title("My programming language preferences")
plt.show()

```

![Example tbarplot](example_output.png?raw=true "Example")
