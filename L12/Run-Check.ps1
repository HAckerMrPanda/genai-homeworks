param([ValidateSet('ru', 'en')][string]$Lang = 'ru')
$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
$taskPython = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath (Join-Path $PSScriptRoot 'server.py'))) {
    Write-Host 'Create server.py with AI first. See AI_PROMPT_RU.txt / AI_PROMPT_EN.txt.'
    exit 1
}
if (-not (Test-Path -LiteralPath $taskPython)) {
    Write-Host 'First run: creating a local Python environment...'
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 -m venv (Join-Path $PSScriptRoot '.venv')
    } elseif (Get-Command python -ErrorAction SilentlyContinue) {
        & python -m venv (Join-Path $PSScriptRoot '.venv')
    } else {
        Write-Host 'Install Python 3.11+ from https://www.python.org/downloads/ and run again.'
        exit 1
    }
    if ($LASTEXITCODE -ne 0) { exit 1 }
}
& $taskPython -c "import sys; assert sys.version_info >= (3,11), 'Python 3.11+ required'"
if ($LASTEXITCODE -ne 0) { exit 1 }
& $taskPython -c "import importlib.util as u, importlib.metadata as m, sys; sys.exit(0 if u.find_spec('mcp') is not None and m.version('mcp') == '2.3.0' else 1)" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host 'First run: installing the MCP library. Internet is needed...'
    & $taskPython -m pip install -r (Join-Path $PSScriptRoot 'requirements.txt') --disable-pip-version-check
    if ($LASTEXITCODE -ne 0) { exit 1 }
}
& $taskPython (Join-Path $PSScriptRoot 'check.py') --lang $Lang
exit $LASTEXITCODE
