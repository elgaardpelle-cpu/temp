Detta är ett enkelt Python-script som läser temperaturdata från en CSV-fil, skapar ett diagram och visar det automatiskt i 6 sekunder innan fönstret stängs.

Vad det gör
Läser tid och temperatur från en CSV-fil (HH:MM eller HH:MM:SS).

Sorterar datan kronologiskt.

Skapar ett linjediagram med matplotlib.

Sparar diagrammet som en PNG-fil.

Öppnar bilden automatiskt.

Väntar 6 sekunder och stänger bildfönstret via PowerShell.

Kommandoöversikt (körs i scriptet)
Läser mätdata.csv eller fil angiven via argument.

Sparar som temperatur.png eller angivet filnamn.

Öppnar bilden med cmd /c start.

Stänger fönstret med PowerShell: Get-Process | Where-Object {$_.MainWindowTitle -like '*filnamn*'} | Stop-Process
