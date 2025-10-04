from math import log as ln, sin, isfinite

def secant(func, x0, x1, tol=1e-10, max_iter=100, safe_domain=None, verbose=False):
    if x0 == x1:
        raise ValueError("x0 and x1 must be different")

    def in_domain(x):
        return True if safe_domain is None else bool(safe_domain(x))

    x_prev, x_curr = x0, x1
    f_prev = func(x_prev) if in_domain(x_prev) else float("nan")
    f_curr = func(x_curr) if in_domain(x_curr) else float("nan")

    history = [(0, x_prev, f_prev), (1, x_curr, f_curr)]
    if verbose:
        print(f"{'k':>3} | {'x_k':>20} | {'f(x_k)':>20}")
        print("-"*50)
        print(f"{0:>3} | {x_prev:>20.12f} | {f_prev:>20.12e}")
        print(f"{1:>3} | {x_curr:>20.12f} | {f_curr:>20.12e}")

    for k in range(1, max_iter+1):
        denom = f_curr - f_prev
        if not isfinite(denom) or abs(denom) < 1e-18:
            raise ZeroDivisionError("Denominator too small or not finite in secant update.")
        x_next = x_curr - f_curr * (x_curr - x_prev) / denom

        if not in_domain(x_next) or not isfinite(x_next):
            raise ValueError(f"Next iterate x={x_next} is outside function domain or not finite.")

        f_next = func(x_next)
        history.append((k+1, x_next, f_next))

        if verbose:
            print(f"{k+1:>3} | {x_next:>20.12f} | {f_next:>20.12e}")

        if abs(x_next - x_curr) < tol:
            return x_next, k+1, history

        x_prev, f_prev = x_curr, f_curr
        x_curr, f_curr = x_next, f_next

    return x_curr, max_iter, history


def fixed_point(phi, x0, tol=1e-10, max_iter=200, safe_domain=None, verbose=False):
    def in_domain(x):
        return True if safe_domain is None else bool(safe_domain(x))

    if not in_domain(x0) or not isfinite(x0):
        raise ValueError("Initial guess x0 is outside domain or not finite.")

    x = x0
    history = [(0, x)]
    if verbose:
        print(f"{'k':>3} | {'x_k':>20}")
        print("-"*30)
        print(f"{0:>3} | {x:>20.12f}")

    for k in range(1, max_iter+1):
        x_next = phi(x)
        if not in_domain(x_next) or not isfinite(x_next):
            raise ValueError(f"Iterate x={x_next} is outside domain or not finite.")
        history.append((k, x_next))

        if verbose:
            print(f"{k:>3} | {x_next:>20.12f}")

        if abs(x_next - x) < tol:
            return x_next, k, history
        x = x_next

    return x, max_iter, history


# Example functions
def f(x):
    return 2*x**3 + 8*x**2 - 3*x + 12

def g(x):
    return ln(x+2) + sin(x+1)

def domain_g(x):
    return x > -2


if __name__ == "__main__":
    print("=== Secant Method Demo ===")
    try:
        root_f, it_f, _ = secant(f, x0=-5.0, x1=-4.0, tol=1e-12, max_iter=100, verbose=True)
        print(f"\nRoot for f(x)=0: x ≈ {root_f:.12f}  (iterations: {it_f})")
    except Exception as e:
        print("Secant on f failed:", e)

    try:
        root_g, it_g, _ = secant(g, x0=-1.5, x1=-0.5, tol=1e-12, max_iter=100, safe_domain=domain_g, verbose=True)
        print(f"\nRoot for g(x)=0: x ≈ {root_g:.12f}  (iterations: {it_g})")
    except Exception as e:
        print("Secant on g failed:", e)

    print("\\n=== Fixed-Point (Picard) Demo for x = g(x) ===")
    try:
        phi = g
        x_fp, it_fp, _ = fixed_point(phi, x0=1.0, tol=1e-12, max_iter=200, safe_domain=domain_g, verbose=True)
        print(f"\\nFixed point of x=g(x): x ≈ {x_fp:.12f}  (iterations: {it_fp})")
    except Exception as e:
        print("Fixed-point on x=g(x) failed:", e)
