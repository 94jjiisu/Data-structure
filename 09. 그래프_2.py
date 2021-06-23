### 그래프 순회 ###

### 깊이 우선 순회 ###

# DFS 구현


def DFS(g, u, discovered):
  """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
  discovered is a dictionary mapping each vertex to the edge that was used to
  discover it during the DFS. (u should be "discovered" prior to the call.)
  Newly discovered vertices will be added to the dictionary as a result.
  """
  for e in g.incident_edges(u): # for every outgoing edge from u
    v = e.opposite(u)
    if v not in discovered: # v is an unvisited vertex
      discovered[v] = e # e is the tree edge that discovered v
      DFS(g, v, discovered) # recursively explore from v
      
# call DFS starting from source s
discovered = {s : None} # a new dictionary, with u trivially discovered
DFS(g, s, discovered)


# DFS 확장 경로 구축

def construct_path(u, v, discovered):
  """
  Return a list of vertices comprising the directed path from u to v,
  or an empty list if v is not reachable from u.
  discovered is a dictionary resulting from a previous call to DFS started at u.
  """
  path = [] # empty path by default
  if v in discovered:
    # we build list from v to u and then reverse it at the end
    path.append(v)
    walk = v
    while walk is not u:
      e = discovered[walk] # find edge leading to walk
      parent = e.opposite(walk)
      path.append(parent)
      walk = parent
    path.reverse() # reorient path from u to v
  return path

# DFS 연결 요소 계산

def DFS_complete(g):
  """Perform DFS for entire graph and return forest as a dictionary.
  Result maps each vertex v to the edge that was used to discover it.
  (Vertices that are roots of a DFS tree are mapped to None.)
  """
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None # u will be the root of a tree
      DFS(g, u, forest)
  return forest


### 너비 우선 순회 ###

# BFS 구현

def BFS(g, s, discovered):
  """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
  discovered is a dictionary mapping each vertex to the edge that was used to
  discover it during the BFS (s should be mapped to None prior to the call).
  Newly discovered vertices will be added to the dictionary as a result.
  """
  level = [s] # first level includes only s
  while len(level) > 0:
    next_level = [] # prepare to gather newly found vertices
    for u in level:
      for e in g.incident_edges(u): # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered: # v is an unvisited vertex
          discovered[v] = e # e is the tree edge that discovered v
          next_level.append(v) # v will be further considered in next pass
    level = next_level # relabel 'next' level to become current

    
    
    
    
    
### 최단 경로 ###

### 다익스트라 알고리즘 ###

from ..ch09.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

def shortest_path_lengths(g, src):
  """Compute shortest-path distances from src to reachable vertices of g.
  Graph g can be undirected or directed, but must be weighted such that
  e.element() returns a numeric weight for each edge e.
  Return dictionary mapping each reachable vertex to its distance from src.
  """
  d = {} # d[v] is upper bound from s to v
  cloud = {} # map reachable v to its d[v] value
  pq = AdaptableHeapPriorityQueue() # vertex v will have key d[v]
  pqlocator = {} # map from vertex to its pq locator
  
  # for each vertex v of the graph, add an entry to the priority queue, with
  # the source having distance 0 and all others having infinite distance
  for v in g.vertices():
    if v is src:
      d[v] = 0
    else:
      d[v] = float('inf') # syntax for positive infinity
    pqlocator[v] = pq.add(d[v], v) # save locator for future updates
    
  while not pq.is_empty():
    key, u = pq.remove_min()
    cloud[u] = key # its correct d[u] value
    del pqlocator[u] # u is no longer in pq
    
    for e in g.incident_edges(u): # outgoing edges (u,v)
      v = e.opposite(u)
      if v not in cloud:
        # perform relaxation step on edge (u,v)
        wgt = e.element()
        if d[u] + wgt < d[v]: # better path to v?
          d[v] = d[u] + wgt # update the distance
          pq.update(pqlocator[v], d[v], v) # update the pq entry
          
          
### 최단 경로 트리 ###

def shortest_path_tree(g, s, d):
  """Reconstruct shortest-path tree rooted at vertex s, given distance map d.
  Return tree as a map from each reachable vertex v (other than s) to the
  edge e=(u,v) that is used to reach v from its parent u in the tree.
  """
  tree = {}
  for v in d:
    if v is not s:
      for e in g.incident_edges(v, False): # consider INCOMING edges
        u = e.opposite(v)
        wgt = e.element()
        if d[v] == d[u] + wgt:
          tree[v] = e # edge e is used to reach v
  return tree



### 최소 신장 트리 ###

from ..ch09.pq import HeapPriorityQueue,AdaptableHeapPriorityQueue
from .partition import Partition

def MST_PrimJarnik(g):
  """Compute a minimum spanning tree of weighted graph g.
  Return a list of edges that comprise the MST (in arbitrary order).
  """
  d = {} # d[v] is bound on distance to tree
  tree = [] # list of edges in spanning tree
  pq = AdaptableHeapPriorityQueue() # d[v] maps to value (v, e=(u,v))
  pqlocator = {} # map from vertex to its pq locator
