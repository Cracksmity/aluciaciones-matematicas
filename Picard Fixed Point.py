# Metodo de Picard para f(x)=2x^3+8x^2-3x+12
# g(x) = -4 + (3x - 12) / (2x^2)

from math import isfinite

def f(x):
    return 2*x**3 + 8*x**2 - 3*x + 12

def g(x):
    if x == 0:  # evitar división por 0 en g(x)
        raise ZeroDivisionError("g(x) no está definida en x=0.")
    return -4 + (3*x - 12) / (2*x**2)

def picard(g, f, x0, tol=1e-3, max_iter=100, stop_on_residual=False):
    """
    Iteración de punto fijo x_{n+1} = g(x_n).
    - stop_on_residual=False: para cuando |x_{n+1}-x_n| < tol
    - stop_on_residual=True : para cuando |f(x_n)| < tol
    """
    x = float(x0)
    print(f"{'n':>3} | {'x_n':>14} | {'|Δx|':>12} | {'|f(x_n)|':>12}")
    print("-"*50)
    prev = None
    for n in range(0, max_iter+1):
        fx = f(x)
        dx = abs(x - prev) if prev is not None else float('nan')
        print(f"{n:>3} | {x:>14.6f} | {dx:>12.6f} | {abs(fx):>12.6f}")
        # criterio de paro
        if stop_on_residual and abs(fx) < tol and n > 0:
            return x, n, "residual"
        if not stop_on_residual and prev is not None and dx < tol:
            return x, n, "delta"
        # siguiente iteración
        prev = x
        xn1 = g(x)
        if not isfinite(xn1):
            raise ArithmeticError("La iteración produjo un valor no finito.")
        x = xn1
    return x, max_iter, "max_iter"

if __name__ == "__main__":
    # Parámetros
    x0 = -4.0       # punto inicial (puedes probar -5, -3, etc.)
    tol = 1e-3
    max_iter = 100

    # Opción A: parar por diferencia sucesiva |Δx| < tol
    root, iters, why = picard(g, f, x0, tol=tol, max_iter=max_iter, stop_on_residual=False)
    print("\nResultado (criterio |Δx|):")
    print(f"x* ≈ {root:.6f} en {iters} iteraciones (motivo: {why})")

    # Opción B: parar por residual |f(x)| < tol
    root, iters, why = picard(g, f, x0, tol=tol, max_iter=max_iter, stop_on_residual=True)
    print("\nResultado (criterio |f(x)|):")
    print(f"x* ≈ {root:.6f} en {iters} iteraciones (motivo: {why})")
