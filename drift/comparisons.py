from collections.abc import Iterable
from typing import List, Any

from .data.model import Artifact, ArtifactDelta, DistroDelta, Distro, Layer, LayerDelta, Source, SourceDelta, Target,\
    TargetDelta

from .utils import get_members_for_object


def compare_string_lists(base: List[str], other: List[str]) -> dict:
    """ compares the members of a list of strings to separate any that were removed or added

    :param base: a list of strings to compare to
    :param other: a list of strings that may contain modifications
    :return: a dictionary with 'added' and 'removed' keys containing only the modified strings
    """
    result = {}
    # because there is no identifier or key in a list of strings,
    # we can only tell what was removed or added, not what is changed.

    items_removed = set(base).difference(set(other))
    if len(items_removed) > 0:
        result['removed'] = items_removed

    items_added = set(other).difference(set(base))
    if len(items_added) > 0:
        result['added'] = items_added

    return result


def compare_artifact_lists(base: List[Artifact], other: List[Artifact]) -> dict:
    result = {}

    base_artifact_names = set([artifact.name for artifact in base.artifacts])
    other_artifact_names = set([artifact.name for artifact in other.artifacts])

    # Q: have any of the artifacts in base been removed in other?
    removed = base_artifact_names.difference(other_artifact_names)
    result['removed'] = removed

    # Q: have any of the artifacts in other been added?
    added = other_artifact_names.difference(base_artifact_names)
    result['added'] = added

    # Q: have any of the artifacts found in both SBoMs changed in some way?
    # find all of the artifacts that were in both SBoMs
    common_artifact_names = base_artifact_names.intersection(other_artifact_names)

    # separate each SBoM copy of artifacts into a dict where the
    base_artifacts = {a.name: a for a in base.artifacts if a.name in common_artifact_names}
    other_artifacts = {a.name: a for a in other.artifacts if a.name in common_artifact_names}

    modified_artifacts = []
    for name in common_artifact_names:
        artifact_delta = compare_artifact(base_artifacts.get(name), other_artifacts.get(name))
        if artifact_delta:
            modified_artifacts.append(artifact_delta)

    result['modified'] = modified_artifacts
    return result


def compare_artifact(base: Artifact, other: Artifact) -> ArtifactDelta:
    """ compares two artifacts and returns just the differences

    :param base: artifact from base SBom
    :param other: artifact from other SBom
    :return: ArtifactDelta object containing differences
    """
    delta = ArtifactDelta(name=base.name)
    filter_list = ['id', 'locations', 'cpes']

    for attribute in get_members_for_object(base, filter_list + ['licenses']):
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))

    delta.licenses = compare_string_lists(base.licenses, other.licenses)

    # if nothing has changed, then return None
    if delta.is_changed(filter_list + ['name']):
        return delta
    return None


def compare_distro(base: Distro, other: Distro) -> DistroDelta:
    """

    :param base:
    :param other:
    :return:
    """
    delta = DistroDelta()
    is_changed = False

    for attribute in ['name', 'idLike', 'version']:
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))
            is_changed = True

    # if nothing has changed, then return None
    if is_changed:
        return delta
    return None


def compare_source(base: Source, other: Source):
    """

    :param base:
    :param other:
    :return:
    """
    delta = SourceDelta()
    if base.type != other.type:
        delta.type = other.type

    delta.target = compare_target(base.target, other.target)

    if delta.type is None and delta.target is None:
        return None
    return delta


def compare_target(base: Target, other: Target) -> TargetDelta:
    """

    :param base:
    :param other:
    :return:
    """
    delta = TargetDelta()
    is_changed = False
    filter_list = ['Config', 'id', 'layers', 'tags', 'repoDigests']

    attributes = [attribute for attribute in get_members_for_object(
        base, filter_list)]

    for attribute in attributes:
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))
            is_changed = True

# --

    # delta.tags = compare_string_lists(base.tags, other.tags)
    # if len(delta.tags.keys()) > 0:
    #     is_changed = True
    #
    # delta.repoDigests = compare_string_lists(base.repoDigests, other.repoDigests)
    # if len(delta.repoDigests.keys()) > 0:
    #     is_changed = True

# --

    for attribute in filter_list[3:]:
        setattr(delta, attribute, compare_string_lists(getattr(base, attribute), getattr(other, attribute)))
        if len(getattr(delta, attribute).keys()) > 0:
            is_changed = True
# --

    delta.layers = compare_layers_list(base.layers, other.layers)
    if len(delta.layers.keys()) > 0:
        is_changed = True

    if is_changed:
        return delta
    return None


def compare_layers_list(base: List[Layer], other: List[Layer]) -> dict:
    """

    :param base:
    :param other:
    :return:
    """
    result = {}

    base_map = {layer.digest: layer for layer in base}
    other_map = {layer.digest: layer for layer in other}

    base_layer_digests = set(base_map.keys())
    other_layer_digests = set(other_map.keys())

    result['removed'] = base_layer_digests.difference(other_layer_digests)
    result['added'] = other_layer_digests.difference(base_layer_digests)

    common_digests = base_layer_digests.intersection(other_layer_digests)
    modified_layers = []
    for digest in common_digests:
        delta = compare_layers(base_map[digest], other_map[digest])
        if delta:
            modified_layers.append(delta)

    result['modified'] = modified_layers
    return result


def compare_layers(base: Layer, other: Layer) -> LayerDelta:
    """

    :param base:
    :param other:
    :return:
    """
    delta = LayerDelta()
    is_changed = False

    for attribute in ['mediaType', 'size']:
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))
            is_changed = True

    if is_changed:
        return delta
    return None
