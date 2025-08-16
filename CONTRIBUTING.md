# Contributing to Crypto Trading AI Research

First off, thank you for considering contributing to this project! Any contributions you make are **greatly appreciated**.

## Branching Strategy

We use a simple branching model based on GitFlow. All new development should happen in feature branches.

- **main**: This branch is for the latest stable release. All pull requests should be made against the `develop` branch.
- **develop**: This is the main development branch. It contains the latest, but not necessarily stable, code.
- **feature/***: These are branches for new features. They should be branched off of `develop` and merged back into `develop` when the feature is complete.

## How Can I Contribute?

### Reporting Bugs

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/your-repo/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/your-repo/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue and describe the enhancement you have in mind.
- Please provide as much context and detail as possible.

### Pull Requests

1.  Fork the repo and create your branch from `develop`.
2.  If you've added code that should be tested, add tests.
3.  Ensure the test suite passes.
4.  Make sure your code lints.
5.  Issue that pull request against the `develop` branch!

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.

### Python Styleguide

- We use `black` for code formatting and `flake8` for linting. Please ensure your code adheres to these standards.
