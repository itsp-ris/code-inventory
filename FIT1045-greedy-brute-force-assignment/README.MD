**Requirements**
1. Not allowed to import any Python library or module and should not be using any inbuilt python functions that 
simplify the tasks you are told to implement.
2. Include comments in your code explaining your algorithm.

<br />

**Task 1.1 & 1.2: graphFile0ps.py**
<br /><br />Limitations:
1. Accepts a filename and produces an adjacency matrix based on the data in that file.
2. Add a program which accepts a filename and a table representing an adjacency matrix which 
writes the adjacency matrix to that file.

<br />

**Task 1.3: intersection.py**
<br /><br />Limitations:
1. Accepts two file names (representing graphs) and finds the intersection of both graphs.
<br />Intersection refers to set of vertices and edges that are shared by any two graphs.
2. Where an edge is shared but has different weights in each graph, the weight of the edge in 
the intersection graph is the larger of the weights.
3. Where an intersection includes a vertex with no edges, that vertex is removed from 
the intersection.

<br />

**Task 1.4: union.py**
<br /><br />Limitations:
1. Accepts two file names (representing graphs) and finds the union of both graphs.
<br />Union refers to set of vertices and edges that are in either of the two graphs.
2. Where an edge is shared but has different weights in each graph, the weight of the edge in 
the union graph is the smaller of the weights.

<br />

**Task 1.5: difference.py**
<br /><br />Limitations:
1. Accepts two file names (representing graphs) and finds the difference between both graphs.
<br />Difference refers to set of edges that are in only one of the two graphs.
2. Where a vertex has no edges in the difference it is not included in the resultant graph.

<br />

**Task 2.1: supergraph.py**
<br /><br />Limitations:
1. Accepts three file names for different graphs and, using your work from previous sections, 
creates a super-graph.
<br /> Super-graph of N graphs is a graph which includes all of the vertices and edges 
from all N graphs (using the cheapest edge where edges are shared).

<br />

**Task 2.2: connectivity.py**
<br /><br />Limitations:
1. Reads in a supergraph (or any combined graph) and determines whether every vertex in 
this combined graph can reach every other vertex in that graph.

<br />


**Task 2.3.1: greedy.py**
<br /><br />Limitations:
1. Accepts three graphs as input (via their filenames) and follows a greedy approach 
to determine the cheapest path from the intermediate graph to connect the other two graphs together.

<br />

**Task 2.3.2: bruteforce.py**
<br /><br />Limitations:
1. Accepts three graphs as input (via their filenames) and applies a brute-force
to determine the cheapest path from the intermediate graph to connect the other two graphs together.

<br />

**Application Development Tools**
1. Python IDE
