# CoolPi

Standalone split of the original app in `microsoftcopilotcodeusedonpi`. Original code and app name kept, with only local-path/update wiring and approved credential removal/prompt changes. The source repository is untouched.

## What it does and needs

Terminal system, file and package menus. Requires Raspberry Pi OS/Debian tools including apt and sudo. Some menus modify the system or publish information. The Gist publishing feature has no authentication and may fail.

## Run

Use the Pi App Store to install and launch. Installation only checks Bash syntax; it does not run administrative actions or install prerequisites. Read the script before selecting Run.

From an extracted checkout:

```sh
bash app-store.sh install
bash app-store.sh run
```

## Safety and limits

This is the original prototype, not a rewritten or hardware-validated release. Some inherited operations may fail or interrupt the system. Prompts do not guarantee safe recovery. Network passwords are requested locally where needed; no OS password is embedded. Use normal sudo authentication. Don't enter credentials on an untrusted/shared terminal.

Do not run unattended on an important Pi. Keep backups. Only administer systems/networks you own or have permission to use.

Linux checks: Bash syntax and packaging tests pass. Raspberry Pi hardware and non-Linux systems are untested. No privileged action was run during validation.

## Tests

```sh
python3 test_packaging.py
```

Version 1.0.0 is the standalone packaging version, not a claim that inherited features changed.

## Fullscreen Store launch

Version 1.0.1 adds a full-terminal interface when launched through the Store. Python 3 with curses and an interactive terminal are required. The original source remains available directly. Arrow keys select, Enter opens, and Q/Esc returns. Original commands temporarily take over the terminal for their prompts and output, then return to the full-terminal menu. Nested selection menus now use fullscreen arrow-key lists through controls-fullscreen.sh. Original source is unchanged; commands and free-form/password/confirmation prompts temporarily retain the terminal. CoolPi fullscreen self-updates fetch the matching fullscreen shell, not the original plain-menu shell. Passwords, sudo, confirmations, package changes and original limitations retain their old behavior. No administrative/package/transfer action ran during validation. Linux terminal checks passed; physical Raspberry Pi and non-Linux systems are untested.
