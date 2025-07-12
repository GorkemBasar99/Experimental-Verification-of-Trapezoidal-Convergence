import numpy as np

# Composite-Trapezoidal Rule


def summed_trapezoidal_rule(f, a, b, tol, maxL=1000):
    h = b - a
    L = 1
    T = h * (f(a) + f(b)) / 2  # trapezoidal initialize
    eval_points = [(a, f(a)), (b, f(b))]

    for k in range(maxL):
        midpoints = a + (np.arange(L) + 0.5) * h
        M = h * np.sum(f(midpoints))
        eval_points.extend([(mid, f(mid)) for mid in midpoints])

        # Update trapezoidal using midpoint
        T = (T + M) / 2
        error = np.abs(T - M)

        if error < tol:
            break

        # Next iteration
        h /= 2
        L *= 2

    else:
        raise Exception(
            "The stopping criteria were not met within the max number of iterations.")

    return T, len(eval_points), eval_points


# Adaptive Trapez
def TrapezAdaptivVorlage(f, a, b, TOL, max_evals=1000, hmin=1e-5):
    eval_count = [2]
    points = [(a, f(a)), (b, f(b))]

    def TrapezRek(f, a, b, fa, fb, TOL, hmin):
        h = b - a
        if h < hmin:
            raise ValueError("Interval length below minimum threshold.")

        mid = (a + b) / 2
        fm = f(mid)
        eval_count[0] += 1
        points.append((mid, fm))

        if not np.isfinite(fm):
            raise ValueError(
                "Function evaluation resulted in a non-finite value.")

        r = fa + fb
        I1 = h / 2 * r  # Initial trapezoidal approximation
        h = h / 2
        I2 = h * (r / 2 + fm)  # Improved trapezoidal approximation

        # Extrapolation (Simpson):
        I = (4 * I2 - I1) / 3

        if eval_count[0] > max_evals:
            raise ValueError(
                "Exceeded maximum number of function evaluations.")

        if abs(I - I2) > TOL:
            #Recursive call for right half and left half
            Irek1 = TrapezRek(f, a, mid, fa, fm, TOL, hmin)
            Irek2 = TrapezRek(f, mid, b, fm, fb, TOL, hmin)
            I = Irek1 + Irek2

        return I

    fa, fb = f(a), f(b)
    if not np.isfinite(fa) or not np.isfinite(fb):
        raise ValueError("Function evaluation resulted in a non-finite value.")

    result = TrapezRek(f, a, b, fa, fb, TOL, hmin)
    return result, eval_count[0], points


# Adaptive Simpson

def AdaptiveSimpsonsRule(f, a, b, TOL, max_evals=10000, hmin=1e-5):
    eval_count = [3]  # Initial evaluations of f(a), f(b), and f(mid)
    mid = (a + b) / 2
    fa, fb, fm = f(a), f(b), f(mid)
    points = [(a, fa), (b, fb), (mid, fm)]

    def SimpsonsRek(f, a, b, fa, fb, fm, TOL, hmin):
        if eval_count[0] > max_evals:
            raise ValueError(
                "Exceeded maximum number of function evaluations.")

        h = b - a
        if h < hmin:
            raise ValueError("Interval length below minimum threshold.")

        mid = (a + b) / 2
        mid1 = (a + mid) / 2
        mid2 = (mid + b) / 2
        fm1 = f(mid1)
        fm2 = f(mid2)
        eval_count[0] += 2
        points.extend([(mid1, fm1), (mid2, fm2)])

        if not (np.isfinite(fm1) and np.isfinite(fm2)):
            raise ValueError(
                "Function evaluation resulted in a non-finite value.")

        S1 = h / 6 * (fa + 4 * fm + fb)  # Initial Simpson's approximation
        # Improved Simpson's approximation
        S2 = h / 12 * (fa + 4 * fm1 + 2 * fm + 4 * fm2 + fb)
        I = (16 * S2 - S1) / 15

        if abs(I - S2) > TOL:
            # Recursive call for right half and left half
            Irek1 = SimpsonsRek(f, a, mid, fa, fm, fm1, TOL, hmin)
            Irek2 = SimpsonsRek(f, mid, b, fm, fb, fm2, TOL, hmin)
            I = Irek1 + Irek2

        return I

    if not (np.isfinite(fa) and np.isfinite(fb) and np.isfinite(fm)):
        raise ValueError("Function evaluation resulted in a non-finite value.")

    result = SimpsonsRek(f, a, b, fa, fb, fm, TOL, hmin)
    return result, eval_count[0], points
