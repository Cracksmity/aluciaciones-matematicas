from math import log2, ceil

def f(x: float) -> float:
    return (3/4)*x**3 + 2*x**2 + x - 9

# Tolerancia sobre la longitud del intervalo
eps = 1e-3

# Utilidad: símbolo del signo
def simbolo_signo(v: float) -> str:
    return "-" if v < 0 else ("+" if v > 0 else "0")

# Utilidad: formato fix-4
fmt = lambda x: f"{x:.4f}"

# 1) Encontrar [a,b] con cambio de signo en [-100, 100]
a = b = None
x_prev, f_prev = None, None
for i in range(-100, 101):
    xi  = float(i)
    fxi = f(xi)
    if fxi == 0.0:
        a = b = xi
        print(f"Raíz exacta en x = {fmt(xi)}")
        break
    if f_prev is not None and f_prev * fxi < 0:
        a, b = x_prev, xi
        break
    x_prev, f_prev = xi, fxi

if a is None:
    raise ValueError("No se encontró un intervalo con cambio de signo en [-100, 100].")


# 2) Iteraciones teóricas
N = ceil(log2((b - a) / eps))
print(f"Intervalo inicial: [{fmt(a)}, {fmt(b)}]  |b-a|={fmt(abs(b-a))}")
print(f"Iteraciones teóricas (eps={eps}): N = {N}")

# 3) Bisección con salidas fix-4
fa, fb = f(a), f(b)
for k in range(1, N + 1):
    m  = (a + b) / 2
    fm = f(m)
    print(
        f"iter {k:02d}: m={fmt(m)}  f(m)={fmt(fm)}  "
        f"signo={simbolo_signo(fm)}  [a,b]=[{fmt(a)}, {fmt(b)}]  |b-a|={fmt(b-a)}"
    )

    if fm == 0.0:
        a = b = m
        fa = fb = fm
        break

    # Actualizar intervalo sin recalcular extremos innecesariamente
    if fa * fm < 0:
        b, fb = m, fm
    else:
        a, fa = m, fm

x_aprox = (a + b) / 2
print(f"≈ raíz en x={fmt(x_aprox)}  con |b-a|={fmt(abs(b-a))}")



