from math import log, sin, cos, sqrt

def regula_falsa(f, a, b, tol=1e-3, max_iter=100, verbose=True, decimals=4):
    """
    Regla Falsa para f(x)=0 en [a,b].
    Imprime una tabla con a, f(a), b, f(b), xr, f(xr) y error a 'decimals' decimales.
    """
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0, []
    if fb == 0:
        return b, 0, []
    if fa * fb > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos.")

    xr_prev = a
    historial = []

    # Formato de 4 decimales (configurable)
    nd = decimals
    num = f"{{:,.{nd}f}}"
    hdr = (
        "Iter |          a       f(a)           b       f(b)          xr       f(xr)       error\n"
        "-----+---------------------------------------------------------------------------------"
    )

    if verbose:
        print(hdr)

    for it in range(1, max_iter + 1):
        xr = b - fb * (a - b) / (fa - fb)
        fxr = f(xr)
        err = abs(xr - xr_prev)

        historial.append(
            {"it": it, "a": a, "fa": fa, "b": b, "fb": fb, "xr": xr, "fxr": fxr, "err": err}
        )

        if verbose:
            print(
                f"{it:4d} | "
                f"{num.format(a):>10} {num.format(fa):>10} "
                f"{num.format(b):>10} {num.format(fb):>10} "
                f"{num.format(xr):>10} {num.format(fxr):>10} {num.format(err):>10}"
            )

        if fxr == 0 or err < tol:
            return xr, it, historial

        # Mantener el cambio de signo
        if fa * fxr < 0:
            b, fb = xr, fxr
        else:
            a, fa = xr, fxr

        xr_prev = xr

    return xr, max_iter, historial


# ====== EJEMPLO RÁPIDO ======
if __name__ == "__main__":
    def f(x):
        return 2*x**3 + 8*x**2 - 3*x + 12

    def h(x):
        return x ** 3 - 3 * x ** 2 + 11 * x + 4 / 3


    def i(x):
        return sqrt(x + 2) - cos(x + 1)  # dominio: x >= -2


    def j(x):
        return (2 * x ** 4) / 3 + x ** 3 - 3 * x ** 2 + 5 * x + 9


    def g(x):
        return log(x + 2) + sin(x + 1)


    a, b = -1.5, 0.0  # hay cambio de signo: g(a)<0, g(b)>0
    raiz, iters, _ = regula_falsa(g, a, b, tol=1e-3, verbose=True, decimals=4)

    print("\nRaíz:", f"{raiz:.4f}", "  Iteraciones:", iters)
    print("\nResultado:")
    print(f"Raíz aproximada: {raiz:.4f}")
    print(f"Iteraciones: {iters}")
    print(f"f(raíz) ≈ {f(raiz):.4f}")


