import sys
import importlib
import gd_animation


def run():
    try:
        if len(sys.argv) < 2:
            raise ImportError

        debug = False
        i = 1
        if sys.argv[i] == "-d":
            debug = True
            i += 1

        if module := sys.argv[i]:
            module = importlib.import_module(module)
            fun = getattr(module, "Fun")()
            gd_animation.animate(fun, debug)

    except ImportError:
        print("Function import failed.")


if __name__ == "__main__":
    run()
