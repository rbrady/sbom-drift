from pprint import pprint

from .data.models.sbom import SBOM
from .data.models.reports import ComparisonReport
from .comparisons import compare_artifact, compare_distro, compare_source, compare_target, compare_artifact_lists


def source_as_base(base: SBOM, other: SBOM) -> ComparisonReport:
    """

    :param base:
    :param other:
    :return:
    """
    return ComparisonReport(artifacts=compare_artifact_lists(base.artifacts, other.artifacts))


def image_as_base(base: SBOM, other: SBOM) -> ComparisonReport:
    """

    :param base:
    :param other:
    :return:
    """
    return ComparisonReport(
        artifacts=compare_artifact_lists(base.artifacts, other.artifacts),
        distro=compare_distro(base.distro, other.distro),
        source=compare_source(base.source, other.source)
    )
