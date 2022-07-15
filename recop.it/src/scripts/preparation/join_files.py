import types
from pathlib import Path

home = Path.cwd().parents[2]


def get_files(home: str) -> types.GeneratorType[str]:
    """Returns a iterator for the address of all the files in it"""
    assert home.exists()
    files = home.joinpath("data", "processed").iterdir()
    return files
