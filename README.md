# Project Lovelace problem modules

[![Tests](https://github.com/project-lovelace/lovelace-problems/actions/workflows/ci.yml/badge.svg)](https://github.com/project-lovelace/lovelace-problems/actions/workflows/ci.yml)

This repository contains modules for generating test cases (inputs and outputs) for
[Project Lovelace](http://projectlovelace.net) problems.

Note that it relies on a private solutions repository to generate solutions.
The solutions are kept private to avoid providing copy-pasteable solutions to every problem.

## New problem submission guide

If you have an idea for a new problem please consider submitting a new problem, we love receiving new contributions!
We discuss new problems on Discord mostly but you can also open a GitHub issue or post on Discourse to discuss. Also feel free to ask us any questions at all!
Let us know if you're interested in submitting new problems so we can invite you to the [Project Lovelace GitHub organization](https://github.com/project-lovelace).

There are three steps to submitting a new problem:

1. Open a pull request to [lovelace-solutions](https://github.com/project-lovelace/lovelace-solutions#new-problem-submission-guide) with the solution to the problem.
2. Open a pull request to lovelace-problems with code to generate test cases for the problem. (You are here!)
3. Open a pull request to [lovelace-website](https://github.com/project-lovelace/lovelace-website#new-problem-submission-guide) with the problem description, code stubs, and any visualization code.

### How to submit new problem test cases

1. Add a new problem module under the [`problems/`](https://github.com/project-lovelace/lovelace-problems/tree/main/problems) directory. Structure it similarly to the other problem modules. You can generate as many test cases as you want although it's good to cover all the interesting cases.
2. Open a pull request! Once all the tests pass it can be merged.
