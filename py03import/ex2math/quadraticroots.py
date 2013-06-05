#!/usr/bin/env python


"""Function that returns roots for a second degree polynomial.
"""

import cmath


def solveQuadraticRoots(A, B, C):
    # FIXME: convert x1, x2 from complex to float type if the roots are real.
    """Solve roots of a quadratic polynomial A*x**2 + B*x + C
    """
    det = cmath.sqrt(B**2 - 4 * A * C)
    x1 = (-B + det) / (2 * A)
    x2 = (-B - det) / (2 * A)
    return [x1, x2]
