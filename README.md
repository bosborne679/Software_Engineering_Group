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

When commiting a change run `git add <file(s)>` thenm `git commit -m <message>` and finally `git push origin <branch name>`
