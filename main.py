import sys, csv, subprocess, time, os
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

IN = sys.argv[1] if len(sys.argv) > 1 else 'mätdata.csv'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'temperatur.png'

times = []
temps = []

with open(IN, encoding='utf-8', newline='') as f:
    r = csv.reader(f)
    next(r, None)
    for row in r:
        if len(row) < 2:
            continue
        t = row[0].strip()
        s = row[1].strip()
        try:
            dt = datetime.strptime(t, '%H:%M')
            temp = float(s)
        except ValueError:
            try:
                dt = datetime.strptime(t, '%H:%M:%S')
                temp = float(s)
            except ValueError:
                continue
        times.append(dt)
        temps.append(temp)

if not times:
    raise SystemExit("Ingen giltig data hittades.")

times, temps = zip(*sorted(zip(times, temps)))

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(times, temps, marker='o', linestyle='-')
ax.set(title='Temperatur under dagen', xlabel='Tid', ylabel='Temperatur (°C)')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
ax.grid(alpha=0.4, linestyle='--')
fig.tight_layout()
fig.savefig(OUT, dpi=300)
plt.close(fig)

if not os.path.isfile(OUT):
    raise SystemExit(f"Fel: Bilden '{OUT}' kunde inte sparas.")

print(f"Diagram sparat som '{OUT}'.")

subprocess.Popen(['cmd', '/c', 'start', '', OUT], shell=True)
time.sleep(6)
subprocess.run([
    'powershell',
    '-Command',
    f"Get-Process | Where-Object {{$_.MainWindowTitle -like '*{OUT}*'}} | Stop-Process"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
