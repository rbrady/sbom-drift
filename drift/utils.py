from pathlib import Path
from typing import List

from pydantic import parse_file_as

from .data.model import SBOM


def load_sbom_from_file(filepath: Path) -> SBOM:
    """ opens and parses a JSON file to an SBOM object

    :param filepath: path to the json SBOM file
    :return: SBOM object
    """
    return parse_file_as(SBOM, filepath)


def load_sbom_from_json(input_data: dict) -> SBOM:
    """ opens and parses a JSON file to an SBOM object

    :param input_data:  dict from json SBOM file
    :return: SBOM object
    """
    return SBOM(**input_data)


def filter_sbom(filter_list: set, sbom_data: SBOM) -> List[dict]:
    """Filter SBOM by a set of keywords

    >  filter_sbom({'name','type'}, ot)
    >  [{'artifacts': [{'name': 'SQLAlchemy', 'type': 'python'}]},
        {'artifacts': [{'name': 'fastapi', 'type': 'python'}]},
        {'artifacts': [{'name': 'uvicorn', 'type': 'python'}]}]

    """
    sbom_filter = []

    for index, _ in enumerate(sbom_data.artifacts):
        # TODO: artifacts keyword could be passed in as a parameter to the
        # function.
        sbom_filter.append(sbom_data.dict(include={'artifacts': {index: filter_list}}))

    return sbom_filter


def convert_filter_to_sets(filtered_sbom: List[dict]) -> List[set]:
    """Convert the filtered sbom into a list of sets
    > convert_filter_to_sets(< data structure here>)
    > [{('name', 'SQLAlchemy'), ('type', 'python')},
       {('name', 'fastapi'), ('type', 'python')},
       {('name', 'uvicorn'), ('type', 'python')}]

    """
    converted_list_set = []

    for data in filtered_sbom:
        # TODO: artifacts keyword could be passed in as a parameter along
        # index.
        converted_list_set.append(set(data['artifacts'][0].items()))

    return converted_list_set

