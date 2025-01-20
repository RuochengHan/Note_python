# tblite

## version issue
Somehow tblite 0.4.0 has some problem in MO coefficient. e.g. c1ccccc1 not equvalent
Recommend to use tblite 0.3.0

Always test c1ccccc1 spped and accuracy after newly install

## pip
```bash
pip install tblite==0.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple # this is python API
export OMP_NUM_THREADS=32
export MKL_NUM_THREADS=32

# sometimes need to reactivate the conda env

```

## conda
```bash
conda install conda-forge::tblite=0.3.0 # this is CMD tblite run
conda install conda-forge::tblite-python=0.3.0 # this is python API
```
