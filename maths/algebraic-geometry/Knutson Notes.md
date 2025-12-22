## Grothendieck Topologies and Descent Theory

### Definition 1.1 (Grothendieck Topology)

A **Grothendieck topology** $\tau$ on a category $\mathcal{C}$ consists of:

- A category $\mathcal{C} = \mathrm{Cat}_\tau$, and
- For each object $U \in \mathcal{C}$, a collection $\mathrm{Cov}_\tau(U)$ of families of morphisms
  $$
  \{ \varphi_i : U_i \to U \}_{i \in I}
  $$
  called **coverings** of $U$,

such that the following axioms are satisfied:

1. **Isomorphisms are coverings**

   If $\varphi : V \to U$ is an isomorphism, then
   $$
   \{ \varphi \} \in \mathrm{Cov}_\tau(U).
   $$

2. **Stability under composition**

   If $\{ U_i \to U \} \in \mathrm{Cov}_\tau(U)$ and for each $i$,
   $$
   \{ V_{ij} \to U_i \} \in \mathrm{Cov}_\tau(U_i),
   $$
   then the composed family
   $$
   \{ V_{ij} \to U \}
   $$
   is in $\mathrm{Cov}_\tau(U)$.

3. **Stability under base change**

   If $\{ U_i \to U \} \in \mathrm{Cov}_\tau(U)$ and $V \to U$ is any morphism in $\mathcal{C}$, then the fiber products
   $$
   U_i \times_U V
   $$
   exist, and the family
   $$
   \{ U_i \times_U V \to V \}
   $$
   is in $\mathrm{Cov}_\tau(V)$.

$$
\begin{array}{ccc}
U_i \times_U V & \longrightarrow & U_i \\
\downarrow & & \downarrow \\
V & \longrightarrow & U
\end{array}
$$

### Note: Fibered Product

### Definition (Fiber Product)

Let $\mathcal{C}$ be a category, and let
\[
X \xrightarrow{f} Z \xleftarrow{g} Y
\]
be morphisms in $\mathcal{C}$.

A **fiber product** (or **fibered product**) of $X$ and $Y$ over $Z$ is an object
\[
X \times_Z Y
\]
together with morphisms
\[
X \times_Z Y \to X, \qquad X \times_Z Y \to Y
\]
such that the diagram
\[
\begin{array}{ccc}
X \times_Z Y & \longrightarrow & Y \\
\downarrow & & \downarrow g \\
X & \xrightarrow{f} & Z
\end{array}
\]
commutes, and which satisfies the following universal property:

For any object $T$ and morphisms
\[
T \to X, \qquad T \to Y
\]
such that
\[
f \circ (T \to X) = g \circ (T \to Y),
\]
there exists a unique morphism
\[
T \to X \times_Z Y
\]
making the entire diagram commute.

