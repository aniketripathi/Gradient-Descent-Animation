import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(fun, debug=False):
    n = fun.n + 1
    xstart, xend = fun.xrange
    ystart, yend = fun.xrange
    rate = fun.rate
    m = fun.count
    title = "f(x,y) = " + fun.name
    get = fun.get
    dx = fun.dx
    dy = fun.dy
    dlen = fun.dlen

    xdata = np.zeros(n)
    ydata = np.zeros(n)
    zdata = np.zeros(n)

    # plot surface
    x = np.linspace(xstart, xend, m)
    y = np.linspace(ystart, yend, m)
    X, Y = np.meshgrid(x, y)
    Z = get(X, Y)
    fig = plt.figure()
    fig.tight_layout()
    ax = plt.axes(projection="3d")
    ax.set_title(title)
    ax.plot_wireframe(X, Y, Z, zorder=1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x,y)")
    ax.set_label(title)

    def init():
        xdata[0], ydata[0] = fun.init_point
        zdata[0] = get(xdata[0], ydata[0])

    def update(i):
        u = xdata[i]
        v = ydata[i]
        z = zdata[i]
        d_x = dx(u, v)
        d_y = dy(u, v)
        d_len = dlen(u, v)

        if debug:
            print(i, round(u, 4), round(v, 4), round(z, 4))

        if d_len > 0:
            xdata[i + 1] = u - d_x / d_len * rate
            ydata[i + 1] = v - d_y / d_len * rate
            zdata[i + 1] = get(u, v)

            ax.plot(
                [u, xdata[i + 1]],
                [v, ydata[i + 1]],
                [z, zdata[i + 1]],
                lw=5,
                color="red",
                zorder=2,
            )

    anim = animation.FuncAnimation(
        fig, update, frames=range(n - 1), init_func=init, repeat=False
    )
    plt.show()
