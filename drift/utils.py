from pathlib import Path

from pydantic import parse_file_as

from .data.model import SBOM


def load_sbom(filepath: Path) -> SBOM:
    """ opens and parses a JSON file to an SBOM object

    :param filepath: path to the json SBOM file
    :return: SBOM object
    """
    return parse_file_as(SBOM, filepath)
