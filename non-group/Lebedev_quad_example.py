import numpy as np
import sys

def print_all(gw):
  g,w = gw
  print(g)
  print(w)

def set_a1():
  l_a = np.array([-1,1])
  grids = []
  for a in l_a:
    for i in range(3):
      grid = np.zeros((3))
      grid[i] = a
      grids.append(grid)

  return np.array(grids), 1./len(grids)

def set_a2():
  l_a = np.array([-1,1])/(2**0.5)
  l_aa = l_aaa = np.array(np.meshgrid(l_a,l_a)).T.reshape(-1,2)

  grids = []
  for aa in l_aa:
    for i in range(3):
      for j in range(i+1,3):
        grid = np.zeros((3))
        grid[i], grid[j] = aa[0], aa[1]
        grids.append(grid)

  return np.array(grids), 1./len(grids)

def set_a3():
  l_a = np.array([-1,1])/(3**0.5)
  l_aaa = np.array(np.meshgrid(l_a,l_a,l_a)).T.reshape(-1,3)

  grids = l_aaa.copy()

  return np.array(grids), 1./len(grids)


def set_bk(a):
  l_a = np.array([-a,a])
  b = (1. - 2.*a*a)**0.5
  l_b = np.array([-b,b])
  l_aab = np.array(np.meshgrid(l_a,l_a,l_b)).T.reshape(-1,3)

  grids = []
  for aab in l_aab:
    for i in range(3):
      grid = aab.copy()
      grid[i],grid[2] = aab[2],aab[i]
      grids.append(grid)

  return np.array(grids), 1./len(grids)


def set_ck(a):
  l_a = np.array([-a,a])
  b = (1. - a*a)**0.5
  l_b = np.array([-b,b])
  l_ab = np.array(np.meshgrid(l_a,l_b)).T.reshape(-1,2)

  grids = []
  for ab in l_ab:
    for i in range(3):
      for j in range(3):
        if i == j:
          continue
        grid = np.zeros((3))
        grid[i], grid[j] = ab[0], ab[1]
        grids.append(grid)

  return np.array(grids), 1./len(grids)

def set_dk(a,b):
  l_a = np.array([-a,a])
  l_b = np.array([-b,b])
  c = (1. - a*a-b*b)**0.5
  l_c = np.array([-c,c])
  l_abc = np.array(np.meshgrid(l_a,l_b,l_c)).T.reshape(-1,3)

  grids = []
  for abc in l_abc:
    for i in range(3):
      for j in range(3):
        if i == j:
          continue
        k = 3-i-j
        grid = np.zeros((3)) 
        grid[i], grid[j], grid[k] = abc[0], abc[1], abc[2]
        grids.append(grid)

  return np.array(grids), 1./len(grids)


print_all(set_a1())
print_all(set_a2())
print_all(set_a3())
print_all(set_bk(0.5))
print_all(set_ck(0.6))
print_all(set_dk(0.3,0.4))

