# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:08:45+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Empty(BaseModel):
    pass


class File(BaseModel):
    content: Optional[str] = Field(None, description='Required. Textual Content.')
    fingerprint: Optional[str] = Field(
        None, description='Fingerprint (e.g. github sha) associated with the `File`.'
    )
    name: Optional[str] = Field(None, description='Required. File name.')


class FunctionCall(BaseModel):
    args: Optional[List] = Field(
        None, description='The arguments that were provided to the function.'
    )
    function: Optional[str] = Field(None, description='Name of the function invoked.')


class ExecutableVersion(Enum):
    RELEASE_EXECUTABLE_VERSION_UNSPECIFIED = 'RELEASE_EXECUTABLE_VERSION_UNSPECIFIED'
    FIREBASE_RULES_EXECUTABLE_V1 = 'FIREBASE_RULES_EXECUTABLE_V1'
    FIREBASE_RULES_EXECUTABLE_V2 = 'FIREBASE_RULES_EXECUTABLE_V2'


class Language(Enum):
    LANGUAGE_UNSPECIFIED = 'LANGUAGE_UNSPECIFIED'
    FIREBASE_RULES = 'FIREBASE_RULES'
    EVENT_FLOW_TRIGGERS = 'EVENT_FLOW_TRIGGERS'


class GetReleaseExecutableResponse(BaseModel):
    executable: Optional[str] = Field(
        None,
        description='Executable view of the `Ruleset` referenced by the `Release`.',
    )
    executableVersion: Optional[ExecutableVersion] = Field(
        None, description='The Rules runtime version of the executable.'
    )
    language: Optional[Language] = Field(
        None, description='`Language` used to generate the executable bytes.'
    )
    rulesetName: Optional[str] = Field(
        None, description='`Ruleset` name associated with the `Release` executable.'
    )
    syncTime: Optional[str] = Field(
        None,
        description='Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the sync_time (inclusive).',
    )
    updateTime: Optional[str] = Field(
        None, description='Timestamp for the most recent `Release.update_time`.'
    )


class Severity(Enum):
    SEVERITY_UNSPECIFIED = 'SEVERITY_UNSPECIFIED'
    DEPRECATION = 'DEPRECATION'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


class Metadata(BaseModel):
    services: Optional[List[str]] = Field(
        None,
        description='Services that this ruleset has declarations for (e.g., "cloud.firestore"). There may be 0+ of these.',
    )


class Release(BaseModel):
    createTime: Optional[str] = Field(
        None, description='Output only. Time the release was created.'
    )
    name: Optional[str] = Field(
        None,
        description='Required. Format: `projects/{project_id}/releases/{release_id}`',
    )
    rulesetName: Optional[str] = Field(
        None,
        description='Required. Name of the `Ruleset` referred to by this `Release`. The `Ruleset` must exist for the `Release` to be created.',
    )
    updateTime: Optional[str] = Field(
        None, description='Output only. Time the release was updated.'
    )


class Result(BaseModel):
    undefined: Optional[Empty] = Field(
        None,
        description='The result is undefined, meaning the result could not be computed.',
    )
    value: Optional[Any] = Field(
        None,
        description='The result is an actual value. The type of the value must match that of the type declared by the service.',
    )


class Source(BaseModel):
    files: Optional[List[File]] = Field(
        None, description='Required. `File` set constituting the `Source` bundle.'
    )


class SourcePosition(BaseModel):
    column: Optional[int] = Field(
        None,
        description='First column on the source line associated with the source fragment.',
    )
    currentOffset: Optional[int] = Field(
        None, description='Start position relative to the beginning of the file.'
    )
    endOffset: Optional[int] = Field(
        None, description='End position relative to the beginning of the file.'
    )
    fileName: Optional[str] = Field(None, description='Name of the `File`.')
    line: Optional[int] = Field(
        None, description='Line number of the source fragment. 1-based.'
    )


class Expectation(Enum):
    EXPECTATION_UNSPECIFIED = 'EXPECTATION_UNSPECIFIED'
    ALLOW = 'ALLOW'
    DENY = 'DENY'


class ExpressionReportLevel(Enum):
    LEVEL_UNSPECIFIED = 'LEVEL_UNSPECIFIED'
    NONE = 'NONE'
    FULL = 'FULL'
    VISITED = 'VISITED'


class PathEncoding(Enum):
    ENCODING_UNSPECIFIED = 'ENCODING_UNSPECIFIED'
    URL_ENCODED = 'URL_ENCODED'
    PLAIN = 'PLAIN'


class State(Enum):
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'


class UpdateReleaseRequest(BaseModel):
    release: Optional[Release] = Field(
        None, description='Required. `Release` to update.'
    )
    updateMask: Optional[str] = Field(
        None, description='Specifies which fields to update.'
    )


class ValueCount(BaseModel):
    count: Optional[int] = Field(
        None, description='The amount of times that expression returned.'
    )
    value: Optional[Any] = Field(None, description='The return value of the expression')


class VisitedExpression(BaseModel):
    sourcePosition: Optional[SourcePosition] = Field(
        None,
        description='Position in the `Source` or `Ruleset` where an expression was visited.',
    )
    value: Optional[Any] = Field(
        None,
        description='The evaluated value for the visited expression, e.g. true/false',
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class Arg(BaseModel):
    anyValue: Optional[Empty] = Field(
        None, description='Argument matches any value provided.'
    )
    exactValue: Optional[Any] = Field(
        None, description='Argument exactly matches value provided.'
    )


class ExpressionReport(BaseModel):
    children: Optional[List[ExpressionReport]] = Field(
        None, description='Subexpressions'
    )
    sourcePosition: Optional[SourcePosition] = Field(
        None, description='Position of expression in original rules source.'
    )
    values: Optional[List[ValueCount]] = Field(
        None, description='Values that this expression evaluated to when encountered.'
    )


class FunctionMock(BaseModel):
    args: Optional[List[Arg]] = Field(
        None,
        description='The list of `Arg` values to match. The order in which the arguments are provided is the order in which they must appear in the function invocation.',
    )
    function: Optional[str] = Field(
        None,
        description='The name of the function. The function name must match one provided by a service declaration.',
    )
    result: Optional[Result] = Field(
        None, description='The mock result of the function call.'
    )


class Issue(BaseModel):
    description: Optional[str] = Field(None, description='Short error description.')
    severity: Optional[Severity] = Field(None, description='The severity of the issue.')
    sourcePosition: Optional[SourcePosition] = Field(
        None, description='Position of the issue in the `Source`.'
    )


class ListReleasesResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='The pagination token to retrieve the next page of results. If the value is empty, no further results remain.',
    )
    releases: Optional[List[Release]] = Field(
        None, description='List of `Release` instances.'
    )


class Ruleset(BaseModel):
    createTime: Optional[str] = Field(
        None, description='Output only. Time the `Ruleset` was created.'
    )
    metadata: Optional[Metadata] = Field(
        None, description='Output only. The metadata for this ruleset.'
    )
    name: Optional[str] = Field(
        None,
        description='Output only. Name of the `Ruleset`. The ruleset_id is auto generated by the service. Format: `projects/{project_id}/rulesets/{ruleset_id}`',
    )
    source: Optional[Source] = Field(
        None, description='Required. `Source` for the `Ruleset`.'
    )


class TestCase(BaseModel):
    expectation: Optional[Expectation] = Field(None, description='Test expectation.')
    expressionReportLevel: Optional[ExpressionReportLevel] = Field(
        None, description='Specifies what should be included in the response.'
    )
    functionMocks: Optional[List[FunctionMock]] = Field(
        None,
        description='Optional function mocks for service-defined functions. If not set, any service defined function is expected to return an error, which may or may not influence the test outcome.',
    )
    pathEncoding: Optional[PathEncoding] = Field(
        None,
        description='Specifies whether paths (such as request.path) are encoded and how.',
    )
    request: Optional[Any] = Field(
        None,
        description='Request context. The exact format of the request context is service-dependent. See the appropriate service documentation for information about the supported fields and types on the request. Minimally, all services support the following fields and types: Request field | Type ---------------|----------------- auth.uid | `string` auth.token | `map` headers | `map` method | `string` params | `map` path | `string` time | `google.protobuf.Timestamp` If the request value is not well-formed for the service, the request will be rejected as an invalid argument.',
    )
    resource: Optional[Any] = Field(
        None,
        description='Optional resource value as it appears in persistent storage before the request is fulfilled. The resource type depends on the `request.path` value.',
    )


class TestResult(BaseModel):
    debugMessages: Optional[List[str]] = Field(
        None,
        description='Debug messages related to test execution issues encountered during evaluation. Debug messages may be related to too many or too few invocations of function mocks or to runtime errors that occur during evaluation. For example: ```Unable to read variable [name: "resource"]```',
    )
    errorPosition: Optional[SourcePosition] = Field(
        None,
        description='Position in the `Source` or `Ruleset` where the principle runtime error occurs. Evaluation of an expression may result in an error. Rules are deny by default, so a `DENY` expectation when an error is generated is valid. When there is a `DENY` with an error, the `SourcePosition` is returned. E.g. `error_position { line: 19 column: 37 }`',
    )
    expressionReports: Optional[List[ExpressionReport]] = Field(
        None,
        description='The mapping from expression in the ruleset AST to the values they were evaluated to. Partially-nested to mirror AST structure. Note that this field is actually tracking expressions and not permission statements in contrast to the "visited_expressions" field above. Literal expressions are omitted.',
    )
    functionCalls: Optional[List[FunctionCall]] = Field(
        None,
        description='The set of function calls made to service-defined methods. Function calls are included in the order in which they are encountered during evaluation, are provided for both mocked and unmocked functions, and included on the response regardless of the test `state`.',
    )
    state: Optional[State] = Field(None, description='State of the test.')
    visitedExpressions: Optional[List[VisitedExpression]] = Field(
        None,
        description='The set of visited permission expressions for a given test. This returns the positions and evaluation results of all visited permission expressions which were relevant to the test case, e.g. ``` match /path { allow read if: } ``` For a detailed report of the intermediate evaluation states, see the `expression_reports` field',
    )


class TestRulesetResponse(BaseModel):
    issues: Optional[List[Issue]] = Field(
        None,
        description='Syntactic and semantic `Source` issues of varying severity. Issues of `ERROR` severity will prevent tests from executing.',
    )
    testResults: Optional[List[TestResult]] = Field(
        None,
        description='The set of test results given the test cases in the `TestSuite`. The results will appear in the same order as the test cases appear in the `TestSuite`.',
    )


class TestSuite(BaseModel):
    testCases: Optional[List[TestCase]] = Field(
        None, description='Collection of test cases associated with the `TestSuite`.'
    )


class ListRulesetsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='The pagination token to retrieve the next page of results. If the value is empty, no further results remain.',
    )
    rulesets: Optional[List[Ruleset]] = Field(
        None, description='List of `Ruleset` instances.'
    )


class TestRulesetRequest(BaseModel):
    source: Optional[Source] = Field(
        None,
        description='Optional `Source` to be checked for correctness. This field must not be set when the resource name refers to a `Ruleset`.',
    )
    testSuite: Optional[TestSuite] = Field(
        None,
        description='The tests to execute against the `Source`. When `Source` is provided inline, the test cases will only be run if the `Source` is syntactically and semantically valid. Inline `TestSuite` to run.',
    )


ExpressionReport.model_rebuild()
