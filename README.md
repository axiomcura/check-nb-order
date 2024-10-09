# check-nb-order

- [check-nb-order](#check-nb-order)
  - [About](#about)
  - [Why is it important to check if your notebooks are executed in order?](#why-is-it-important-to-check-if-your-notebooks-are-executed-in-order)
  - [How does check-nb-order solve this issue](#how-does-check-nb-order-solve-this-issue)
  - [check-nb-order current features](#check-nb-order-current-features)
  - [Development stack](#development-stack)
  - [License and Contributions](#license-and-contributions)

## About

‘check-nb-order’ is a lightweight and simple tool designed to verify whether the cells in your Jupyter notebooks have been executed in the correct order. This tool is inspired by this [article](https://carpenter-singh-lab.broadinstitute.org/blog/best-practices-jupyter-notebook), which outlines best practices for maintaining well-structured Jupyter notebooks.

This repository focuses specifically on ensuring that notebooks are executed sequentially before merging them into your codebase or analytical repositories.

## Why is it important to check if your notebooks are executed in order?

Jupyter notebooks have become essential for data science projects, allowing analysts and scientists to share a clear, interactive narrative of how their code processes data. Think of it like storytelling—users can write code, explain their thought process with markdown, and visualize their results all in one place. This level of transparency helps others understand the steps involved and try the approaches themselves.

A key feature of Jupyter notebooks is the ability to execute code cells independently. Users can independently run specific cells, and variables declared earlier are retained in memory for subsequent use. While this flexibility is convenient, it also introduces a significant risk: executing code out of order may lead to unpredictable results. The retained variables may not reflect the intended data flow, and the output could differ from what was expected, leading to confusion for others who try to follow along. Think of it like reading the pages of a book out of order.

## How does check-nb-order solve this issue

`check-nb-order` uses the `nbformat` package to parse the metadata within the 

`check-nb-order` provides two ways to ensure that your Jupyter notebooks are executed in the correct order:

- **Pre-commit Hook**: check-nb-order can be used as a pre-commit hook by adding it to your .pre-commit-config.yaml file. This ensures that all .ipynb files are checked for proper cell execution order before committing changes. If any notebook is found to have cells executed out of order, an error will be raised, preventing the commit. The error message will indicate which cells are out of order and what their correct execution sequence should be.
- **Standalone Script**: Alternatively, check-nb-order can be run as a standalone script, providing more flexibility. This option allows users to manually check the order of execution in their notebooks without integrating it into the pre-commit workflow.

## check-nb-order current features

Below is a list of the current features supported in `check-nb-order`:

- **Cell Type Distinction**: Differentiates between markdown cells and code cells, ensuring proper identification during notebook validation.
- **Automatic nbconvert Execution** (optional): Executes `nbconvert` automatically if the notebook cells are in the correct order. Generating an `nbconvert` file streamlines code review, making it easier for reviewers to assess your code.

## Development stack

Below is the development stack that is used to develop `check-nb-order`:

- **pre-commit**: A framework for managing and maintaining multi-language pre-commit hooks. It ensures code quality by automatically running checks (like linting, formatting, etc.) before each commit.
- **poetry**: A dependency management and packaging tool for Python. It helps manage project dependencies, ensure reproducible builds, and streamline the publishing of Python packages.
- **pytest**: A testing framework that allows for simple unit tests as well as complex functional testing. It provides an easy way to write scalable tests with detailed error reporting.
- **ruff**: A fast Python linter that focuses on speed and extensibility, allowing for quick code analysis and adherence to style guides, such as PEP 8, without slowing down the development process.
- **click**: A Python package used to create command-line interfaces. It helps in building user-friendly and customizable command-line applications with minimal boilerplate code.

## License and Contributions

This project is licensed under the [BSD 3-Clause License](LICENSE). The BSD 3-Clause License is a permissive license that allows for broad usage, modification, and distribution of the code, both in open-source and proprietary projects. Contributions to the project are welcomed under this license, meaning that any submitted code will also be distributed under these same terms. The license ensures that contributors retain the right to use their code freely, while also allowing others to use, modify, or redistribute the project as long as they credit the original authors and maintain the license in all redistributions. Commercial use of the code is permitted, but the project or its contributors cannot be used
