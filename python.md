1. check if the line containing x:
```python
line.startswith(str(x))
```
2. pip reinstall:
```bash
pip install --upgrade --force-reinstall <package>
```
3. remeber to .copy after np.delete. The result will not be wrong without .copy(), but execution time will be longer:
```python
a = np.delete(a, self.ind, i).copy()
```
4. multithreading einsum: https://pypi.org/project/einsumt/
5. pytorch cannot use complex value tensor converted from numpy.
6. check if the type is list:
```python
bool isinstance(a, list)
```
7. numpy.loadtxt load only one number:
```python
ndmin=1 # in loadtxt
```
8. kill a process
```python
os.kill(pid, signal.SIGTERM)
```

9. reduce function:
```python
from functools import reduce
abc = reduce(np.dot, (a,b,c))
```

10. initialize python nested list:
```python
[[0] * (n + 1) for _ in range(m + 1)] # not [[0]*(n+1)]*(m+1)!!!
```
