# Writting formal papers

## Core structural elements

### Definition

**Purpose:** Fix meaning precisely.

**Use when:** You introduce a new object, concept, or condition.

**Rules of thumb:**

- No proofs in definitions
- Should be unambiguous and reusable
- Everything that follows depends on this
- Highlight the term

### Lemma

**Purpose:** A technical result used to prove something else.

**Use when:** The result is important to reach the goal but not the “main point.”

**Typical traits**

* Often structural or restrictive
* Frequently reused
* Can be very powerful even if “small”

TODO: Lemma includes a proof?

### Theorem

**Purpose:** A main result or milestone.

**Use when:** You want to signal significance.

**Notes**

- “Theorem” is about *importance*, not difficulty
- In speculative work, theorems may be conditional (“If…, then…”)

### Proposition

**Purpose:** A result that’s useful but not central.

**Use when:** It’s stronger than a lemma, weaker than a theorem.

Often interchangeable with “lemma,” but slightly more self-contained.

### Corollary

**Purpose:** A result that follows almost immediately from another.

**Use when:** Minimal extra reasoning is required.

Good signals

* Proof is very short
* Depends directly on one named result

## Supporting elements

### Example

**Purpose:** Illustrate, not prove.

**Use when:** You want to show *how* something works.

**Important**

- Examples do **not** establish general truth
- They help intuition and readability


### **Remark**

**Purpose:** Clarify, contextualize, or warn.

**Use when:** Something is useful but not part of the proof.

Common uses:

- Explain intuition
- Note limitations
- Connect to known results
- Justify why something is interesting

### **Observation**

**Purpose:** State something evident or lightly justified.

**Use when:** The result is simple and not worth a full lemma.

Often informal but still precise.

## Logical flow elements

### Proof

**Purpose:** Establish truth rigorously.

Conventions:

* Start with **“Proof.”**
* End with **□** or **QED**
* Avoid storytelling; focus on logic
* Use complete sentences (this matters more than people think)

### **Claim**

**Purpose:** A sub-result inside a proof.

**Use when:** You need a temporary lemma.

Useful for long or nested arguments.

### **Assumption / Hypothesis**

**Purpose:** Fix the logical universe.

**Use when:** Working conditionally.

Make assumptions explicit early and remind the reader when needed.

## Meta-structure elements

### **Notation**

**Purpose:** Reduce clutter and ambiguity.

**Use when:** Symbols recur.

> *Notation.* Let ( T(n) ) denote the Collatz map.

### **Convention**

**Purpose:** Declare default interpretations.

**Use when:** Avoiding repeated caveats.

> *Convention.* All integers are positive unless stated otherwise.


## How these work together (typical pattern)

1. Definitions fix the setting
2. Lemmas restrict structure
3. Corollaries eliminate cases
4. Remarks explain meaning or direction
5. Theorem collects the payoff

## One guiding principle (very important)

> **The name of a statement tells the reader how hard to pay attention.**

- Definition → memorize
- Lemma → trust and reuse
- Corollary → quick consequence
- Remark → helpful but skippable


