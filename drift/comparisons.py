from inspect import getmembers, isroutine
from typing import List, Any

from .data.model import Artifact, ArtifactDelta, DistroDelta, Distro, Source, SourceDelta, Target, TargetDelta


def get_members_for_object(obj: Any, ignore_list: List[str]) -> List:
    """ gets a list of public attributes for a given python object

    :param obj: a python object
    :param ignore_list: a list of attribute names to ignore / filter out
    :return: a list of attribute names
    """
    # get the attributes of the class, ignoring routines
    all_attributes = getmembers(obj, lambda a: not (isroutine(a)))
    # filter out any private, special or collection attrs
    return [a[0] for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))
            and not (a[0].startswith('_')) and not (a[0] in ignore_list)]


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


def compare_artifact(base: Artifact, other: Artifact) -> ArtifactDelta:
    """ compares two artifacts and returns just the differences

    :param base: artifact from base SBom
    :param other: artifact from other SBom
    :return: ArtifactDelta object containing differences
    """
    delta = ArtifactDelta(name=base.name)
    is_changed = False

    # # get the attributes of the class, ignoring routines
    # all_attributes = getmembers(base, lambda a: not (isroutine(a)))
    # # filter out any private, special or collection attrs
    # attributes = [a for a in all_attributes if not (a[0].startswith('__') and a[0].endswith('__'))
    #               and not (a[0].startswith('_'))
    #               and not(a[0] in ['Config', 'id', 'locations', 'cpes', 'licenses'])]

    attributes = [attribute for attribute in get_members_for_object(
        base, ['Config', 'id', 'locations', 'cpes', 'licenses'])]

    for attribute in attributes:
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))
            is_changed = True

    # delta.cpes = compare_string_lists(base.cpes, other.cpes)
    # is_changed = len(delta.cpes) > 0

    delta.licenses = compare_string_lists(base.licenses, other.licenses)
    is_changed = len(delta.licenses) > 0

    # if nothing has changed, then return None
    if is_changed:
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

    delta.target = compare_target(Target(**base.target), Target(**other.target))

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

    attributes = [attribute for attribute in get_members_for_object(
        base, ['Config', 'id', 'tags', 'layers', 'repoDigests'])]

    for attribute in attributes:
        if getattr(base, attribute) != getattr(other, attribute):
            setattr(delta, attribute, getattr(other, attribute))
            is_changed = True

    delta.tags = compare_string_lists(base.tags, other.tags)
    is_changed = len(delta.tags) > 0

    # TODO: implement layers compare

    delta.repoDigests = compare_string_lists(base.repoDigests, other.repoDigests)
    is_changed = len(delta.repoDigests) > 0

    if is_changed:
        return delta
    return None
