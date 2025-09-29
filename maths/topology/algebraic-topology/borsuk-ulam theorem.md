---
title: Borsuk–Ulam Theorem
up:
  - [[maths/algebraic-topology]]
---

<!-- PARENT: auto -->
Parent: [[algebraic-topology|algebraic topology]]
<!-- /PARENT -->

# Borsuk–Ulam Theorem

**Theorem (Borsuk–Ulam).**  

For any continuous map $$ f : S^n \to \mathbb{R}^n $$ there exists a point $$ x \in S^n $$ such that
$$
f(x) = f(-x).
$$
In other words, if you continuously squash a (2)-sphere into the plane, at least one pair of antipodal points on the sphere will be mapped to the same point.

---
## 1-dimensional case

Let $f : S^1 \to \mathbb{R}$. Define
$$
g(x) = f(x) - f(-x).
$$
Then $g$ is continuous and **odd** (i.e. $g(-x) = -g(x)$).

- If $g(x) = 0$ for some $x$, we are done.  
- Otherwise, suppose $g(x) > 0$ at some $x$. Then $g(-x) < 0$.  
- By the intermediate value theorem, $g$ must vanish somewhere in between.  

Hence $f(x) = f(-x)$ for some $x$.

---

## 2-dimensional case (sketch)

For $f : S^2 \to \mathbb{R}^2$, one can argue via covering space theory:

- Suppose no pair of antipodal points maps to the same place.  
- Construct an odd map $S^2 \to S^1$ by normalizing $f(x)-f(-x)$.  
- But there is no continuous odd map $S^2 \to S^1$ (since it would lift to a contradiction in $\mathbb{R}^2$ via the covering $S^1 \to \mathbb{R}P^1$).  

Thus the theorem holds for $n=2$.

---

## Sketch of Proof (via homology)

1. **Contrapositive setup.**  
   Assume no such $x$ exists, i.e. $f(x) \neq f(-x)$ for all $x$.

2. **Define an odd map.**  
   Construct  
   $$
   g(x) = \frac{f(x) - f(-x)}{\lVert f(x) - f(-x)\rVert} : S^n \to S^{n-1},
   $$
   which satisfies $g(-x) = -g(x)$.

3. **Descend to projective space.**  
   The antipodal symmetry means $g$ factors through real projective space:  
   $S^n \twoheadrightarrow \mathbb{R}P^n \xrightarrow{\;\tilde g\;} S^{n-1}$.

4. **Homological contradiction.**  
   - $H_n(\mathbb{R}P^n; \mathbb{Z}_2) \cong \mathbb{Z}_2$.  
   - $S^{n-1}$ has trivial $H_n$.  
   - So any map $\mathbb{R}P^n \to S^{n-1}$ must kill the top homology class.  
   - But construction forces a nontrivial map on top homology (degree considerations).

5. **Contradiction.**  
   Hence such a point $x$ must exist.

---

## Note: Even/Odd as Group Actions

For $f:\mathbb{R}\to\mathbb{R}$:

- **Even:** $f(-x)=f(x)$  
  → Invariant under the $\mathbb{Z}_2$ action $x \mapsto -x$ on the domain.  
  → Factors through the quotient $\mathbb{R}/(x\sim -x)$.

- **Odd:** $f(-x)=-f(x)$  
  → Equivariant for the $\mathbb{Z}_2$ action on both domain and codomain (sign action).  

In other words,

- *Even = $\mathbb{Z}_2$-invariant map.*  
- *Odd = $\mathbb{Z}_2$-equivariant map (with sign action on target).*

This is the perspective used in **equivariant topology**.