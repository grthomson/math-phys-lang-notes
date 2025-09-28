---
title: Brouwer Fixed Point Theorem
up:
  - [[maths/algebraic-topology]]
---

<!-- PARENT: auto -->
Parent: [[maths/algebraic-topology|algebraic topology]]
<!-- /PARENT -->

# Brouwer Fixed Point Theorem

**Theorem.**  
Every continuous map $f : D^n \to D^n$ has a fixed point:
$$
\exists x \in D^n \quad \text{with} \quad f(x) = x.
$$

Here $D^n = \{ x \in \mathbb{R}^n : \lVert x \rVert \le 1 \}$ is the closed $n$-disk.

---

## Low-dimensional proofs

### Case $n=1$ (interval)

Let $f:[0,1] \to [0,1]$ be continuous. Define $g(x) = f(x) - x$.

- $g(0) = f(0) \ge 0$,  
- $g(1) = f(1) - 1 \le 0$.  

By the Intermediate Value Theorem, $g$ must vanish at some $c \in [0,1]$, i.e. $f(c) = c$.

---

### Case $n=2$ (disk)

Suppose, for contradiction, that $f:D^2\to D^2$ has no fixed point.

1. **Build a retraction.**  
   For each $x\in D^2$, draw the ray from $f(x)$ through $x$.  
   This ray meets the boundary $S^1$ at a unique point $r(x)$.  
   Then $r:D^2\to S^1$ is continuous and satisfies $r|_{S^1}=\mathrm{id}_{S^1}$.  
   So $r$ is a **retraction**.

2. **Contradiction via fundamental groups.**  
   If $r$ exists, then $r \circ i = \mathrm{id}_{S^1}$ where $i:S^1 \hookrightarrow D^2$ is inclusion.  
   On $\pi_1$:  
   $$
   r_* \circ i_* = \mathrm{id}_{\pi_1(S^1)}.
   $$
   But $\pi_1(D^2)=0$, so $i_*$ is the zero map.  
   Contradiction.  

Hence $f$ must have a fixed point.

---

## Higher dimensions ($n \ge 3$)

The same retraction idea applies:

- **No fixed point assumption** gives a retraction $r: D^n \to S^{n-1}$.
- But topology forbids such a retraction.  
- Proving this requires **heavier tools**:

### Homology version
- $H_{n-1}(S^{n-1}) \cong \mathbb{Z}$,  
- $H_{n-1}(D^n) = 0$.  
- If a retraction existed, the induced map on homology would send a generator of $H_{n-1}(S^{n-1})$ to a nontrivial class in $H_{n-1}(D^n)$ — impossible.

### Degree theory version
- The identity on $S^{n-1}$ has degree $\pm 1$.  
- If it factored through $D^n$, the degree would have to be $0$.  
- Contradiction.

---

## Summary of methods

- **$n=1$:** Intermediate Value Theorem (analysis).  
- **$n=2$:** Fundamental group $\pi_1(S^1) \cong \mathbb{Z}$ (elementary algebraic topology).  
- **$n\ge 3$:** Homology or degree theory (higher algebraic topology).  

Thus the core of Brouwer’s theorem in *all* dimensions is the impossibility of retracting the disk $D^n$ onto its boundary $S^{n-1}$.
