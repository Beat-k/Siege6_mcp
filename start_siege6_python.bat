@echo off
echo Starting Siege6 MCP Server (Python version)...
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the Python MCP server
python siege6_mcp.py

REM Keep terminal open if there's an error
if %errorlevel% neq 0 (
    echo.
    echo Press any key to exit...
    pause >nul
)