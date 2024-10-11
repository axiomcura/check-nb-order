import pathlib
import nbformat
from typing import Optional
from dataclasses import dataclass


@dataclass
class JupyterCell:
    """Data class representing a Jupyter notebook cell, containing
    information about its type and execution count.

    Attributes:
    ----------
    cell_type : str
        The type of the Jupyter notebook cell (e.g., 'code', 'markdown').
    execution_count : int
        The execution count of the cell, indicating the order in which
        the code cells were run.
    """

    cell_type: str
    execution_count: None | int


def load_nb_contents(
    fpath: str | pathlib.Path, ignore_md: Optional[bool] = False
) -> list[JupyterCell]:
    """
    Loads the contents of a Jupyter notebook file and extracts information about each cell.

    Parameters
    ----------
    fpath : str | pathlib.Path
        Path to the Jupyter notebook file. Can be either a string or a pathlib.Path object.
    ignore_md: Optional[bool]
        Ignore cells that are markdown. Default is False

    Returns
    -------
    list[JupyterCell]
        A list of JupyterCell objects, each representing a cell in the notebook with its type
        and execution count. For markdown cells, the execution count is set to None since they
        do not have one.
    """
    # TODO: add type checker here

    # extracting raw notebook metadata and only get cell metadata
    raw_content = nbformat.read(fpath, as_version=4)
    cell_content = list(raw_content.values())[0]

    # collecting the JupyerCell Objects
    cell_objects = []
    for jupyter_cell in cell_content:
        if jupyter_cell["cell_type"] == "markdown":
            # we can ignore markdown cells if we don't want it
            if ignore_md is True:
                continue
            else:
                # markdowns do not have execution counts therefore default to "None"
                cell_objects.append(
                    JupyterCell(
                        cell_type=jupyter_cell["cell_type"], execution_count=None
                    )
                )
        else:
            cell_objects.append(
                JupyterCell(
                    cell_type=jupyter_cell["cell_type"],
                    execution_count=jupyter_cell["execution_count"],
                )
            )

    return cell_objects
