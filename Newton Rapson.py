import math

# --- Define función y derivada ---
def f(x):
    return 2*x**3 + 8*x**2 - 3*x + 12

def df(x):
    return 6*x**2 + 16*x - 3

# --- Metodo de Newton-Raphson ---
def newton(f, df, x0, tol=1e-10, max_iter=100, verbose=True):
    x = x0
    if verbose:
        print(f"{'n':>3} {'x_n':>14} {'f(x_n)':>14} {'f\'(x_n)':>14} {'x_{n+1}':>14}")
        print("-"*65)
    for n in range(1, max_iter+1):
        dfx = df(x)
        if abs(dfx) < 1e-14:
            raise ZeroDivisionError(
                f"Derivada casi nula en x={x:.12g}. Prueba con otro x0."
            )
        fx = f(x)
        x_next = x - fx/dfx
        if verbose:
            print(f"{n:3d} {x:14.10f} {fx:14.10f} {dfx:14.10f} {x_next:14.10f}")
        if abs(x_next - x) < tol:
            return x_next, n
        x = x_next
    # Si no converge en max_iter
    return x, max_iter

if __name__ == "__main__":
    # Parámetros (puedes cambiarlos)
    x0 = -5.0     # valor inicial sugerido
    tol = 1e-12   # tolerancia de paro
    max_iter = 50

    root, iters = newton(f, df, x0, tol=tol, max_iter=max_iter, verbose=True)
    print("\nRaíz aproximada:", f"{root:.12f}")
    print("Iteraciones usadas:", iters)
    print("Chequeo f(raíz):   ", f"{f(root):.3e}")
