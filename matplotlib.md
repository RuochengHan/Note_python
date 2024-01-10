1. To obtain the exact ratio of the figure (without labels):
```python
ax.set_aspect(1/2)
```

2. Rotate the ticks
```python
plt.xticks(rotation=45)
```

3. X display is not available "Could not connect to any X display":
```python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
```

4. Segmentation fault (core dumped) or python: tpp.c:83: __pthread_tpp_change_priority: Assertion `new_prio == -1 || (new_prio >= fifo_min_prio && new_prio <= fifo_max_prio)' failed.
Aborted (core dumped): https://github.com/matplotlib/matplotlib/issues/9294/
```bash
pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
