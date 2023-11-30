"""Test Python-related code."""

import requests_mock

from pyenvtool.python import PYTHON_DOWNLOADS, PyVer, python_supported_versions

PYTHON_HTML_OUTPUT = """
<div class="row active-release-list-widget">

<h2 class="widget-title">Active Python Releases</h2>

<div class="list-row-headings">
    <span class="release-version">Python version</span>
    <span class="release-status">Maintenance status</span>
    <span class="release-start">First released</span>
    <span class="release-end">End of support</span>
    <span class="release-pep">Release schedule</span>
</div>
<ol class="list-row-container menu">
    <li>
        <span class="release-version">3.13</span>
        <span class="release-status"><a href="https://www.python.org/download/pre-releases/">prerelease</a></span>
        <span class="release-start">2024-10-01 (planned)</span>
        <span class="release-end">2029-10</span>
        <span class="release-pep"><a href="https://peps.python.org/pep-0719/">PEP 719</a></span>
    </li>
    <li>
        <span class="release-version">3.12</span>
        <span class="release-status">bugfix</span>
        <span class="release-start">2023-10-02</span>
        <span class="release-end">2028-10</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0693">PEP 693</a></span>
    </li>
    <li>
        <span class="release-version">3.11</span>
        <span class="release-status">bugfix</span>
        <span class="release-start">2022-10-24</span>
        <span class="release-end">2027-10</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0664">PEP 664</a></span>
    </li>
    <li>
        <span class="release-version">3.10</span>
        <span class="release-status">security</span>
        <span class="release-start">2021-10-04</span>
        <span class="release-end">2026-10</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0619">PEP 619</a></span>
    </li>
    <li>
        <span class="release-version">3.9</span>
        <span class="release-status">security</span>
        <span class="release-start">2020-10-05</span>
        <span class="release-end">2025-10</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0596">PEP 596</a></span>
    </li>
    <li>
        <span class="release-version">3.8</span>
        <span class="release-status">security</span>
        <span class="release-start">2019-10-14</span>
        <span class="release-end">2024-10</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0569">PEP 569</a></span>
    </li>
     <!--<li>
        <span class="release-version">2.7</span>
        <span class="release-status">end-of-life</span>
        <span class="release-start">2010-07-03</span>
        <span class="release-end">2020-01-01</span>
        <span class="release-pep"><a href="https://www.python.org/dev/peps/pep-0373">PEP 373</a></span>
    </li>-->
</ol>
</div>
"""  # noqa: E501


def test_python_supported() -> None:
    with requests_mock.Mocker() as mock_requests:
        mock_requests.get(PYTHON_DOWNLOADS, text=PYTHON_HTML_OUTPUT)

        supported = sorted(v for v, _ in python_supported_versions())

    assert supported == [
        PyVer(3, 8),
        PyVer(3, 9),
        PyVer(3, 10),
        PyVer(3, 11),
        PyVer(3, 12),
    ]
