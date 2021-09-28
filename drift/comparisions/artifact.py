from typing import List

from ..data.model import Artifact


def attribute_differences(base: Artifact, other: Artifact):
    differences = {}

    if base.name != other.name:
        differences['name'] = other.name

    if base.version != other.version:
        differences['version'] = other.version

    if base.type != other.type:
        differences['type'] = other.type

    if base.foundBy != other.foundBy:
        differences['foundBy'] = other.foundBy

    if base.purl != other.purl:
        differences['purl'] = other.purl

    if base.language != other.language:
        differences['language'] = other.language


def cpe_differences(base_cpes: List[str], other_cpes: List[str]):
    if base_cpes.sort() != other_cpes.sort():
        # lists can have items added, changed or removed.
        cpes_differences = {'added': [], 'removed': [], 'changed': []}
        for base_cpe in base_cpes:
            for other_cpe in other_cpes:
                if base_cpe == other_cpe:
                    break


def artifact_count(base: list, other: list) -> bool:
    return len(base) == len(other)


def artifact_equality(base: list, other: list) -> bool:
    # are the artifacts the same between both lists
    pass


def version_check(base: list, other: list):
    pass
