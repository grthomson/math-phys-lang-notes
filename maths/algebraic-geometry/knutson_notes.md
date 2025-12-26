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

In other words, if a family (i.e. covering family) collection $\{ U_i \to U \}$ is in $\mathrm{Cov}_\tau(U)$, then for every morphism mapping to $U_i$ (call these morphisms $V_{ij}$) we also have that the composition $V_{ij} \rightarrow U_i \rightarrow U$ is also in  $\mathrm{Cov}_\tau(U)$.  Compare to: arbitrary unions of open sets are open. Can consider this "enlargement" of $U$ under union: here we have composition.

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
$$
X \xrightarrow{f} Z \xleftarrow{g} Y
$$
be morphisms in $\mathcal{C}$.

A **fiber product** (or **fibered product**) of $X$ and $Y$ over $Z$ is an object
$$
X \times_Z Y
$$
together with morphisms
$$
X \times_Z Y \to X, \qquad X \times_Z Y \to Y
$$
such that the diagram
$$
\begin{array}{ccc}
X \times_Z Y & \longrightarrow & Y \\
\downarrow & & \downarrow g \\
X & \xrightarrow{f} & Z
\end{array}
$$
commutes, and which satisfies the following universal property:

For any object $T$ and morphisms
$$
T \to X, \qquad T \to Y
$$
such that
$$
f \circ (T \to X) = g \circ (T \to Y),
$$
there exists a unique morphism
$$
T \to X \times_Z Y
$$
making the entire diagram commute.

<br>

```tikz
\usepackage{tikz-cd}
\usepackage{xcolor}

\definecolor{mypink}{HTML}{FF69B4}

\begin{document}

\begin{tikzcd}[
  scale=1.3,
  transform shape,
  row sep=3.2em,
  column sep=3.4em,
  text=mypink,
  draw=mypink,
  every to/.style={draw=mypink, line width=0.9pt},
  arrows={-Stealth}
]
|[font=\huge]| T
  \arrow[drr, bend left, "{\raisebox{3pt}{\small\textit{x}}}"]
  \arrow[ddr, bend right, "{\raisebox{3pt}{\small\textit{y}}}"]
  \arrow[dr, dotted, "{\raisebox{2pt}{\small(\textit{x},\textit{y})}}" description]
  & & \\
& |[font=\huge]| X \times_Z Y
    \arrow[r, "{\raisebox{3pt}{\small\textit{p}}}"]
    \arrow[d, "{\hspace{4pt}\small\textit{q}}"]
  & |[font=\huge]| X \arrow[d, "{\hspace{4pt}\small\textit{f}}"] \\
& |[font=\huge]| Y \arrow[r, "{\raisebox{3pt}{\small\textit{g}}}"]
  & |[font=\huge]| Z
\end{tikzcd}

\end{document}
```

<br>

### Definition 1.2

Let $\tau$ be a topology and $\mathcal{D}$ a category with products.

A **presheaf** on $\tau$ with values in $\mathcal{D}$ is a functor

$$F : \mathcal{C}^{\mathrm{op}} \to \mathcal{D}.$$


A **sheaf** is a presheaf satisfying the following condition:

If $\{ U_i \to U \} \in \mathrm{Cov}_\tau$, then the diagram

<br> 

```tikz
\usepackage{tikz-cd}
\usepackage{xcolor}

\definecolor{mypink}{HTML}{FF69B4}

\begin{document}

% scaled product symbol (no extra packages)
\newcommand{\Bigprod}{\mathop{\scalebox{1.35}{$\prod$}}}

\begin{tikzcd}[
  scale=1.2,
  transform shape,
  row sep=3em,
  column sep=3.5em,
  text=mypink,
  draw=mypink,
  every to/.style={draw=mypink, line width=0.9pt},
  arrows={-Stealth}
]
|[font=\huge]| F(U)
  \arrow[r, "{\raisebox{3pt}{\small\textit{\(\pi\)}}}"] &
|[font=\huge]| \Bigprod_i F(U_i)
  \arrow[r, shift left=0.7ex, "{\raisebox{3pt}{\small\textit{\(\pi_1\)}}}"]
  \arrow[r, shift right=0.7ex, "{\raisebox{3pt}{\small\textit{\(\pi_2\)}}}"'] &
|[font=\huge]| \Bigprod_{i,j} F(U_i \times_U U_j)
\end{tikzcd}

\end{document}

```

<br>

is **exact**.

(Exactness here means that $\pi$ is the equalizer of $\pi_1$ and $\pi_2$.)


### Note: Equalizer

### Definition (Equalizer)

Let $\mathcal{C}$ be a category and let

$$X \;\substack{\xrightarrow{\ f\ }\\[-0.6em]\xrightarrow[\ g\ ]{}}\; Y$$

be two parallel morphisms in $\mathcal{C}$.
<br>

An **equalizer** of $f$ and $g$ is an object $E$ together with a morphism

$$e : E \to X$$

such that

$$f \circ e = g \circ e,$$

and which is **universal** with this property:  
<br>
for any object $T$ with a morphism $t : T \to X$ satisfying

$$
f \circ t = g \circ t,$$
there exists a unique morphism

$$u : T \to E$$

such that

$$e \circ u = t.$$
<br>

```tikz
\usepackage{tikz-cd}
\usepackage{xcolor}

\definecolor{mypink}{HTML}{FF69B4}

\begin{document}

\begin{tikzcd}[
  scale=1.3,
  transform shape,
  row sep=3.2em,
  column sep=3.5em,
  text=mypink,
  draw=mypink,
  every to/.style={draw=mypink, line width=0.9pt},
  arrows={-Stealth}
]
|[font=\huge]| T \arrow[d, dotted, "u"'] \arrow[r, "t"] & |[font=\huge]| X \arrow[r, shift left=0.7ex, "f"] \arrow[r, shift right=0.7ex, "g"'] & |[font=\huge]| Y \\
|[font=\huge]| E \arrow[ru, "e"'] & &
\end{tikzcd}

\end{document}
```

### Back to Sheaves

## The Sheaf Condition — Intuitive Explanation

Let $U \in \mathcal{C}$ be an object covered by a family of morphisms $\{U_i \to U\}$, and  
$F : \mathcal C^{op} \to \mathcal D$ be a presheaf (assigning data to objects).

Because $F$ is contravariant, each $U_i \to U$ induces a restriction map

$$F(U) \to F(U_i).$$ 

Collecting these gives a single map

$$\pi : F(U) \to \prod_i F(U_i).$$

The pieces $U_i$ overlap pairwise and each overlap is represented in the fiber product

$$U_i \times_U U_j.$$

From the two projection maps

$$U_i \times_U U_j \to U_i, \qquad U_i \times_U U_j \to U_j,$$

applying $F$ produces two restriction maps. Bundling these for all $(i,j)$ gives

$$\pi_1, \pi_2 : \prod_i F(U_i) \rightrightarrows \prod_{i,j} F(U_i \times_U U_j).$$

The sheaf condition says that

$$F(U) \xrightarrow{\pi} \prod_i F(U_i)$$

is the **equalizer** of $\pi_1$ and $\pi_2$:
it picks out exactly those families of local data that agree on all overlaps.

In words:  
**local data that is compatible on overlaps comes from a unique global datum.**

---

### Final Mental Model

- $F(U)$: **global data**
- $F(U_i)$: **data on each patch**
- $F(U_i \times_U U_j)$: **data on overlaps**

The sheaf condition says:

> **Global data = families of local data that agree on overlaps.**

This is expressed precisely in the equalizer diagram.

---

## Classical Topology Version (Open Sets)

If $U$ is a topological space and $\{U_i\}$ an open cover, and $F$ assigns
(e.g.) functions, sections, or other data to open sets:

- $F(U)$ is the data on the whole space,
- $F(U_i)$ is the data on each open set,
- $F(U_i \cap U_j)$ is the data on the overlaps.

The sheaf condition becomes:

> If we choose data $s_i \in F(U_i)$ on each $U_i$,  
> and if for every pair $(i,j)$ the restrictions of $s_i$ and $s_j$ to  
> $U_i \cap U_j$ are equal,  
> then there exists a **unique** $s \in F(U)$ whose restriction to each $U_i$ is $s_i$.

This is the **gluing condition** from topology.
