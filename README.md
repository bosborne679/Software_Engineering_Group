# MCS - Minimalist Chat Server

## Requirements

Run `sudo apt install -y python3 python3-venv python3-pip` to ensure prereqs are installed.

## Developer Guide

To start developing, from a Linux machine with Git installed:

```bash
mkdir MCS
git clone https://github.com/bosborne679/Software_Engineering_Group MCS/
cd MCS
git checkout -b <branch name>
```

From there:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

When commiting a change run `git add <file(s)>` then `git commit -m <message>` and finally `git push origin <branch name>`

## Running

This script can be ran in two seperate instances which will change how it is being ran.

### Developer

If you are running this as a developer:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m MCS
```

This will start the server. From there it will await connections.

### Network Admin

From the server simply run `python3 -m MCS`. Future iterations will have this ran manually at start up.
