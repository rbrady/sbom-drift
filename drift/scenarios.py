from pprint import pprint

from .data.model import SBOM, ComparisonReport
from .comparisons import compare_artifact, compare_distro, compare_source, compare_target


def source_as_base(base: SBOM, other: SBOM) -> ComparisonReport:
    """

    :param base:
    :param other:
    :return:
    """
    result = ComparisonReport()
    result.artifacts = []

    base_artifact_names = set([artifact.name for artifact in base.artifacts])
    other_artifact_names = set([artifact.name for artifact in other.artifacts])

    # Q: have any of the artifacts in base been removed in other?
    removed = base_artifact_names.difference(other_artifact_names)

    # Q: have any of the artifacts in other been added?
    added = other_artifact_names.difference(base_artifact_names)

    # Q: have any of the artifacts found in both SBoMs changed in some way?
    # find all of the artifacts that were in both SBoMs
    common_artifact_names = base_artifact_names.intersection(other_artifact_names)

    # separate each SBoM copy of artifacts into a dict where the
    base_artifacts = {a.name: a for a in base.artifacts if a.name in common_artifact_names}
    other_artifacts = {a.name: a for a in base.artifacts if a.name in common_artifact_names}

    for name in common_artifact_names:
        artifact_delta = compare_artifact(base_artifacts.get(name), other_artifacts.get(name))
        print(artifact_delta)
        if artifact_delta is not None:
            result.artifacts.append(artifact_delta)

    return result


def image_as_base(base: SBOM, other: SBOM) -> ComparisonReport:
    """

    :param base:
    :param other:
    :return:
    """
    result = ComparisonReport()

    base_artifact_names = set([artifact.name for artifact in base.artifacts])
    other_artifact_names = set([artifact.name for artifact in other.artifacts])

    # Q: have any of the artifacts in base been removed in other?
    removed = base_artifact_names.difference(other_artifact_names)

    # Q: have any of the artifacts in other been added?
    added = other_artifact_names.difference(base_artifact_names)

    # Q: have any of the artifacts found in both SBoMs changed in some way?
    # find all of the artifacts that were in both SBoMs
    common_artifact_names = base_artifact_names.intersection(other_artifact_names)

    # separate each SBoM copy of artifacts into a dict where the
    base_artifacts = {a.name: a for a in base.artifacts if a.name in common_artifact_names}
    other_artifacts = {a.name: a for a in other.artifacts if a.name in common_artifact_names}

    for name in common_artifact_names:
        artifact_delta = compare_artifact(base_artifacts.get(name), other_artifacts.get(name))
        if artifact_delta is not None:
            result.artifacts.append(artifact_delta)

    result.distro = compare_distro(base.distro, other.distro)
    result.source = compare_source(base.source, other.source)

    return result
