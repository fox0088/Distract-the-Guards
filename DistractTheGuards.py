# python version 2.7.13

from fractions import gcd
import copy

def solution(l):  
  gd_pr_list=list()
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      if(chk_pair(l[i], l[j])):

        # add to list of good pairings as tuples
        gd_pr_list.append((l[i],l[j]))

  return len(l) if len(gd_pr_list)==0 else find_pairings(l,gd_pr_list)

def chk_pair(x, y):
  res = (x+y) / gcd(x,y)
  return bool(res & (res - 1))

def find_pairings(l,gl):
  min_guard_cnt=len(l)
  counter=0   # tracks complete rotation of gd_pr_list

  while counter<len(l):
    tmp_l=copy.copy(l)  
    g0=gl[0]        # capture 1st tuple in gd_pr_list
    tmp_l.remove(g0[0])
    tmp_l.remove(g0[1])
    gl.remove(g0)   # remove 1st tuple to rotate later

# remove rest of tuple values from temp list
    for g in gl:        
      if (g[0] in tmp_l and g[1] in tmp_l):
        tmp_l.remove(g[0])
        tmp_l.remove(g[1])

    if min_guard_cnt > len(tmp_l): min_guard_cnt = len(tmp_l)

    gl.append(g0) # add initial tuple to end of gd_pr_list
    counter+=1

  return min_guard_cnt

if __name__=='__main__':
  l1=[1, 1,1, 33333323,130, 324, 3, 3, 1, 3, 3, 3, 32, 33]
  l2=[1, 7, 3, 21, 13, 19, 323, 24]
  l3=[1,1,3,2,4]
  l1=[1,1]
  print 'Solution:',solution(l2)
