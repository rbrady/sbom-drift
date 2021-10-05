from __future__ import annotations
from collections.abc import Iterable
from typing import List, Optional, Any, Mapping, Union

from pydantic import BaseModel, Field

from ...utils import get_members_for_object


class DeltaBaseModel(BaseModel):
    """

    """

    def is_changed(self, filter_list: List[str] = []) -> bool:
        """

        :param filter_list:
        :return:
        """

        ret = False

        attributes = [attribute for attribute in get_members_for_object(self, filter_list)]

        for attribute in attributes:
            item = getattr(self, attribute)
            if isinstance(item, Iterable):
                if len(item) > 0:
                    ret = True
            elif item:
                ret = True

        return ret


class ArtifactDelta(DeltaBaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    type: Optional[str] = None
    foundBy: Optional[str] = None
    locations: Optional[List[Location]] = None
    licenses: Optional[dict] = None
    language: Optional[str] = None
    cpes: Optional[dict] = {}
    purl: Optional[str] = None
    metadataType: Optional[str] = None
    metadata: Optional[Metadata] = None


class LayerDelta(DeltaBaseModel):
    mediaType: Optional[str] = None
    digest: Optional[str] = None
    size: Optional[int] = None


class TargetDelta(DeltaBaseModel):
    userInput: Optional[str] = None
    imageID: Optional[str] = None
    manifestDigest: Optional[str] = None
    mediaType: Optional[str] = None
    tags: Optional[dict] = None
    imageSize: Optional[int] = None
    layers: Optional[List[LayerDelta]] = None
    manifest: Optional[str] = None
    config: Optional[str] = None
    repoDigests: Optional[dict] = None
    scope: Optional[str] = None


class SourceDelta(DeltaBaseModel):
    type: Optional[str] = None
    target: Optional[TargetDelta] = None


class DistroDelta(DeltaBaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    idLike: Optional[str] = None


class LocationDelta(BaseModel):
    path: Optional[str] = None
    layerID: Optional[str] = None



