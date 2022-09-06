# hbase_kernel
 Hbase Kernel for Jupyter

![PyPI version](https://img.shields.io/pypi/pyversions/hbase_kernel.svg)
![Github license](https://img.shields.io/github/license/Hourout/hbase_kernel.svg)
[![PyPI](https://img.shields.io/pypi/v/hive_kernel.svg)](https://pypi.python.org/pypi/hbase_kernel)
![PyPI format](https://img.shields.io/pypi/format/hbase_kernel.svg)
![contributors](https://img.shields.io/github/contributors/Hourout/hbase_kernel)
![downloads](https://img.shields.io/pypi/dm/hbase_kernel.svg)


## Installation

#### step1:
```
pip install hbase_kernel
```

To get the newest one from this repo (note that we are in the alpha stage, so there may be frequent updates), type:

```
pip install git+https://github.com/Hourout/hbase_kernel.git
```

#### step2:
Add kernel to your jupyter:

```
python -m hbase_kernel.install
```

ALL DONE! 🎉🎉🎉

## Uninstall

#### step1:

View and remove hbase kernel
```
jupyter kernelspec list
jupyter kernelspec remove hbase
```

#### step2:
uninstall hbase kernel:

```
pip uninstall hbase-kernel
```

ALL DONE! 🎉🎉🎉

## Using

```
jupyter notebook
```
<img src="image/hbase2.png" width = "700" height = "300" />

### step1: you should set hbase server (host and port)

### step2: write your hive sql
![](image/hbase1.png)

## Quote 
kernel logo

<img src="https://hbase.apache.org/images/hbase_logo_with_orca_large.png" width = "32" height = "32" />

- https://hbase.apache.org/