from rich.console import Console

console = Console()

def show_menu():
    console.print("\n[bold cyan]NTL-SysToolbox[/bold cyan]")
    console.print("1. Diagnostic")
    console.print("2. Sauvegarde WMS")
    console.print("3. Audit d'obsolescence")
    console.print("0. Quitter")

    return input("Choix : ")
