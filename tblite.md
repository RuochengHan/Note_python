# tblite

## version issue
Somehow tblite 0.4.0 has some problem in MO coefficient. e.g. c1ccccc1 not equivalent
0.4.0 is quicker (~2-3 times) for large molecules (200 atoms). The energy/gradient seems to be the same.

Recommend to use tblite 0.3.0 for MO coefficient.
Recommend to use tblite 0.4.0 for energy/gradient.
Note that conda install conda-forge::tblite-python=0.4.0 with tblite=0.4.0 can use all 16 cores, with **pip version tblite 0.4.0 causes problem in using all 16 cores (only 2-4 cores)**


Always test c1ccccc1 speed and accuracy after newly install

## pip
```bash
pip install tblite==0.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple # this is python API
export OMP_NUM_THREADS=16
export MKL_NUM_THREADS=16

# sometimes need to reactivate the conda env

```


## conda
```bash
conda install conda-forge::tblite=0.3.0 # this is CMD tblite run
conda install tblite-python=0.3.0 # this is python API
export OMP_NUM_THREADS=16
export MKL_NUM_THREADS=16
```
