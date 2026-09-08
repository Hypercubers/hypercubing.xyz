# Conic Sweep Puzzle Sets
<style>

.md-typeset .cut-depth-table {

  overflow-x: visible !important;

}

.md-typeset .cut-depth-table .md-typeset__scrollwrap {

  overflow-x: auto !important;

}

.md-typeset .cut-depth-table table {

  border-collapse: collapse !important;

  max-width: none !important;

}

.md-typeset .cut-depth-table table th,

.md-typeset .cut-depth-table table td {

  border: 1px solid var(--md-typeset-table-color) !important;

  padding: 0.2em 0.4em !important;

  text-align: center !important;

  vertical-align: middle !important;

  font-size: 1.01rem !important;

  line-height: 1.15 !important;

}

.md-typeset .cut-depth-table table th {

  font-weight: 700 !important;

}

.md-typeset .cut-depth-table table td img {

  display: block !important;

  margin: 0 auto !important;

  max-width: none !important;

}

.md-typeset .cut-depth-table table td mjx-container,

.md-typeset .cut-depth-table table th mjx-container {

  display: inline-block !important;

  margin: 0 auto !important;

  text-align: center !important;

  font-size: 1.0em !important;

}

/* Keep the cone-angle column from wrapping */

.md-typeset .cut-depth-table table th:nth-child(5),

.md-typeset .cut-depth-table table td:nth-child(5) {

  white-space: nowrap !important;

}

/* Click-to-copy angle values */

.md-typeset .copy-angle {

  cursor: pointer !important;

  white-space: nowrap !important;

  display: inline-block !important;

}

.md-typeset .copy-angle:hover {

  background: transparent !important;

}

.md-typeset .copy-angle::after {

  content: none !important;

}

.md-typeset .copy-angle.copied-angle {

  background: var(--md-accent-fg-color--transparent) !important;

}

/* Exact/degree toggle */

.md-typeset .cut-depth-table .angle-exact {

  white-space: nowrap !important;

  display: inline-block !important;

}

.md-typeset .cut-depth-table .angle-degree {

  white-space: nowrap !important;

  display: none !important;

}

.md-typeset .cut-depth-table:has(.angle-toggle:checked) .angle-exact {

  display: none !important;

}

.md-typeset .cut-depth-table:has(.angle-toggle:checked) .angle-degree {

  display: inline-block !important;

}

/* Toggle label in the Cone Angle header */

.md-typeset .cut-depth-table .angle-toggle-label {

  display: block !important;

  margin-top: 0.25em !important;

  font-size: 0.75em !important;

  font-weight: 400 !important;

  white-space: nowrap !important;

}

.md-typeset .cut-depth-table .angle-toggle {

  margin-right: 0.25em !important;

}

/* Collapsed right-side table of contents */

@media screen and (min-width: 76.25em) {

  .md-sidebar--secondary {

    width: 2.2rem !important;

    min-width: 2.2rem !important;

    transition: width 0.18s ease;

  }

  .md-sidebar--secondary .md-sidebar__scrollwrap {

    opacity: 0;

    pointer-events: none;

    overflow: hidden;

    transition: opacity 0.18s ease;

  }

  .md-sidebar--secondary::before {

    content: "Contents";

    position: sticky;

    top: 4rem;

    display: block;

    writing-mode: vertical-rl;

    text-orientation: mixed;

    font-size: 0.7rem;

    opacity: 0.65;

    padding-top: 0.5rem;

    margin-left: 0.35rem;

  }

  .md-sidebar--secondary:hover,

  .md-sidebar--secondary:focus-within {

    width: 12.1rem !important;

    min-width: 12.1rem !important;

  }

  .md-sidebar--secondary:hover .md-sidebar__scrollwrap,

  .md-sidebar--secondary:focus-within .md-sidebar__scrollwrap {

    opacity: 1;

    pointer-events: auto;

    overflow: auto;

  }

  .md-sidebar--secondary:hover::before,

  .md-sidebar--secondary:focus-within::before {

    display: none;

  }

}

/* Intro/wiki-style figures */

.md-typeset .wiki-thumb {

  float: right;

  clear: right;

  width: 260px;

  margin: 0 0 1em 1.25em;

  padding: 0.35em;

  border: 1px solid var(--md-typeset-table-color);

  font-size: 0.8em;

  line-height: 1.25;

  text-align: center;

}

.md-typeset .wiki-thumb img {

  display: block;

  width: 100%;

  height: auto;

  margin: 0 auto 0.35em auto;

}

.md-typeset .wiki-clear {

  clear: both;

}

@media screen and (max-width: 700px) {

  .md-typeset .wiki-thumb {

    float: none;

    width: auto;

    margin: 1em 0;

  }

}

/* Tighten terminology definition list spacing */

.md-typeset .terminology-list {

  margin-top: 0.4em !important;

  margin-bottom: 0.6em !important;

}

.md-typeset .terminology-list dl {

  margin-top: 0.4em !important;

  margin-bottom: 0.6em !important;

}

.md-typeset .terminology-list dt {

  margin-top: 0.35em !important;

  margin-bottom: 0 !important;

  padding-bottom: 0 !important;

  font-weight: 700;

}

.md-typeset .terminology-list dd {

  margin-top: 0 !important;

  margin-bottom: 0.35em !important;

  margin-left: 1.5em !important;

  padding-top: 0 !important;

}

.md-typeset .terminology-list p {

  margin-top: 0.2em !important;

  margin-bottom: 0.35em !important;

}

.md-typeset .terminology-list p + p {

  margin-top: 0 !important;

}

/* Indented subterms under Boundary/Intersection */

.md-typeset .terminology-list .subterm-list {

  margin-top: 0.2em !important;

  margin-bottom: 0.35em !important;

  margin-left: 1.5em !important;

}

.md-typeset .terminology-list .subterm-list dl {

  margin-top: 0 !important;

  margin-bottom: 0 !important;

}

.md-typeset .terminology-list .subterm-list dt {

  margin-top: 0.2em !important;

  margin-bottom: 0 !important;

  padding-bottom: 0 !important;

  font-weight: 700;

}

.md-typeset .terminology-list .subterm-list dd {

  margin-top: 0 !important;

  margin-bottom: 0.25em !important;

  margin-left: 1.5em !important;

  padding-top: 0 !important;

}



/* Table controls: row filters and screen scaling */
.md-typeset .cut-depth-table {
  --table-scale: 1;
}

.md-typeset .cut-depth-table .table-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.75em;
  margin: 0.4em 0 0.5em 0;
  font-size: 0.85em;
}

.md-typeset .cut-depth-table .table-visibility-controls,
.md-typeset .cut-depth-table .table-scale-controls {
  display: flex;
  align-items: center;
  gap: 0.65em;
  flex-wrap: wrap;
}

.md-typeset .cut-depth-table .table-controls label {
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.md-typeset .cut-depth-table .table-controls label.is-disabled {
  opacity: 0.45;
  cursor: not-allowed;
}

.md-typeset .cut-depth-table .table-controls input:disabled {
  cursor: not-allowed;
}

.md-typeset .cut-depth-table .table-scale-button {
  min-width: 1.8em;
  padding: 0.05em 0.45em;
  border: 1px solid var(--md-typeset-table-color);
  border-radius: 0.2em;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  cursor: pointer;
  font: inherit;
  line-height: 1.4;
}

.md-typeset .cut-depth-table .table-scale-button:hover {
  background: var(--md-accent-fg-color--transparent);
}

.md-typeset .cut-depth-table .table-scale-value {
  min-width: 3.5em;
  text-align: center;
  font-variant-numeric: tabular-nums;
}

.md-typeset .cut-depth-table table {
  zoom: var(--table-scale);
}

/* Hide rows, then hide the step column whenever either row filter is active */
.md-typeset .cut-depth-table.hide-intersections tbody tr.intersection-row,
.md-typeset .cut-depth-table.hide-phases tbody tr.phase-row {
  display: none !important;
}

.md-typeset .cut-depth-table.hide-intersections table th:nth-child(1),
.md-typeset .cut-depth-table.hide-intersections table td:nth-child(1),
.md-typeset .cut-depth-table.hide-phases table th:nth-child(1),
.md-typeset .cut-depth-table.hide-phases table td:nth-child(1) {
  display: none !important;
}

</style>

<!-- <details>

<summary>Author's note</summary>

This article was primarily written by me, Preston Alden.

</details> -->

A **polyhedral conic sweep set** is a set of every distinct puzzle produced by cutting a solid with congruent, origin-centered cones whose axes are aligned to the face normals of a given polyhedron.

This article is meant to serve as a reference sheet detailing notable puzzle sets in full with their exact measurements and solutions. In practice, these solutions can provide exceptionally helpful literal guidelines when designing cutpaths for twisty puzzles.

## Terminology
***Note:** Several of these terms were coined while writing this article and are only meant to aid in explanation. Most were adapted from existing mathematical terminology, such as “concurrence,” in an effort to make them intuitive and minimize unnecessary abstraction.*

<figure class="wiki-thumb">

  <img src="https://assets.hypercubing.xyz/img/conic_cut_gifs/sphere_cone_centerline_no_xh_final.gif" alt="A visualization of a single conical cut">

  <figcaption>A visualization of a single conical cut, where θ represents the cone angle and the trace line is shown in red</figcaption>

</figure>

<div class="terminology-list" markdown="1">

<br>
**Trace line**

A **trace line** is a curve formed by the intersection of a cone and the surface of a solid. In the case of a sphere (when centered at the origin), a trace line will always be circular, but with a different solid or polyhedron a trace line can be very curvy and sharp.

<br>
**Puzzle**

A **puzzle** is any result in a full conic sweep operation for a given polyhedron where \(0^\circ < \theta < 180^\circ\). The sets below exhibit every “unique” puzzle for their respective polyhedra so they only cover results in the range \(0^\circ < \theta \le 90^\circ\) because values past \(90^\circ\) only produce mirrored (non-unique) puzzles. Each set is composed of two alternating types of puzzles: a sweep over a range before an intersection known as a phase, or a static instance at a phase boundary.

<br>

**Boundary/Intersection**

A phase boundary or intersection occurs when two or more trace lines make contact in one of three ways:

<div class="subterm-list" markdown="1">

**— Tangency**

When two trace lines meet at a point and share the same local direction at that point.

**— Concurrence**

When three or more non-tangent trace lines intersect at one common point.

**— Coincidence**

When two trace lines completely overlap (this only occurs when \(\theta = 90^\circ\)).

</div>

</div>

<div class="wiki-clear"></div>
<br>
# Catalog of Conic Sweep Sets
## Platonic solids
The Platonic solids form a fundamental class of conic sweep sets. These sets often appear as recurring subsets within other polyhedral conic sweep sets, especially those associated with the Catalan and Archimedean solids.

## Tetrahedral conic sweep set
![Tetrahedron 90 sweep full](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_90_sweep_full.gif&width=200)

The tetrahedral conic sweep set consists of five distinct constructions. Uniquely, the tetrahedron is the only Platonic solid that does not end with a coincident intersection due to its lack of opposing faces. It is the only set that never crosses the center point of its faces. This group contains only two trace-line intersections, one tangent and the other concurrent.

<div class="cut-depth-table" markdown="1">

<div class="table-controls">
  <div class="table-visibility-controls">
    <label><input class="hide-intersections-toggle" type="checkbox"> Hide Intersections</label>
    <label><input class="hide-phases-toggle" type="checkbox"> Hide Phases</label>
  </div>
  <div class="table-scale-controls">
    <button class="table-scale-button table-scale-minus" type="button" aria-label="Make table smaller">−</button>
    <span class="table-scale-value">100%</span>
    <button class="table-scale-button table-scale-plus" type="button" aria-label="Make table larger">+</button>
  </div>
</div>

| Step | Phase | Boundary /<br>Intersection | Image | Cone Angle \(\theta\)<br><label class="angle-toggle-label"><input class="angle-toggle" type="checkbox">show degree form</label> | Sweep Progress <br> (\(s = \theta/90^\circ\)) | Type |
|---:|---:|---:|---|---|---|---|
| 1 | 1 | NA | ![Tetrahedron 54p8 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_54p8_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta <\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta <\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{0\% < s < \mathord{\sim}60.8\%\right\}\) | NA |
| 2 | NA | 1 | ![Tetrahedron 54p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_54p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span></span> | \(\displaystyle \mathord{\sim}60.8\%\) | Tangent |
| 3 | 2 | NA | ![Tetrahedron 70p5 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_70p5_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle < \theta <\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle < \theta <\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}60.8\% < s < \mathord{\sim}78.4\%\right\}\) | NA |
| 4 | NA | 2 | ![Tetrahedron 70p5](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_70p5.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span></span> | \(\displaystyle \mathord{\sim}78.4\%\) | Concurrent |
| 5 | 3 | NA | ![Tetrahedron 90 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Tetrahedron_90_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle < \theta \le\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle < \theta \le\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}78.4\% < s \le 100\%\right\}\) | NA |

</div>

## Hexahedral conic sweep set
![Cube 90 sweep full](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_90_sweep_full.gif&width=200)

The hexahedral conic sweep set consists of six distinct constructions. This group contains three trace-line intersections: 1 tangent, 1 concurrent, and 1 coincident.

<div class="cut-depth-table" markdown="1">

<div class="table-controls">
  <div class="table-visibility-controls">
    <label><input class="hide-intersections-toggle" type="checkbox"> Hide Intersections</label>
    <label><input class="hide-phases-toggle" type="checkbox"> Hide Phases</label>
  </div>
  <div class="table-scale-controls">
    <button class="table-scale-button table-scale-minus" type="button" aria-label="Make table smaller">−</button>
    <span class="table-scale-value">100%</span>
    <button class="table-scale-button table-scale-plus" type="button" aria-label="Make table larger">+</button>
  </div>
</div>

| Step | Phase | Boundary /<br>Intersection | Image | Cone Angle \(\theta\)<br><label class="angle-toggle-label"><input class="angle-toggle" type="checkbox">show degree form</label> | Sweep Progress <br> (\(s = \theta/90^\circ\)) | Type |
|---:|---:|---:|---|---|---|---|
| 1 | 1 | NA | ![Cube 45 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_45_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="45deg">\(\displaystyle 45^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="45deg">\(\displaystyle 45.000^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{0\% < s \lt 50.0\%\right\}\) | NA |
| 2 | NA | 1 | ![Cube 45](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_45.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="45deg">\(\displaystyle 45^\circ\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="45deg">\(\displaystyle 45.000^\circ\)</span></span> | \(\displaystyle 50.0\%\) | Tangent |
| 3 | 2 | NA | ![Cube 54p7 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_54p7_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="45deg">\(\displaystyle 45^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="45deg">\(\displaystyle 45.000^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{50.0\% \lt s \lt \mathord{\sim}60.8\%\right\}\) | NA |
| 4 | NA | 2 | ![Cube 54p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_54p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span></span> | \(\displaystyle \mathord{\sim}60.8\%\) | Concurrent |
| 5 | 3 | NA | ![Cube 90 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_90_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}60.8\% \lt s \lt 100\%\right\}\) | NA |
| 6 | NA | 3 | ![Cube 90](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Cube_90.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span></span> | \(\displaystyle 100\%\) | Coincident |

</div>

## Octahedral conic sweep set
![Octahedron 90 sweep full](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_90_sweep_full.gif&width=200)

The octahedral conic sweep set consists of eight distinct constructions. This group contains four trace-line intersections: 2 tangent, 1 concurrent, and 1 coincident.

<div class="cut-depth-table" markdown="1">

<div class="table-controls">
  <div class="table-visibility-controls">
    <label><input class="hide-intersections-toggle" type="checkbox"> Hide Intersections</label>
    <label><input class="hide-phases-toggle" type="checkbox"> Hide Phases</label>
  </div>
  <div class="table-scale-controls">
    <button class="table-scale-button table-scale-minus" type="button" aria-label="Make table smaller">−</button>
    <span class="table-scale-value">100%</span>
    <button class="table-scale-button table-scale-plus" type="button" aria-label="Make table larger">+</button>
  </div>
</div>

| Step | Phase | Boundary /<br>Intersection | Image | Cone Angle \(\theta\)<br><label class="angle-toggle-label"><input class="angle-toggle" type="checkbox">show degree form</label> | Sweep Progress <br> (\(s = \theta/90^\circ\)) | Type |
|---:|---:|---:|---|---|---|---|
| 1 | 1 | NA | ![Octahedron 35p3 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_35p3_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{0\% < s \lt \mathord{\sim}39.2\%\right\}\) | NA |
| 2 | NA | 1 | ![Octahedron 35p2](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_35p2.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span></span> | \(\displaystyle \mathord{\sim}39.2\%\) | Tangent |
| 3 | 2 | NA | ![Octahedron 54p7 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_54p7_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}39.2\% \lt s \lt \mathord{\sim}60.8\%\right\}\) | NA |
| 4 | NA | 2 | ![Octahedron 54p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_54p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span></span> | \(\displaystyle \mathord{\sim}60.8\%\) | Tangent |
| 5 | 3 | NA | ![Octahedron 70p5 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_70p5_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}60.8\% \lt s \lt \mathord{\sim}78.4\%\right\}\) | NA |
| 6 | NA | 3 | ![Octahedron 70p5](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_70p5.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span></span> | \(\displaystyle \mathord{\sim}78.4\%\) | Concurrent |
| 7 | 4 | NA | ![Octahedron 90 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_90_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}78.4\% \lt s \lt 100\%\right\}\) | NA |
| 8 | NA | 4 | ![Octahedron 90](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Octahedron_90.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span></span> | \(\displaystyle 100\%\) | Coincident |

</div>

## Dodecahedral conic sweep set
![Dodecahedron 90 sweep full](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_90_sweep_full.gif&width=200)

The dodecahedral conic sweep set consists of 12 distinct constructions. This group contains six trace-line intersections: 2 tangent, 3 concurrent, and 1 coincident.

<div class="cut-depth-table" markdown="1">

<div class="table-controls">
  <div class="table-visibility-controls">
    <label><input class="hide-intersections-toggle" type="checkbox"> Hide Intersections</label>
    <label><input class="hide-phases-toggle" type="checkbox"> Hide Phases</label>
  </div>
  <div class="table-scale-controls">
    <button class="table-scale-button table-scale-minus" type="button" aria-label="Make table smaller">−</button>
    <span class="table-scale-value">100%</span>
    <button class="table-scale-button table-scale-plus" type="button" aria-label="Make table larger">+</button>
  </div>
</div>

| Step | Phase | Boundary /<br>Intersection | Image | Cone Angle \(\theta\)<br><label class="angle-toggle-label"><input class="angle-toggle" type="checkbox">show degree form</label> | Sweep Progress <br> (\(s = \theta/90^\circ\)) | Type |
|---:|---:|---:|---|---|---|---|
| 1 | 1 | NA | ![Dodecahedron 31p7 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_31p7_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5+sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+\sqrt{5}}{10}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="31.717deg">\(\displaystyle \mathord{\sim}31.717^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{0\% < s \lt \mathord{\sim}35.2\%\right\}\) | NA |
| 2 | NA | 1 | ![Dodecahedron 31p7](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_31p7.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5+sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+\sqrt{5}}{10}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="31.717deg">\(\displaystyle \mathord{\sim}31.717^\circ\)</span></span> | \(\displaystyle \mathord{\sim}35.2\%\) | Tangent |
| 3 | 2 | NA | ![Dodecahedron 37p4 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_37p4_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5+sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+\sqrt{5}}{10}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="31.717deg">\(\displaystyle \mathord{\sim}31.717^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}35.2\% \lt s \lt \mathord{\sim}41.5\%\right\}\) | NA |
| 4 | NA | 2 | ![Dodecahedron 37p4](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_37p4.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span></span> | \(\displaystyle \mathord{\sim}41.5\%\) | Concurrent |
| 5 | 3 | NA | ![Dodecahedron 58p3 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_58p3_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5-sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-\sqrt{5}}{10}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="58.283deg">\(\displaystyle \mathord{\sim}58.283^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}41.5\% \lt s \lt \mathord{\sim}64.8\%\right\}\) | NA |
| 6 | NA | 3 | ![Dodecahedron 58p3](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_58p3.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5-sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-\sqrt{5}}{10}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="58.283deg">\(\displaystyle \mathord{\sim}58.283^\circ\)</span></span> | \(\displaystyle \mathord{\sim}64.8\%\) | Tangent |
| 7 | 4 | NA | ![Dodecahedron 63p4 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_63p4_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5-sqr(5))/10))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-\sqrt{5}}{10}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/sqr(5))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{5}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="58.283deg">\(\displaystyle \mathord{\sim}58.283^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="63.435deg">\(\displaystyle \mathord{\sim}63.435^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}64.8\% \lt s \lt \mathord{\sim}70.5\%\right\}\) | NA |
| 8 | NA | 4 | ![Dodecahedron 63p4](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_63p4.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/sqr(5))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{5}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="63.435deg">\(\displaystyle \mathord{\sim}63.435^\circ\)</span></span> | \(\displaystyle \mathord{\sim}70.5\%\) | Concurrent |
| 9 | 5 | NA | ![Dodecahedron 79p2 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_79p2_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/sqr(5))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{5}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="63.435deg">\(\displaystyle \mathord{\sim}63.435^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}70.5\% \lt s \lt \mathord{\sim}88.0\%\right\}\) | NA |
| 10 | NA | 5 | ![Dodecahedron 79p2](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_79p2.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span></span> | \(\displaystyle \mathord{\sim}88.0\%\) | Concurrent |
| 11 | 6 | NA | ![Dodecahedron 90 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_90_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}88.0\% \lt s \lt 100\%\right\}\) | NA |
| 12 | NA | 6 | ![Dodecahedron 90](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Dodecahedron_90.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span></span> | \(\displaystyle 100\%\) | Coincident |

</div>

## Icosahedral conic sweep set
![Icosahedron 90 sweep full](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_90_sweep_full.gif&width=200)

The icosahedral conic sweep set consists of 24 distinct constructions. This group contains 12 trace-line intersections: 4 tangent, 7 concurrent, and 1 coincident.

<div class="cut-depth-table" markdown="1">

<div class="table-controls">
  <div class="table-visibility-controls">
    <label><input class="hide-intersections-toggle" type="checkbox"> Hide Intersections</label>
    <label><input class="hide-phases-toggle" type="checkbox"> Hide Phases</label>
  </div>
  <div class="table-scale-controls">
    <button class="table-scale-button table-scale-minus" type="button" aria-label="Make table smaller">−</button>
    <span class="table-scale-value">100%</span>
    <button class="table-scale-button table-scale-plus" type="button" aria-label="Make table larger">+</button>
  </div>
</div>

| Step | Phase | Boundary /<br>Intersection | Image | Cone Angle \(\theta\)<br><label class="angle-toggle-label"><input class="angle-toggle" type="checkbox">show degree form</label> | Sweep Progress <br> (\(s = \theta/90^\circ\)) | Type |
|---:|---:|---:|---|---|---|---|
| 1 | 1 | NA | ![Icosahedron 20p9 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_20p9_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="arccos((sqr(15)+sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}+\sqrt{3}}{6}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="0deg">\(\displaystyle 0^\circ\)</span>\(\displaystyle < \theta \lt\)<span class="copy-angle" data-copy="20.905deg">\(\displaystyle \mathord{\sim}20.905^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{0\% < s \lt \mathord{\sim}23.2\%\right\}\) | NA |
| 2 | NA | 1 | ![Icosahedron 21](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_21.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos((sqr(15)+sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}+\sqrt{3}}{6}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="20.905deg">\(\displaystyle \mathord{\sim}20.905^\circ\)</span></span> | \(\displaystyle \mathord{\sim}23.2\%\) | Tangent |
| 3 | 2 | NA | ![Icosahedron 35p3 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_35p3_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos((sqr(15)+sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}+\sqrt{3}}{6}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="20.905deg">\(\displaystyle \mathord{\sim}20.905^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}23.2\% \lt s \lt \mathord{\sim}39.2\%\right\}\) | NA |
| 4 | NA | 2 | ![Icosahedron 35p2](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_35p2.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span></span> | \(\displaystyle \mathord{\sim}39.2\%\) | Tangent |
| 5 | 3 | NA | ![Icosahedron 37p4 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_37p4_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(2/sqr(6))">\(\displaystyle \cos^{-1}\!\left(\dfrac{2}{\sqrt{6}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="35.264deg">\(\displaystyle \mathord{\sim}35.264^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}39.2\% \lt s \lt \mathord{\sim}41.5\%\right\}\) | NA |
| 6 | NA | 3 | ![Icosahedron 37p4](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_37p4.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span></span> | \(\displaystyle \mathord{\sim}41.5\%\) | Concurrent |
| 7 | 4 | NA | ![Icosahedron 41p8 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_41p8_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5+2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5+2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr(5)/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{5}}{3}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="37.377deg">\(\displaystyle \mathord{\sim}37.377^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="41.810deg">\(\displaystyle \mathord{\sim}41.810^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}41.5\% \lt s \lt \mathord{\sim}46.5\%\right\}\) | NA |
| 8 | NA | 4 | ![Icosahedron 41p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_41p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr(5)/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{5}}{3}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="41.810deg">\(\displaystyle \mathord{\sim}41.810^\circ\)</span></span> | \(\displaystyle \mathord{\sim}46.5\%\) | Concurrent |
| 9 | 5 | NA | ![Icosahedron 54p7 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_54p7_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr(5)/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{5}}{3}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="41.810deg">\(\displaystyle \mathord{\sim}41.810^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}46.5\% \lt s \lt \mathord{\sim}60.8\%\right\}\) | NA |
| 10 | NA | 5 | ![Icosahedron 54p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_54p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span></span> | \(\displaystyle \mathord{\sim}60.8\%\) | Tangent |
| 11 | 6 | NA | ![Icosahedron 56p8 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_56p8_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/sqr(3))">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{\sqrt{3}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((19+8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19+8\sqrt{5}}{123}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="54.736deg">\(\displaystyle \mathord{\sim}54.736^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="56.795deg">\(\displaystyle \mathord{\sim}56.795^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}60.8\% \lt s \lt \mathord{\sim}63.1\%\right\}\) | NA |
| 12 | NA | 6 | ![Icosahedron 56p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_56p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((19+8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19+8\sqrt{5}}{123}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="56.795deg">\(\displaystyle \mathord{\sim}56.795^\circ\)</span></span> | \(\displaystyle \mathord{\sim}63.1\%\) | Concurrent |
| 13 | 7 | NA | ![Icosahedron 60p8 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_60p8_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((19+8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19+8\sqrt{5}}{123}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr(5/21))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5}{21}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="56.795deg">\(\displaystyle \mathord{\sim}56.795^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="60.794deg">\(\displaystyle \mathord{\sim}60.794^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}63.1\% \lt s \lt \mathord{\sim}67.5\%\right\}\) | NA |
| 14 | NA | 7 | ![Icosahedron 60p8](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_60p8.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr(5/21))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5}{21}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="60.794deg">\(\displaystyle \mathord{\sim}60.794^\circ\)</span></span> | \(\displaystyle \mathord{\sim}67.5\%\) | Concurrent |
| 15 | 8 | NA | ![Icosahedron 69p1 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_69p1_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr(5/21))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5}{21}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos((sqr(15)-sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}-\sqrt{3}}{6}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="60.794deg">\(\displaystyle \mathord{\sim}60.794^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="69.095deg">\(\displaystyle \mathord{\sim}69.095^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}67.5\% \lt s \lt \mathord{\sim}76.8\%\right\}\) | NA |
| 16 | NA | 8 | ![Icosahedron 69p1](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_69p1.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos((sqr(15)-sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}-\sqrt{3}}{6}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="69.095deg">\(\displaystyle \mathord{\sim}69.095^\circ\)</span></span> | \(\displaystyle \mathord{\sim}76.8\%\) | Tangent |
| 17 | 9 | NA | ![Icosahedron 70p5 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_70p5_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos((sqr(15)-sqr(3))/6)">\(\displaystyle \cos^{-1}\!\left(\dfrac{\sqrt{15}-\sqrt{3}}{6}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="69.095deg">\(\displaystyle \mathord{\sim}69.095^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}76.8\% \lt s \lt \mathord{\sim}78.4\%\right\}\) | NA |
| 18 | NA | 9 | ![Icosahedron 70p5](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_70p5.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span></span> | \(\displaystyle \mathord{\sim}78.4\%\) | Concurrent |
| 19 | 10 | NA | ![Icosahedron 79p2 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_79p2_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(1/3)">\(\displaystyle \cos^{-1}\!\left(\dfrac{1}{3}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="70.529deg">\(\displaystyle \mathord{\sim}70.529^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}78.4\% \lt s \lt \mathord{\sim}88.0\%\right\}\) | NA |
| 20 | NA | 10 | ![Icosahedron 79p2](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_79p2.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span></span> | \(\displaystyle \mathord{\sim}88.0\%\) | Concurrent |
| 21 | 11 | NA | ![Icosahedron 84p5 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_84p5_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((5-2*sqr(5))/15))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{5-2\sqrt{5}}{15}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="arccos(sqr((19-8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19-8\sqrt{5}}{123}}\right)\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="79.188deg">\(\displaystyle \mathord{\sim}79.188^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="84.545deg">\(\displaystyle \mathord{\sim}84.545^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}88.0\% \lt s \lt \mathord{\sim}93.9\%\right\}\) | NA |
| 22 | NA | 11 | ![Icosahedron 84p6](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_84p6.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="arccos(sqr((19-8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19-8\sqrt{5}}{123}}\right)\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="84.545deg">\(\displaystyle \mathord{\sim}84.545^\circ\)</span></span> | \(\displaystyle \mathord{\sim}93.9\%\) | Concurrent |
| 23 | 12 | NA | ![Icosahedron 90 sweep](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_90_sweep.gif&width=75) | <span class="angle-exact">\(\displaystyle \{\)<span class="copy-angle" data-copy="arccos(sqr((19-8*sqr(5))/123))">\(\displaystyle \cos^{-1}\!\left(\sqrt{\dfrac{19-8\sqrt{5}}{123}}\right)\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span>\(\displaystyle \}\)</span><span class="angle-degree">\(\displaystyle \{\)<span class="copy-angle" data-copy="84.545deg">\(\displaystyle \mathord{\sim}84.545^\circ\)</span>\(\displaystyle \lt \theta \lt\)<span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span>\(\displaystyle \}\)</span> | \(\displaystyle \left\{\mathord{\sim}93.9\% \lt s \lt 100\%\right\}\) | NA |
| 24 | NA | 12 | ![Icosahedron 90](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Icosahedron_90.gif&width=75) | <span class="angle-exact"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90^\circ\)</span></span><span class="angle-degree"><span class="copy-angle" data-copy="90deg">\(\displaystyle 90.000^\circ\)</span></span> | \(\displaystyle 100\%\) | Coincident |

</div>

These animations were created using a modified version of Jaap's "[Sphere](https://www.jaapsch.net/puzzles/sphere.htm?sym=1&blue=150)" simulator.

<script>
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".cut-depth-table").forEach(function (wrapper) {
    const table = wrapper.querySelector("table");
    if (!table) return;

    const hideIntersections = wrapper.querySelector(".hide-intersections-toggle");
    const hidePhases = wrapper.querySelector(".hide-phases-toggle");
    const scaleMinus = wrapper.querySelector(".table-scale-minus");
    const scalePlus = wrapper.querySelector(".table-scale-plus");
    const scaleValue = wrapper.querySelector(".table-scale-value");

    table.querySelectorAll("tbody tr").forEach(function (row) {
      const cells = row.querySelectorAll("td");
      const phase = cells[1] ? cells[1].textContent.trim() : "";
      const intersection = cells[2] ? cells[2].textContent.trim() : "";

      row.classList.toggle("phase-row", phase !== "" && phase !== "NA");
      row.classList.toggle("intersection-row", intersection !== "" && intersection !== "NA");
    });

    function updateRowFilters() {
      const intersectionsHidden = hideIntersections && hideIntersections.checked;
      const phasesHidden = hidePhases && hidePhases.checked;

      wrapper.classList.toggle("hide-intersections", intersectionsHidden);
      wrapper.classList.toggle("hide-phases", phasesHidden);

      if (hidePhases) {
        hidePhases.disabled = intersectionsHidden;
        hidePhases.closest("label").classList.toggle("is-disabled", intersectionsHidden);
      }

      if (hideIntersections) {
        hideIntersections.disabled = phasesHidden;
        hideIntersections.closest("label").classList.toggle("is-disabled", phasesHidden);
      }
    }

    if (hideIntersections) {
      hideIntersections.addEventListener("change", function () {
        if (hideIntersections.checked && hidePhases) hidePhases.checked = false;
        updateRowFilters();
      });
    }

    if (hidePhases) {
      hidePhases.addEventListener("change", function () {
        if (hidePhases.checked && hideIntersections) hideIntersections.checked = false;
        updateRowFilters();
      });
    }

    let scale = 1;
    const minScale = 0.5;
    const maxScale = 1.8;
    const scaleStep = 0.1;

    function setScale(nextScale) {
      scale = Math.min(maxScale, Math.max(minScale, nextScale));
      wrapper.style.setProperty("--table-scale", scale.toFixed(2));
      if (scaleValue) scaleValue.textContent = `${Math.round(scale * 100)}%`;
    }

    if (scaleMinus) {
      scaleMinus.addEventListener("click", function () {
        setScale(scale - scaleStep);
      });
    }

    if (scalePlus) {
      scalePlus.addEventListener("click", function () {
        setScale(scale + scaleStep);
      });
    }

    updateRowFilters();
    setScale(1);
  });
});

document.addEventListener("click", async function (event) {
  const target = event.target.closest(".copy-angle");
  if (!target) return;

  const text = target.getAttribute("data-copy");
  if (!text) return;

  try {
    await navigator.clipboard.writeText(text);

    target.classList.add("copied-angle");
    setTimeout(() => {
      target.classList.remove("copied-angle");
    }, 1200);
  } catch (error) {
    console.error("Copy failed:", error);
  }
});
</script>
