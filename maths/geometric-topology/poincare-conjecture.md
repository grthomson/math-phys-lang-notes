---
id: 81tfolv0ye1e6yx4zdp51ft
title: Poincare Conjecture
desc: ''
updated: 1745157220152
created: 1744804328676
up:
  - [[maths/geometric-topology]]
---
# "Every closed smooth simply connected 3-manifold is diffeomorphic to S^(3)"

###  NB :
- Every topological 3-manifold can be equipped with a differentiable structure
- Every homeomorphism between smooth 3-manifolds can be approximated by a diffeomorphism
- Therefore statements about topological 3-manifolds up to homeomorphism are equivalent to statements about smooth 3-manifolds up to diffeomorphism
### In dimension 3:
- Every topological manifold admits a unique smooth structure (Moise's theorem),
- Every homeomorphism between smooth 3-manifolds is isotopic to a diffeomorphism,
- Therefore, classifying 3-manifolds up to homeomorphism is equivalent to classifying them up to diffeomorphism.

### A 3-manifold is a topological space 𝑀 such that every point has a neighborhood 𝑈 ⊂ 𝑀 which is homeomorphic to an open subset of 𝑅 3. 
- That is, ∀ 𝑝 ∈ 𝑀 there exists an open neighborhood 𝑈 of 𝑝 which admits a homeomorphism 𝜑 : 𝑈 → 𝑉 ⊂ 𝑅 3

### Not every topological manifold can be defined by an equivalent differentiable or smooth manifold - we need the transition maps for overlapping charts to be smooth

- A topological manifold has charts 𝜙_𝑖 : 𝑈_𝑖 → 𝑅^𝑛 where each 𝜙𝑖 is just a homeomorphism (continuous, with continuous inverse). The transition maps 𝜙_𝑗 ∘ 𝜙_𝑖^−1 ϕ j ​are homeomorphisms between open subsets of 𝑅^𝑛, but not necessarily smooth.

- We have a smooth manifold when the transition maps 𝜙_𝑗 ∘ 𝜙_𝑖^(−1) are all smooth wherever charts overlap.

### In dimension 3 it's always possible to find an atlas (a collection of charts) whose transition maps are smooth — i.e., you can promote the topological manifold to a smooth one.

### But this is nontrivial, and fails in other dimensions:

- In dimension 4 there are topological manifolds that do not admit any smooth structure at all. 

- In dimension 7+ some topological manifolds admit multiple inequivalent smooth structures (same underlying topology, different ways to define smoothness — e.g. exotic 𝑅^4).

### When is a manifold homeomorphic to a subset of 𝑅^𝑛? 

- Embedding: A manifold 𝑀 is said to be embedded in 𝑅^𝑁 if there is a smooth injective map 𝑓 : 𝑀 ↪ 𝑅^𝑁 whose image is homeomorphic (and diffeomorphic) to 𝑀, and which has an injective derivative everywhere. 
- Whitney's Embedding Theorem says that: Any smooth 𝑛-dimensional manifold can be embedded into 𝑅^2𝑛 R. So yes, eventually you can embed it into some big Euclidean space — just not necessarily in dimension 𝑛.

## Fibre Bundles

A fibre bundle is a quadruple ( 𝐸 , 𝑀 , 𝜋 , 𝐹 ) where: 

- 𝐸 (total space), 𝑀 (base space), and 𝐹 (fibre) are topological spaces, 
- 𝜋 : 𝐸 → 𝑀 is a continuous surjection, 
- For every 𝑝 ∈ 𝑀, there exists an open set 𝑈 ∋ 𝑝 and a homeomorphism 

𝜙 : 𝜋^(−1)(𝑈) → 𝑈 × 𝐹 

such that 𝜋 = pr_1 ∘ 𝜙. 

This expresses that: 𝜋^(− 1)( 𝑈 ) ≅ 𝑈 × 𝐹,  i.e. the bundle is locally a product space.

```
           φ
π⁻¹(U) ---------> U × F
  |                 |
  | π               | pr₁
  v                 v
   U  ----------->  U
          id
```

In simple terms we have a continuous surjection 𝜋 : E --> M and for any point in M, there is *some* containing open set U whose pre-image under 𝜋 is homoeomorphic to the product of U with F.

The product of open sets in M with the fibre F captures the "local product" aspect of E. Note that 𝜙 is a homeomorphism between U x F (in M x F) and 𝜋^(−1)(𝑈) (open in E).

### Example 1: Möbius Band 

We define the Möbius band as the quotient space: 

### 𝐸 : = ( [ 0 , 1 ] × 𝑅 ) / ∼ 
 with the equivalence relation: 
( 0 , 𝑦 ) ∼ ( 1 , − 𝑦 ) 


- Total space: Möbius band 𝐸 
- Base space: 𝑀 = 𝑆^1 (the circle) 
- Fibre: 𝐹 = 𝑅 

### Projection Map π
Define:
-  π: E → S¹
- π([x, y]) := x mod 1

This is well-defined because:

If (0, y) ∼ (1, –y), then x mod 1 gives the same point in S¹ = ℝ / ℤ.

So π is a continuous surjection, sending each fibre (a vertical line) to a point on the base circle.

Local Trivializations
Choose an open interval U ⊂ S¹ that avoids the gluing point (e.g., a small arc not containing the image of x = 0 or x = 1).

Then: π⁻¹(U) ⊂ E is homeomorphic to U × ℝ

This is because the gluing does not affect these interior regions.

Define the trivialization:

φ: π⁻¹(U) → U × ℝ
φ([x, y]) = (x mod 1, y)

### The circle S¹ is defined as ℝ / ℤ, so x mod 1 gives a point on the circle.

The circle S¹ is defined as the quotient ℝ / ℤ, so x mod 1 gives a point on the circle. This means we identify all real numbers that differ by an integer: x ∼ x + n for n ∈ ℤ. Geometrically, this wraps the real line into a circle by treating points like 0 and 1 as the same.

The projection π([x, y]) = x mod 1 sends each point on the Möbius band to its basepoint on S¹.

Here, the Möbius band is defined as the quotient space:

E = ([0,1] × ℝ) / (0, y) ∼ (1, –y)
The projection map π sends the class [x, y] ∈ E to the class of x ∈ [0,1] in ℝ / ℤ, i.e., to a point on the circle. This makes S¹ the base space, and the vertical lines in the strip (the fibres) map to points on the circle.

Over small open intervals U ⊂ S¹, the Möbius band looks like a rectangle (no twist), so:

π⁻¹(U) ≅ U × ℝ
This means the preimage of U under π behaves locally like a simple product — a strip — because the twisting only affects the ends of the band.

We define a local trivialization map:

φ([x, y]) = (x mod 1, y)
This identifies each point in π⁻¹(U) with a pair (x, y) ∈ U × ℝ, giving a homeomorphism between the open subset of the Möbius band and the product space.

This is what makes the Möbius band a locally trivial fibre bundle over the circle.

So,
 
π⁻¹(U) ≅ U × ℝ
via the map φ([x, y]) = (x mod 1, y) — a homeomorphism.

This map is a homeomorphism

- E Locally: 𝜋^(−1) ( 𝑈 ) ≅ 𝑈 × 𝑅 for small open 𝑈 ⊂ 𝑆^1. 
- Globally: The bundle is not homeomorphic to 𝑆^1 × 𝑅 due to a twist in how fibres are glued around the circle. This is a nontrivial line bundle. 

### Example 2: Tangent Bundle of 𝑆 ^ 1 (The Circle)
- Total space: 𝑇𝑆^1 ≅ 𝑆^1 × 𝑅 
- Base space: 𝑀 = 𝑆 1 
- Fibre: 𝐹 = 𝑅 

- 𝑇𝑆^1 Locally: 𝜋 − 1 ( 𝑈 ) ≅ 𝑈 × 𝑅 
- Globally: In this case, the bundle is globally trivial — the tangent bundle of the circle is diffeomorphic to the cylinder 𝑆 1 × 𝑅. This is a trivial line bundle.
In other words the product of the fibre and base space just IS the total space E.

## Tangent Bundles Generally

### Tangent Space 
Let 𝑀 be a smooth manifold and let 𝑝 ∈ 𝑀. The tangent space at 𝑝, denoted 𝑇𝑝𝑀 , is a real vector space whose elements are called tangent vectors at 𝑝. 

There are several equivalent ways to define 𝑇𝑝𝑀 

The most common ones are:

- Derivations: Define 𝑇𝑝𝑀 as the set of all derivations at 𝑝 — i.e., linear maps: 

v: 𝐶∞ (M) → ℝ 

such that: 

v(fg) = v(f)g(p) + f(p)v(g) 

for all 𝑓 , 𝑔 ∈ 𝐶∞( 𝑀 ) . These are like directional derivatives acting on smooth functions. 

-- Equivalence classes of curves: 

Alternatively, define 𝑇 𝑝 𝑀 as equivalence classes of smooth curves 𝛾 : ( − 𝜖 , 𝜖 ) → 𝑀 with 𝛾 ( 0 ) = 𝑝 , where: 

 γ₁ ∼ γ₂  ⇔  (d/dt)|₀ [φ ∘ γ₁]\(t) = (d/dt)|₀ [φ ∘ γ₂]\(t) 
 
 for any (and hence all) charts 𝜑 around 𝑝. In both cases, 𝑇 𝑝 𝑀 ≅ R 𝑛 as vector spaces, but not canonically — it depends on local charts


"The geometric tangent space is thus canonically isomorphic to the set of derivations at p

Why does this matter? Because on an abstract manifold, the geometric tangent space doesn't have any coordinate-independent meaning, but the space of derivations at p does. So we take the space of derivations at p as our definition of the tangent space to M at p.

<!-- PARENT: auto -->
Parent: [[maths/geometric-topology|geometric-topology]]
<!-- /PARENT -->
