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

11. give a combined list:
```python
l_abc = np.array(np.meshgrid(l_a,l_b,l_c)).T.reshape(-1,3)
```

12. pandas without index:
```python
import pandas as pd
df = pd.read_csv('file.csv', index_col=0)
df.to_csv('file.csv', index=False)
```

13. pandas cannot read '\t' in string from request respond, but the printed out string can be read/
```python
# Reason:
#JSON Serialization: When data is sent as JSON, special characters like tabs and newlines are often escaped to ensure that the JSON remains valid and can be properly parsed. In JSON, a tab character is represented as \\t and a newline as \\n.
#String Representation: When you receive the response, these escaped characters are treated as literal strings in Python. Therefore, you see \\t instead of an actual tab character and \\n instead of an actual newline.

# Solution:
cleaned_text = response.text.replace('\\t', "\t").replace('\\n', "\n")
```
