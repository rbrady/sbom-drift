from __future__ import annotations

from typing import List, Optional, Any, Mapping

from pydantic import BaseModel, Field


class Location(BaseModel):
    path: str
    layerID: Optional[str] = None


class Digest(BaseModel):
    algorithm: str
    value: str


class File(BaseModel):
    path: str
    digest: Optional[Digest] = None
    isConfigFile: Optional[bool] = None
    size: Optional[str] = None


class Metadata(BaseModel):
    package: Optional[str] = None
    source: Optional[str] = None
    version: str
    sourceVersion: Optional[str] = None
    architecture: Optional[str] = None
    maintainer: Optional[str] = None
    installedSize: Optional[int] = None
    files: List[File]
    name: Optional[str] = None
    license: Optional[str] = None
    author: Optional[str] = None
    authorEmail: Optional[str] = None
    platform: Optional[str] = None
    sitePackagesRootPath: Optional[str] = None
    topLevelPackages: Optional[List[str]] = None


class Artifact(BaseModel):
    id: str
    name: str
    version: str
    type: str
    foundBy: str
    locations: List[Location]
    licenses: List[str]
    language: str
    cpes: List[str]
    purl: str
    metadataType: str
    metadata: Optional[Metadata] = None


class ArtifactDelta(BaseModel):
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


class ComparisonReport(BaseModel):
    artifacts: Optional[List[ArtifactDelta]] = []
    distro: Optional[DistroDelta] = None
    source: Optional[SourceDelta] = None


class Layer(BaseModel):
    mediaType: str
    digest: str
    size: int


class Target(BaseModel):
    userInput: str
    imageID: str
    manifestDigest: str
    mediaType: str
    tags: List[str]
    imageSize: int
    layers: Optional[List[Layer]] = None
    manifest: str
    config: str
    repoDigests: List[str]
    scope: str


class TargetDelta(BaseModel):
    userInput: Optional[str] = None
    imageID: Optional[str] = None
    manifestDigest: Optional[str] = None
    mediaType: Optional[str] = None
    tags: Optional[dict] = None
    imageSize: Optional[int] = None
    layers: Optional[List[Layer]] = None  # TODO: change to a dict for added/removed
    manifest: Optional[str] = None
    config: Optional[str] = None
    repoDigests: Optional[dict] = None
    scope: Optional[str] = None


class Source(BaseModel):
    type: str
    target: Any  # TODO: check this field with a source sbom


class SourceDelta(BaseModel):
    type: Optional[str] = None
    target: Optional[TargetDelta] = None


class Distro(BaseModel):
    name: str
    version: str
    idLike: str


class DistroDelta(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    idLike: Optional[str] = None


class Descriptor(BaseModel):
    name: str
    version: str


class Schema(BaseModel):
    version: str
    url: str


class SBOM(BaseModel):
    artifacts: List[Artifact]  # primary comparisons
    artifactRelationships: List  # examples empty
    source: Source  # same stage comparisons
    distro: Distro  # image / container cases

    # info about creator of sbom, used to setup comparison in future
    descriptor: Descriptor
    schema_: Schema = Field(..., alias='schema')
