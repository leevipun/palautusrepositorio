import requests
from player import Player
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import box

def main():
    console = Console()
    
    # Welcome banner
    welcome_text = Text("NHL Player Statistics", style="bold magenta")
    console.print(Panel(welcome_text, box=box.DOUBLE, style="cyan"))
    
    # Season selection with style
    season_choices = "[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]"
    season = Prompt.ask(f"[bold green]Select season {season_choices}[/bold green]")
    
    # Nationality selection with style
    nationality_choices = "[USA/FIN/CAN/SWE/CZE/RUS/FLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]"
    nationality = Prompt.ask(f"[bold blue]Select nationality {nationality_choices}[/bold blue]")

    # Loading indicator
    with console.status(f"[bold green]Fetching player data for {season}...", spinner="dots"):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == nationality:            
            player = Player(player_dict)
            players.append(player)

    if not players:
        console.print(f"[bold red]No players found for nationality {nationality} in season {season}[/bold red]")
        return

    # Sort players by points (goals + assists)
    sorted_players = sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    # Create a beautiful table
    table = Table(title=f"Top {nationality} Players - Season {season}", box=box.ROUNDED)
    
    table.add_column("Rank", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta", min_width=20)
    table.add_column("Team", style="green", min_width=8)
    table.add_column("Goals", justify="right", style="red")
    table.add_column("Assists", justify="right", style="blue")
    table.add_column("Points", justify="right", style="bold yellow")
    table.add_column("Games", justify="right", style="white")

    # Add rows to the table
    for i, player in enumerate(sorted_players, 1):
        points = player.goals + player.assists
        
        # Add medal emojis for top 3
        rank = str(i)
        if i == 1:
            rank = "🥇 1"
        elif i == 2:
            rank = "🥈 2"
        elif i == 3:
            rank = "🥉 3"
        
        table.add_row(
            rank,
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points),
            str(player.games)
        )

    console.print(table)
        

if __name__ == "__main__":
    main()