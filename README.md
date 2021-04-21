# Project Lovelace problem modules
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://aliramadhan.me"><img src="https://avatars.githubusercontent.com/u/20099589?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ali Ramadhan</b></sub></a><br /><a href="#content-ali-ramadhan" title="Content">🖋</a> <a href="https://github.com/project-lovelace/lovelace-problems/commits?author=ali-ramadhan" title="Tests">⚠️</a> <a href="https://github.com/project-lovelace/lovelace-problems/commits?author=ali-ramadhan" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!