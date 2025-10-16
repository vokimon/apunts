# Dependency system and non-gitable dependencies


## Problem to be solved

How to handle external dependencies in project repository?

Right now several approaches are common:

- Tell the developers/users to install them before start working
- Integrate 3rd party code into project's git repository
- Integrate the dependency as submodule

All those have their own benefits and drawbacks,
but them all have drawbacks.

- Asking the users to install dependencies by hand is inconvenient for them
- Integrating code could led to duplications and conflicts when dependencies are shared.
- Submodules solves both problem when working with git, but when distributing zips, developers end up choosing between including or not the dependencies, with their drawbacks.

This problem gets more convoluted when developing an addon with dependencies.
This turns into a hard decision to build upon giant shoulders when developing an addon or a simple game.

## Proposed solution

The proposed solution is to make part of your git maintained status to specify dependencies for the project
but not dependencies content.
This could be done in many ways.
Here I propose one i consider good of course open to discussion.

- Make dependencies declaration a part of project metadata
- Separate addons content in a different place, either project centered `.godot` or user wide `~/local/.godot`
- When the editor opens a project, it should retrieve them from the store if they are not already installed
    - This retrieval should be recursive, if dependencies have dependencies.
- 


