# MONarchy module for MON estimators #
======================================

## MONArchy provides : ##
- estimation functions using MON and derivative methods
- The MONArchy class to call each function on a set of data

## Analyse.py ##
- Analyse : to load data and return a JSON file with estimations and descriptive statistics

exemple : 
```
a = Analyse(path)
print(a.head())

print(a.info(column_name))
```
with 
- ``path`` : the path of a CSV file (string)
- ``column_name`` : the column name (string)

produce a JSON file with statistical estimators

## Changelog ##

### 1.0.5 ###
- add bayesian MoN 

## Refercences ##

@article{orenstein_robust_2019,
	title = {Robust Mean Estimation with the Bayesian Median of Means},
	url = {http://arxiv.org/abs/1906.01204},
	journaltitle = {{arXiv}:1906.01204 [math, stat]},
	author = {Orenstein, Paulo},
	urldate = {2021-04-08},
	date = {2019-06-04},
	eprinttype = {arxiv},
	eprint = {1906.01204},
	keywords = {Bayesian, Estimators, {MON}, Math, Mathematics - Statistics Theory, Statistics - Methodology},
}