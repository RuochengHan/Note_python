# Usually used package

```bash
conda install numpy matplotlib scikit-learn xtb psi4 rdkit
pip install opt_einsum scikit-learn rdkit MDAnalysis xtb typing-extensions tblite==0.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple # xtb requires typing-extensions
```

# PIP
1. mysql (Ref. https://stackoverflow.com/questions/74236020/please-help-me-to-fix-the-error-mysqlclient)
```bash
error: subprocess-exited-with-error

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple # not mysql-connector
```

# Conda
1. Error when conda install: IOError: [Errno 24] Too many open files:
```bash
ulimit -n 4096
```
2. 50X error, usually means cahnnels defaults not work, need to use conda-forge, but simply remove does not work in miniconda docker.
```bash
# Either to use nodefaults in conda_env.yml:
name: py39
channels:
  - nodefaults
  - conda-forge
dependencies:
  - python=3.9
  - xtb-python

# Or force --override-channels
conda install --override-channels -c conda-forge --yes --file conda_requirements.txt
```
