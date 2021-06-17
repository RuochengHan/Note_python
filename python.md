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
