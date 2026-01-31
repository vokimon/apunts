# =========================
# Collatz symbolic BFS
# =========================

from sympy import (
    symbols, And, Or, Not,
    Eq, Mod, simplify
)
from collections import deque


# -------------------------
# Symbol
# -------------------------

n = symbols('n', integer=True, positive=True)


# -------------------------
# Domain knowledge
# -------------------------

# Known lower bound for a minimal irreducible number (if it exists)
DOMAIN = n > 2**68


# -------------------------
# Odd predecessor existence
# -------------------------

def odd_predecessor_existence_condition(parent_value):
    """
    Odd predecessor exists iff (2*parent_value - 1) is divisible by 3.
    """
    return Eq(Mod(2*parent_value - 1, 3), 0)


# -------------------------
# Contradiction checker
# -------------------------

def is_contradiction(cond):
    """
    Returns True only if SymPy can prove the condition is False.
    """
    try:
        return simplify(cond) is False
    except Exception:
        return False


# -------------------------
# Breadth-first predecessor analysis
# -------------------------

def predecessor_bfs(
    n,
    max_depth=3,
    domain_condition=True
):
    """
    Breadth-first symbolic predecessor exploration.

    Returns:
        A SymPy Boolean expression representing an OR of all
        inviability conditions for n being the minimal irreducible.
    """

    # Each state: (value, exists_condition, viability_condition, depth)
    queue = deque()
    queue.append((n, True, True, 0))

    # OR accumulator of inviability conditions
    inviability = False

    print("\n=== BFS START ===\n")

    while queue:
        value, exists, viable, depth = queue.popleft()

        print(f"[depth {depth}]")
        print(" value  =", value)
        print(" exists =", exists)
        print(" viable =", viable)

        # ---------------------------------
        # Emit inviability condition
        # ---------------------------------

        branch_inviable = And(exists, Not(viable))
        inviability = Or(inviability, branch_inviable)

        print("  -> emits inviability:", branch_inviable)

        # ---------------------------------
        # Check if branch can continue
        # ---------------------------------

        branch_ok = And(exists, viable, domain_condition)

        if is_contradiction(branch_ok):
            print("  ✗ branch impossible, stop\n")
            continue

        if depth >= max_depth:
            print("  ↳ max depth reached\n")
            continue

        # ---------------------------------
        # Even predecessor
        # ---------------------------------

        even_value = 2 * value
        even_exists = exists
        even_viable = And(viable, even_value >= n)

        print("  → even predecessor")

        queue.append((
            even_value,
            even_exists,
            even_viable,
            depth + 1
        ))

        # ---------------------------------
        # Odd predecessor
        # ---------------------------------

        odd_exists_local = odd_predecessor_existence_condition(value)
        odd_value = (2 * value - 1) / 3
        odd_exists = And(exists, odd_exists_local)
        odd_viable = And(viable, odd_value >= n)

        print("  → odd predecessor")

        queue.append((
            odd_value,
            odd_exists,
            odd_viable,
            depth + 1
        ))

        print()

    print("=== BFS END ===\n")

    return simplify(inviability)


# -------------------------
# Run analysis
# -------------------------

if __name__ == "__main__":

    inviability_condition = predecessor_bfs(
        n,
        max_depth=6,
        domain_condition=DOMAIN
    )

    print("FINAL INVIABILITY CONDITION:\n")
    print(inviability_condition)
