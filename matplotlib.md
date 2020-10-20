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
