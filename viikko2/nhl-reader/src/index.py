import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich import box

from player import Player

def get_player_data(season, nationality):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    response = requests.get(url, timeout=20)
    return [Player(player_dict) for player_dict in response.json()
            if player_dict['nationality'] == nationality]

def create_table(season, nationality):
    table = Table(title=f"Top {nationality} Players - Season {season}", box=box.ROUNDED)
    columns = [
        ("Rank", "center", "cyan"),
        ("Name", "left", "magenta"),
        ("Team", "left", "green"),
        ("Goals", "right", "red"),
        ("Assists", "right", "blue"),
        ("Points", "right", "bold yellow"),
        ("Games", "right", "white")
    ]
    for name, justify, style in columns:
        table.add_column(name, justify=justify, style=style)
    return table

def add_player_rows(table, players):
    sorted_players = sorted(players, key=lambda p: p.goals + p.assists, reverse=True)
    medals = ["🥇 1", "🥈 2", "🥉 3"]

    for i, player in enumerate(sorted_players, 1):
        rank = medals[i-1] if i <= 3 else str(i)
        points = player.goals + player.assists
        table.add_row(
            rank,
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points),
            str(player.games)
        )

def display_welcome():
    console = Console()
    welcome_text = Text("NHL Player Statistics", style="bold magenta")
    console.print(Panel(welcome_text, box=box.DOUBLE, style="cyan"))
    return console

def get_user_input():
    season = Prompt.ask("[bold green]Select season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]")
    nationality = Prompt.ask("[bold blue]Select nationality [USA/FIN/CAN/SWE/CZE/RUS/FLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]")
    return season, nationality

def main():
    console = display_welcome()
    season, nationality = get_user_input()

    with console.status(f"[bold green]Fetching player data for {season}...", spinner="dots"):
        players = get_player_data(season, nationality)

    if not players:
        console.print(f"[bold red]No players found for nationality {nationality} in season {season}[/bold red]")
        return

    table = create_table(season, nationality)
    add_player_rows(table, players)
    console.print(table)

if __name__ == "__main__":
    main()
