@ECHO OFF

REM 1. Define the temporary VBS file path
SET TempVBSFile=%TEMP%\~tmpSendKeysTemp.vbs

REM 2. Create the VBScript content to send {F11} or !{ENTER} (Alt+Enter)
IF EXIST "%TempVBSFile%" DEL /F /Q "%TempVBSFile%"
ECHO Set WshShell = WScript.CreateObject("WScript.Shell") >>"%TempVBSFile%"
ECHO Wscript.Sleep 500 >>"%TempVBSFile%"
REM Use {F11} for modern apps/browsers, or !{ENTER} for old console
ECHO WshShell.SendKeys "{F11}" >>"%TempVBSFile%"
ECHO Wscript.Sleep 500 >>"%TempVBSFile%"

REM 3. Execute the VBScript
CSCRIPT //nologo "%TempVBSFile%"

REM 4. Clean up the temporary VBS file (optional)
IF EXIST "%TempVBSFile%" DEL /F /Q "%TempVBSFile%"


python "%~dp0main.py"