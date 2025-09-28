---
title: Metric Spaces
up:
  - [[maths/topology]]
---

<!-- PARENT: auto -->
Parent: [[maths/topology|topology]]
<!-- /PARENT -->

**Definition.**  
A **metric space** is a pair $(X,d)$ where $d:X\times X\to \mathbb{R}$ satisfies:

1. $d(x,y)\ge 0$ with equality iff $x=y$,  
2. $d(x,y)=d(y,x)$,  
3. $d(x,z)\le d(x,y)+d(y,z)$ (triangle inequality).

---

## Relation to Topology

- Every metric induces a topology via **open balls**.  
- Thus every metric space is a topological space, but not every topological space is metrizable.

---

## Cross-links

- Compactness in metric spaces → TODO
- Connectedness in metric spaces → TODO
- Homotopy theory uses path-connectedness → [[maths/algebraic-topology/homotopy|homotopy]]  
- Algebraic invariants often assume underlying metric/topological structure → [[maths/algebraic-topology|algebraic topology]]
