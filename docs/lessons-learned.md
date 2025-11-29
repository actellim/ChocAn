# Lessons Learned

## Requirements Workflow

- Working from a unified space is the best measure towards collaboration.
	- Likely a git repo for this project with version control.
	- Most of what we're working on should live in the `docs/` directory.
	- Writing docs in markdown enables basically universal conversion using [pandoc](https://github.com/jgm/pandoc) (can export to `.pdf`, `.html`, `.docx`, `.odf`, etc.).
- The *Defining Requirements* step should come **before** the *UML Use-Case Diagram* step.
	- Having the requirements listed **first** would make it easier to derive the relation graph.

## Analysis/Design Workflow(s)

- Testing involves re-reading the original request and ensuring that assumptions align with the original requirements.
- Seems like class diagram creation should come before designing the attributes and methods. I didn't find that particularly useful, but if we're making them that'd probably be the ideal time, as it does make it easier to understand some of the dependencies. 

