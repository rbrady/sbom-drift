from __future__ import annotations
from typing import List, Optional, Union

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


class Source(BaseModel):
    type: str
    target: Union[Target, str]  # TODO: check this field with a source sbom


class Distro(BaseModel):
    name: str
    version: str
    idLike: str


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
