N = 54
expected = [3**i for i in range(N)]


def assert3powers(step, function):
    print(step)
    for n in range(N):
        print(n, function(n))
    assert expected == [function(n) for n in range(N)], step


assert3powers(
    "3**i = 1+2*sum(3**i for i in range(n))",
    lambda n: 1 + 2 * sum(3**i for i in range(n)),
)

assert3powers(
    "Apply again in the inner formula",
    lambda n: 1 + 2 * sum(1 + 2 * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "Extract constant term",
    lambda n: 1 + 2 * n + 2 * sum(2 * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "Extract constant factor",
    lambda n: 1 + 2 * n + 4 * sum(sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "Count summations",
    lambda n: 1 + 2 * n + 4 * sum((n - i - 1) * (3**i) for i in range(n)),
)

assert3powers(
    "Apply again",
    lambda n: 1
    + 2 * n
    + 4 * sum((n - i - 1) * (1 + 2 * sum(3**j for j in range(i))) for i in range(n)),
)

assert3powers(
    "Extract constant term",
    lambda n: 1
    + 2 * n
    + 4 * sum((n - i - 1) for i in range(n))
    + 4 * sum((n - i - 1) * 2 * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "i' = n-i-1; 0<=i, 0<=n-i-1, i<=n-1, i<n ; i<n, n-i-1<n -i-1<0, i>-1 i>=0 ",
    lambda n: 1
    + 2 * n
    + 4 * sum(i for i in range(n))
    + 4 * sum((n - i - 1) * 2 * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "sum(i for i in range(n)) = n*(n-1)/2",
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum((n - i - 1) * 2 * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "extract factor 2",
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8 * sum((n - i - 1) * sum(3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    "moved factor inside",
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8 * sum(sum((n - i - 1) * 3**j for j in range(i)) for i in range(n)),
)

assert3powers(
    """
    0<=j<i, 0<=i<n,
    0<=j<n-1, j+1<=i<n, 
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8 * sum(sum((n - i - 1) * 3**j for i in range(j + 1, n)) for j in range(n - 1)),
)
assert3powers(
    """
    i'=i-j-1
    i=i'+j+1
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8
    * sum(
        sum((n - i - j - 2) * 3**j for i in range(n - j - 1)) for j in range(n - 1)
    ),
)
assert3powers(
    """
    Extracted 3**j
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8
    * sum(
        sum((n - i - j - 2) for i in range(n - j - 1)) * 3**j for j in range(n - 1)
    ),
)
assert3powers(
    """
    0<=i<=n-j-2
    i' = n-j-2-i
    0<=n-j-2-i'<=n-j-2
    -n-j-2<=-i'<=0
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8 * sum(sum(i for i in range(n - j - 1)) * 3**j for j in range(n - 1)),
)
assert3powers(
    """
    sum(i for i in range(n - j - 1)) = (n-j-2)(n-j-1)/2
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 8 * sum((n - j - 2) * (n - j - 1) / 2 * 3**j for j in range(n - 1)),
)
assert3powers(
    """
    sum(i for i in range(n - j - 1)) = (n-j-2)(n-j-1)/2
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum((n - j - 2) * (n - j - 1) * 3**j for j in range(n - 1)),
)
assert3powers(
    """
    j -> i
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum((n - i - 2) * (n - i - 1) * 3**i for i in range(n - 1)),
)
assert3powers(
    """
    3**i = 1 + 2 * sum(3**j for j in range(i))
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4
    * sum(
        (n - i - 2) * (n - i - 1) * (1 + 2 * sum(3**j for j in range(i)))
        for i in range(n - 1)
    ),
)
assert3powers(
    """
    Extract constant term
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum((n - i - 2) * (n - i - 1) for i in range(n - 1))
    + 4
    * sum(
        (n - i - 2) * (n - i - 1) * 2 * sum(3**j for j in range(i))
        for i in range(n - 1)
    ),
)
assert3powers(
    """
    Extract constant factor
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum((n - i - 2) * (n - i - 1) for i in range(n - 1))
    + 8
    * sum(
        (n - i - 2) * (n - i - 1) * sum(3**j for j in range(i)) for i in range(n - 1)
    ),
)
assert3powers(
    """
    i' = i-n+2
    i = i'+n-2
    0<=i<=n-2
    0<=i+n-2<=n-2
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * sum(i * (i + 1) for i in range(n - 1))
    + 8
    * sum(
        (n - i - 2) * (n - i - 1) * sum(3**j for j in range(i)) for i in range(n - 1)
    ),
)
assert3powers(
    """
    sum(i*i + i for i in range(n-1))
    = sum(i*i for i in range(n-1)) + sum(i for i in range(n-1))
    = k*(k+1)*(2*k+1)/6 + k*(k+1)/2 | k = n-2
    = (n-2)*(n-1)*(2*n-3)/6 + (n-2)*(n-1)/2
    = (n-2)*(n-1)/6 * (2*n-3 +3)
    = n*(n-1)*(n-2)/3
    """,
    lambda n: 1
    + 2 * n
    + 2 * n * (n - 1)
    + 4 * n * (n - 1) * (n - 2) / 3
    + 8
    * sum(
        (n - i - 2) * (n - i - 1) * sum(3**j for j in range(i)) for i in range(n - 1)
    ),
)
assert3powers(
    """
    Hypo: sum ( 2^n * n! / (n-i)! / i! )
    """,
    lambda n: 1
    + 2 * n / 1
    + 4 * n * (n - 1) / 2
    + 8 * n * (n - 1) * (n - 2) / 2 / 3
    + 8
    * sum(
        (n - i - 2) * (n - i - 1) * sum(3**j for j in range(i)) for i in range(n - 1)
    ),
)


def fact(
    n,
):
    return n * fact(n - 1) if n else 1


assert3powers(
    """
    Hypo: sum ( 2^i * n! / (n-i)! / i! )
    """,
    lambda n: sum(2**i * fact(n) // fact(n - i) // fact(i) for i in range(n + 1)),
)


def binomial_coef(i, n):
    return fact(n) / fact(n - i) / fact(i)


assert3powers(
    """
    Using factorial based binomial_coef function
    """,
    lambda n: sum(2**i * binomial_coef(i, n) for i in range(n + 1)),
)


def binomial_coef(k, n):
    return (n + 1 - k) * binomial_coef(k - 1, n) // k if k else 1


assert3powers(
    """
    Using single recursion version of binomial_coef
    """,
    lambda n: sum(2**i * binomial_coef(i, n) for i in range(n + 1)),
)
