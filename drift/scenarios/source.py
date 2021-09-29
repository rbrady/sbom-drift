from ..data.model import SBOM
from ..comparisions.artifact import attribute_differences, cpe_differences

# source to source
# - artifacts
#   - count
#   - version
#   - added
#   - removed


def source_to_source(base: SBOM, other: SBOM):
    # for the artifacts in the base doc, are they found in the other doc
    # [
    #     {
    #         'name': 'fastapi',
    #         'base': <artifact>,
    #         'other': <artifact>
    #     },
    #     {
    #         'name': 'SqlAlchemy',
    #         'base': None,
    #         'other': < artifact >
    #     },
    # ]
    #
    # artifact_list = []
    #
    # for base_artifact in base.artifacts:
    #     artifact_list.append({
    #         'name': base_artifact.name,
    #         'base': base_artifact,
    #     })
    #
    # for other_artifact in other.artifacts:
    #     artifact_list.append({
    #         'name': other_artifact.name,
    #         'other': other_artifact,
    #     })
    #
    # # find the other artifact that matches
    # other_artifact = [a for a in other.artifacts if a.name == base_artifact.name][0]
    # attribute_results = attribute_differences(base_artifact, other_artifact)
    pass
