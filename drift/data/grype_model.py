from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class Metrics(BaseModel):
    baseScore: float
    exploitabilityScore: float
    impactScore: float


class VendorMetadata(BaseModel):
    BaseSeverity: Optional[str] = None
    Status: Optional[str] = None


class Cvs(BaseModel):
    version: str
    vector: str
    metrics: Metrics
    vendorMetadata: VendorMetadata


class Fix(BaseModel):
    versions: List[str]
    state: str


class Advisory(BaseModel):
    id: str
    link: str


class Vulnerability(BaseModel):
    id: str
    dataSource: str
    namespace: str
    severity: str
    urls: List[str]
    description: str
    cvss: List[Cvs]
    fix: Fix
    advisories: List[Advisory]


class Metrics1(BaseModel):
    baseScore: float
    exploitabilityScore: float
    impactScore: float


class Cvs1(BaseModel):
    version: str
    vector: str
    metrics: Metrics1
    vendorMetadata: Dict[str, Any]


class RelatedVulnerability(BaseModel):
    id: str
    dataSource: str
    namespace: str
    severity: str
    urls: List[str]
    description: str
    cvss: List[Cvs1]


class Distro(BaseModel):
    type: str
    version: str


class SearchedBy(BaseModel):
    distro: Optional[Distro] = None
    namespace: str
    cpes: Optional[List[str]] = None
    language: Optional[str] = None


class Found(BaseModel):
    versionConstraint: str
    cpes: Optional[List[str]] = None


class MatchDetail(BaseModel):
    matcher: str
    searchedBy: SearchedBy
    found: Found


class Location(BaseModel):
    path: str
    layerID: Optional[str] = None


class Metadatum(BaseModel):
    SourceRpm: str


class Artifact(BaseModel):
    name: str
    version: str
    type: str
    locations: List[Location]
    language: str
    licenses: List[str]
    cpes: List[str]
    purl: str
    metadata: Optional[Metadatum]


class Match(BaseModel):
    vulnerability: Vulnerability
    relatedVulnerabilities: List[RelatedVulnerability]
    matchDetails: List[MatchDetail]
    artifact: Artifact


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
    layers: List[Layer]
    manifest: str
    config: str
    repoDigests: List


class Source(BaseModel):
    type: str
    target: Any
    # target: Union[Target, str]


class Distro1(BaseModel):
    name: str
    version: str
    idLike: str


class Log(BaseModel):
    Structured: bool
    Level: str
    FileLocation: str


class CliOptions(BaseModel):
    ConfigPath: str
    Verbosity: int


class Db(BaseModel):
    Dir: str
    UpdateURL: str
    AutoUpdate: bool
    ValidateByHashOnStart: bool


class Dev(BaseModel):
    ProfileCPU: bool


class Registry(BaseModel):
    insecure_skip_tls_verify: bool = Field(..., alias="insecure-skip-tls-verify")
    auth: List


class Configuration(BaseModel):
    ConfigPath: str
    Output: str
    OutputTemplateFile: str
    Scope: str
    Quiet: bool
    Log: Log
    CliOptions: CliOptions
    Db: Db
    Dev: Dev
    CheckForAppUpdate: bool
    FailOn: str
    registry: Registry


class Db1(BaseModel):
    built: str
    schemaVersion: int
    location: str
    checksum: str
    error: Any


class Descriptor(BaseModel):
    name: str
    version: str
    configuration: Configuration
    db: Db1


class Model(BaseModel):
    matches: List[Match]
    source: Source
    distro: Distro1
    descriptor: Descriptor
