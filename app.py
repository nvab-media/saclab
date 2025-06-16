from flask import Flask, send_from_directory 
import notes
app = Flask(__name__)


@app.route("/")
def serve_pdf():
    return send_from_directory(directory='sql', path='SecuriryLab.pdf')


@app.route("/alive")
def alive():
    return "Keep alive"


@app.route('/')
def home():
    return "Welcome to Command Reference! Use /linux, /window, /nmap or /<command>."

@app.route('/linux')
def linux():
    return "Linux Commands:\n" + "\n".join(notes.linux_cmds)

@app.route('/windows')
def windows():
    return "Windows Commands:\n" + "\n".join(notes.windows_cmds)

@app.route('/nmap')
def show_nmap():
    return "Nmap Commands:\n\n" + "\n\n".join(f"{k}:\n{v}" for k, v in notes.nmap_commands.items())

@app.route('/vul')
def show_vul():
    return "Vul scanning:\n\n" + "\n\n".join(f"{k}:\n{v}" for k, v in notes.vul.items())

@app.route('/index')
def show_index():
    return "Index Page:\n\n" + "\n\n".join(f"{k}:\n{v}" for k, v in notes.index.items())

@app.route('/<cmdname>')
def show_command(cmdname):
    cmd = cmdname.lower()
    if cmd in notes.command_usage:
        return f"{cmd.upper()}:\n\n{notes.command_usage[cmd]}"
    elif cmd in notes.nmap_commands:
        return f"NMAP - {cmd}:\n\n{notes.nmap_commands[cmd]}"
    return f"Command '{cmd}' not found."



if __name__ == "__main__":
    app.run()
