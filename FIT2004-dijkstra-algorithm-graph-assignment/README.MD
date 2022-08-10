**Requirements**
1. Briefly describe the solution and its space and time complexity to the problem in 
a PDF file named Report_A4.pdf
2. The PDF file must give an outline of the solution (e.g., a high level idea of how did you 
solve it) and the worst-case space and time complexity of the solution.
3. Use the combination of array and list; NOT dictionary or any other python built-in data 
structures.
<br />Be aware of the time and space complexity of the python built-in function, if use any
python built-in functions.

<br />

**Task 1: Quickest Path**
<br /><br />Limitations:
1. Create a function named quickestPath(self, source, target) within the Graph class.
2. Return 2 values within a tuple:
    1) list containing all nodes in the order of the quickest path traversal from the source to 
    the target.
    2) time storing the total time required to reach the target from the source.
3. Traversed nodes is not unique as there can be multiple quickest paths.
4. If a path does not exist between source and target, function would return [[],−1].
5. Function should run within the time complexity of O(E log V) where V is the total number of 
points/nodes/vertices in the road network; and E is the total number of roads/edges in the road 
network. 
<br />The space complexity remains the same as the space complexity of your input graph O(E + V).

<br />

**Task 2: Safe Quickest Path**
Just like in the real world, certain paths could undesirable to travel - having tolls, under
roadworks or congested with heavy traffic, etc.
<br /><br />Limitations:
1. Information about which location having red light cameras are stored within the input file 
camera.txt.
<br />The rest of the unmentioned vertices are without red light cameras.
2. Information about which road having tolls are stored within the input file toll.txt.
<br />The rest of the unmentioned edges are without tolls.
3.  Represent these additional elements into the Graph data structure. 
<br />Create a function named augmentGraph(self, filename_camera, filename_toll) within the Graph class.
<br />Ensure that the space complexity remains at O(V + E).
5. Extend quickest path solution from Task 1 to account for the additional constraint of a safe path.
<br /> Create the function named quickestSafePath(self, source, target) within the Graph class.
6. Function should run within the time complexity of O(E log V) where V is the total number of 
points/nodes/vertices in the road network; and E is the total number of roads/edges in the road 
network. 
<br />The space complexity remains the same as the space complexity of your input graph O(E + V).

<br />

**Task 3: Quickest Detour Path**
Often during our travels, we would need to make a detour - be it for a quick refuel, bunk for the 
night, grabbing a quick meal or even going on a sight-seeing. 
<br />For this assignment, generalize this as detouring to a certain point/location/node/vertex 
for a service. 
<br />Such locations are stored within the input file service.txt
<br /><br />Limitations:
1. The rest of the unmentioned vertices are without any service.
2. Represent the additional service information within the Graph data structure.
<br />Create the function named addService(self, filename_service) within your Graph class.
<br />Ensure the complexity to still be within O(V + E).
3. Extend quickest path solution from Task 1 to now account for the additional constraint of a 
detour path.
<br />Create a function named quickestDetourPath(self, source, target) within the Graph class.
4. Function should run within the time complexity of O(E log V) where V is the total number of 
points/nodes/vertices in the road network; and E is the total number of roads/edges in the road 
network. 
<br />The space complexity remains the same as the space complexity of your input graph O(E + V).

<br />

**Application Development Tools**
1. PyCharm
