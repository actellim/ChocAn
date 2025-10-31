# Lessons Learned

## Requirements Workflow

- Working from a unified space is the best measure towards collaboration.
	- Likely a git repo for this project with version control.
	- Most of what we're working on should live in the `docs/` directory.
	- Writing docs in markdown enables basically universal conversion using [pandoc](https://github.com/jgm/pandoc) (can export to `.pdf`, `.html`, `.docx`, `.odf`, etc.).
- The *Defining Requirements* step should come **before** the *UML Use-Case Diagram* step.
	- Having the requirements listed **first** would make it easier to derive the relation graph.

