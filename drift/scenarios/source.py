from ..data.model import SBOM

# source to source
# - artifacts
#   - count
#   - version
#   - added
#   - removed


def source_to_source(base: SBOM, other: SBOM):
    # for the artifacts in the base doc, are they found in the other doc
    for base_artifact in base.artifacts:


    pass


def artifact_count(base: list, other: list) -> bool:
    return len(base) == len(other)


def artifact_equality(base: list, other: list) -> bool:
    # are the artifacts the same between both lists
    pass


def version_check(base: list, other: list):

    pass
