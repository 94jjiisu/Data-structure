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
