# Usually used package

```bash
conda install numpy matplotlib scikit-learn xtb psi4 rdkit
pip install opt_einsum -i https://pypi.tuna.tsinghua.edu.cn/simple
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
