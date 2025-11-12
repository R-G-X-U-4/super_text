; Script for Super Text setup
; Created for Inno Setup 6.6.0
; ---------------------------------------------

[Setup]
AppName=Super Text
AppVersion=1.0
AppPublisher=RGXU4
DefaultDirName={autopf}\Super Text
DefaultGroupName=Super Text
OutputDir=.\installer
OutputBaseFilename=setup
SetupIconFile=assets\logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
; --- Main Executable ---
Source: "dist\SuperText.exe"; DestDir: "{app}"; Flags: ignoreversion
; --- UI Folder (with .ui and icons) ---
Source: "ui\*"; DestDir: "{app}\ui"; Flags: recursesubdirs createallsubdirs
; --- Assets Folder (for logo, etc.) ---
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs
; --- Optional files ---
; Source: "readme.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
; Start menu icon
Name: "{autoprograms}\Super Text"; Filename: "{app}\SuperText.exe"; IconFilename: "{app}\assets\logo.ico"
; Desktop icon (optional)
Name: "{autodesktop}\Super Text"; Filename: "{app}\SuperText.exe"; IconFilename: "{app}\assets\logo.ico"; Tasks: desktopicon

[Run]
; Launch app after install
Filename: "{app}\SuperText.exe"; Description: "Launch Super Text"; Flags: nowait postinstall skipifsilent
