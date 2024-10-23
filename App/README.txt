# Food-Map

Food Map is a project by Mikaela Amon, Thara Corpuz, Zhean Ganituen, Aaron Go, and Emmanuel Punsalan for **Introduction to Intelligent Systems**. 

## How To

1. (Optional) Create and use a Python [virtual environment](https://docs.python.org/3/library/venv.html)
2. Install the dependencies
3. Running the code

> You can combine step (1) and (2) by simply running the batch file `init` but this only works for the Windows Command Prompt.

### Installing dependencies

The dependencies of this project are:

* [NetworkX](https://networkx.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [Indexed Priority Queue](https://github.com/gabrielbazan/indexed_priority_queue)
* [Colorama](https://pypi.org/project/colorama/)

To install these, run the following command:

> If the you have the virtual environment remember to be inside `venv`.

```
pip install -r requirements.txt
```

### Using `venv`
(optional) set up a Python virtual environment first. To set this up run the following code:

Initialize python virtual environment as venv

```
python -m venv venv
```

Activate the virtual environment

```
venv\Scripts\activate
```

Your terminal should now look like

```
(venv) C:\Users\..
```

### Using the code

Simply run:

```
$ python App/main.py
```

> Or, if you are in Windows Command Prompt, simply run the batch file: 
> ```
> $ rrr
> ```

#### Inside the main file:

The main file has the following commands: 

1. **make**
   - **Description:** Initialize the graph using predefined rules. Input format: `make`

2. **exit**
   - **Description:** Exit the program. Input format: `exit`

3. **set start**
   - **Description:** Set the start index to the specified number. Input format: `set start <vertex>`
   - `<vertex>` is the numerical value representation of the vertex.

4. **set goal**
   - **Description:** Set the goal index to the specified number. Input format: `set goal <vertex>`
   - `<vertex>` is the numerical value representation of the vertex.
  
5. **view**
   - **Description:** View the current graph. Input format: `view`

6. **view result**
   - **Description:** View the graph with start, end vertices, and the result of the algorithm as the path. Input format: `view result <algorithm>`
   - `<algorithm>` is `dfs`, `ucs`, `a*` or `a_star`.

7. **show start**
   - **Description:** Show the current start index. Input format: `show start`

8. **show goal**
   - **Description:** Show the current goal index. Input format: `show goal`

9. **add vertex**
   - **Description:** Add a vertex to the graph. Input format: `add vertex <vertex>`
   - `<vertex>` is the numerical value representation of the vertex.

10. **del vertex**
   - **Description:** Delete a vertex from the graph. Input format: `del vertex <vertex>`
   - `<vertex>` is the numerical value representation of the vertex.

11. **add edge**
   - **Description:** Add an edge to the graph. Input format: `add edge <u> <v>`
   - `<u> <v>` are the end points of the edge separated by a space.
  
12. **del edge**
   - **Description:** Delete an edge from the graph. Input format: `del edge <u> <v>`
   - `<u> <v>` are the end points of the edge separated by a space.

**Input the `?` command to get a list of commands**.

#### Command Sequence

Run `make` command first to create a graph.
Then, run the `set start <vertex>` and `set goal <vertex>`.
To verify the graph is created with the correct start and goal nodes run `view`.
To view the result of the three algorithms (UCS, DFS, and A*) run the command `view result <algorithm>`.