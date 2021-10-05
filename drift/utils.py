from inspect import getmembers, isroutine
from typing import Any, List

# def load_sbom_from_file(filepath: Path) -> SBOM:
#     """ opens and parses a JSON file to an SBOM object
#
#     :param filepath: path to the json SBOM file
#     :return: SBOM object
#     """
#     return parse_file_as(SBOM, filepath)
#
#
# def load_sbom_from_json(input_data: dict) -> SBOM:
#     """ opens and parses a JSON file to an SBOM object
#
#     :param input_data:  dict from json SBOM file
#     :return: SBOM object
#     """
#     return SBOM(**input_data)


# def filter_sbom(filter_list: set, sbom_data: SBOM) -> List[dict]:
#     """Filter SBOM by a set of keywords
#
#     >  filter_sbom({'name','type'}, ot)
#     >  [{'artifacts': [{'name': 'SQLAlchemy', 'type': 'python'}]},
#         {'artifacts': [{'name': 'fastapi', 'type': 'python'}]},
#         {'artifacts': [{'name': 'uvicorn', 'type': 'python'}]}]
#
#     """
#     sbom_filter = []
#
#     for index, _ in enumerate(sbom_data.artifacts):
#         # TODO: artifacts keyword could be passed in as a parameter to the
#         # function.
#         sbom_filter.append(sbom_data.dict(include={'artifacts': {index: filter_list}}))
#
#     return sbom_filter
#
#
# def convert_filter_to_sets(filtered_sbom: List[dict]) -> List[set]:
#     """Convert the filtered sbom into a list of sets
#     > convert_filter_to_sets(< data structure here>)
#     > [{('name', 'SQLAlchemy'), ('type', 'python')},
#        {('name', 'fastapi'), ('type', 'python')},
#        {('name', 'uvicorn'), ('type', 'python')}]
#
#     """
#     converted_list_set = []
#
#     for data in filtered_sbom:
#         # TODO: artifacts keyword could be passed in as a parameter along
#         # index.
#         converted_list_set.append(set(data['artifacts'][0].items()))
#
#     return converted_list_set
#

def get_members_for_object(obj: Any, ignore_list: List[str], default_ignores: List[str] = ['Config']) -> List:
    """ gets a list of public attributes for a given python object

    :param obj: a python object
    :param ignore_list: a list of attribute names to ignore / filter out
    :param default_ignores: pydantic BaseModel specific attributes not needed for comparison.
    :return: a list of attribute names
    """
    # get the attributes of the class, ignoring routines
    all_attributes = getmembers(obj, lambda a: not (isroutine(a)))
    # filter out any private, special or collection attrs
    return [a[0] for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))
            and not (a[0].startswith('_')) and not (a[0] in default_ignores + ignore_list)]
