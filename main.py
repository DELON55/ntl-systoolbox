#!/usr/bin/env python3

"""
Main CLI for NTL SysToolbox (FULL VERSION)
Supports:
- Linux Diagnostic
- Windows Diagnostic
- SSH
- MySQL Dump
- CSV Export
- Obsolescence
"""

import sys

# =========================
# IMPORTS MODULES
# =========================

try:
    from modules.diagnostic.linux_diagnostic import run_linux_diagnostic
except:
    run_linux_diagnostic = None

try:
    from modules.diagnostic.windows_diagnostic import run_windows_diagnostic
except:
    run_windows_diagnostic = None

try:
    from modules.ssh.ssh_connect import ssh_connect
except:
    ssh_connect = None

try:
    from modules.backup.mysql_dump import dump_database
except:
    dump_database = None

try:
    from modules.backup.export_csv import export_table
except:
    export_table = None


# =========================
# OBSOLESCENCE MODULE
# =========================

def check_obsolescence():
    print("\n[+] Obsolescence check")
    try:
        import platform
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Version: {platform.version()}")
    except Exception as e:
        print(f"Erreur: {e}")


# =========================
# MENU
# =========================

def show_menu():
    print("""
=====================================
 NTL SysToolbox CLI - FULL
=====================================
1. Diagnostic Linux (serveurs)
2. Diagnostic Windows (AD / clients)
3. Connexion SSH
4. Dump MySQL (WMS)
5. Export CSV
6. Obsolescence
0. Quitter
=====================================
""")


# =========================
# MAIN LOOP
# =========================

def main():
    while True:
        show_menu()
        choice = input("Choix : ").strip()

        # =========================
        # LINUX DIAGNOSTIC
        # =========================
        if choice == "1":
            print("\n[+] Diagnostic Linux...")
            if run_linux_diagnostic:
                try:
                    run_linux_diagnostic()
                except Exception as e:
                    print(f"Erreur Linux diag: {e}")
            else:
                print("Module Linux non disponible")

        # =========================
        # WINDOWS DIAGNOSTIC
        # =========================
        elif choice == "2":
            print("\n[+] Diagnostic Windows...")
            if run_windows_diagnostic:
                try:
                    run_windows_diagnostic()
                except Exception as e:
                    print(f"Erreur Windows diag: {e}")
            else:
                print("Module Windows non disponible")

        # =========================
        # SSH
        # =========================
        elif choice == "3":
            print("\n[+] Connexion SSH...")
            if ssh_connect:
                host = input("IP : ")
                user = input("User : ")
                ssh_connect(host, user)
            else:
                print("Module SSH non disponible")

        # =========================
        # MYSQL DUMP
        # =========================
        elif choice == "4":
            print("\n[+] Dump MySQL...")
            if dump_database:
                try:
                    result = dump_database()
                    print(f"Dump créé : {result}")
                except Exception as e:
                    print(f"Erreur dump: {e}")
            else:
                print("Module dump non disponible")

        # =========================
        # EXPORT CSV
        # =========================
        elif choice == "5":
            print("\n[+] Export CSV...")
            if export_table:
                try:
                    export_table()
                    print("Export terminé")
                except Exception as e:
                    print(f"Erreur export: {e}")
            else:
                print("Module export non disponible")

        # =========================
        # OBSOLESCENCE
        # =========================
        elif choice == "6":
            check_obsolescence()

        # =========================
        # EXIT
        # =========================
        elif choice == "0":
            print("Au revoir")
            sys.exit(0)

        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
