<h1> Gradient Descent Animation </h1>

<p> Simple code showing gradient descent animation for a given function. The gradients are normalized by dividing them with magnitude of the gradient. </p>

<p><strong>Requirements: </strong> numpy and matplotlib

<h3> Execution</h3>

<p> Run the main file with the name of file (without .py) that contains the function. If '-d' flag is set, the program will output the following - iteration_number, x, y, fun(x, y). e.g. To run gradient descent animation for fun1 use - </p>
```python main.py -d fun1```

<h3>Adding custom function</h3>

1. Create a new python file with any name.
2. Import numpy (if required) and <strong>AbsFun</strong> class from <strong>fun</strong>.
3. Create a new class named <strong>Fun</strong> extending the class AbsFun and call the AbsFun constructor to initiallize the variables.
4. Implement <strong>get</strong> method as f(x,y), <strong>dx</strong> as partial derivative of f w.r.t. x and <strong>dy</strong> as partial derivative of f w.r.t. y. You can check your 3d function here - https://www.math3d.org/
5. Set these variables as per your desired preference.
    5.1 <em>n</em> = number of iterations
    5.2 <em>xrange</em> = a tuple specifying range of x that is used to draw the function.
    5.3 <em>yrange</em> = a tuple specifying range of y that is used to draw the function
    5.4 <em>init_point</em> = a tuple (x,y) describing the initial point from where the animation starts
    5.5 <em>rate</em> = A decimal value describing how large each step is. Default is 1
    5.6 <em>name</em> = Function name (or formula) that will displayed as title. The program will add 'f(x,y) = ' before the name.
    5.7 <em>count</em> = Used to create a mesh for plotting the function. Default is 20
