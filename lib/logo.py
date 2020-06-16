import os
w = '\x1b[1;37m'
b = '\x1b[1;36m'
g = '\x1b[1;32m'
y = '\x1b[1;33m'
r = '\x1b[1;31m'

def banner():
	os.system('clear')
	print(f'''{g}╔╦╗┬ ┬┬ ┌┬┐┬   ╔╗ ╔═╗
║║║│ ││  │ │───╠╩╗╠╣
╩ ╩└─┘┴─┘┴ ┴   ╚═╝╚{y} v0.1
{w}╔═════════════════════════════════════════╗
{w}║{y}*{w} Author{r} :{b} Anbia Nuansyah             {w}   ║
{w}║{y}*{w} Youtube{r}:{b} TANKERTV               {w}        ║
{w}║{y}*{w} Github{r} :{g} \x1b[4mhttps://github.com/tankertv11\x1b[0m{w}    ║
{w}╚═════════════════════════════════════════╝ ''')
