# Overfit
Perfectly fits a polynomial hypersurface to any dataset.
A fairly straightforward mathematical exercise, this gave me a fun problem to work on during covid.

## Theory
This algorithm is a multivariable generalization of
[polynomial interopolation](https://en.wikipedia.org/wiki/Polynomial_interpolation "Wikipedia"),
which is generally *not* the best strategy for
[multivariate interpolation](https://en.wikipedia.org/wiki/Multivariate_interpolation "Wikipedia"),
but it does serve as a demonstration for polynomial completeness.

## Running
This program is run from the command line by running the file overfit.py. It takes
an input dataset as a csv file containing m rows (datapoints) of n columns each.
The first n-1 elements in each row represent that datapoint's coordinates, and the nth
element is the value at that point. The next arguments can be either a set of
coordinates to interpolate or a command to plot the polynomial with a given window.

## Example
This repository includes some (very) small example data.
I built this less than a year into college before I understood portability,
but this doesn't use any particularly specialized packages. I'm able to run
on an intel-based Macbook running MacOS Ventura with Python 3.9.6,
matplotlib 3.7.2 and numpy 1.25.2 with the following commands.
Since numpy is a matplotlib prereq, only
installing matplotlib should suffice.

```
python -m venv venv
source venv/bin/activate
pip install matplotlib
git clone https://github.com/cooper6558/Overfit.git
cd Overfit
python overfit.py planar_data.csv plot 0 4 0 4
python overfit.py planar_data.csv 2.5
> Prediction: 2.367188
python overfit.py data.csv 1 2 3
> Prediction: 5.687369
```

## A note on code quality
If you think this code looks like it was written by a college freshman, that's because it was.
I was revisiting this repository three years later and decided I might as well keep it up,
so I wrote this quick readme and fixed some things to make the code run without crashing,
but I won't be spending any more time on this project.
