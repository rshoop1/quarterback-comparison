from drafter import *
from dataclasses import dataclass
from bakery import assert_equal
from qbdata import Player, players

set_website_title("NFL Quarterback Comparison")

set_site_information(
    author="Ryan Shoop",
    description="Compare NFL quarterbacks using their 2025 season statistics.",
    sources="NFL.com 2025 Player Passing Statistics, FF Today 2025 Quarterback Statistics, and Drafter documentation.",
    planning=["Copy of CS1 Final Project 0: Pick a Problem.pdf", "Copy of CS1 Final Project 0: Pick a Problem.pdf" ],
    links=[],
)

hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    players: list[Player]
    player1: str
    player2: str
    category: str
    comparisons: int
    
def find_player(players: list[Player], name: str) -> Player:
    for player in players:
        if player.name == name:
            return player
    return None

def get_stat(player: Player, category: str) -> int:
    if category == "Passing Yards":
        return player.passing_yards
    elif category == "Passing Touchdowns":
        return player.passing_touchdowns
    elif category == "Interceptions":
        return player.interceptions
    elif category == "Games":
        return player.games
    return 0

def find_leader(players: list[Player], category: str) -> Player:
    leader = players[0]

    for player in players:
        if category == "Interceptions":
            if get_stat(player, category) < get_stat(leader, category):
                leader = player
        else:
            if get_stat(player, category) > get_stat(leader, category):
                leader = player

    return leader

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("NFL Quarterback Comparison"),
        "Welcome to the NFL Player Comparison Tool!",
        "Compare quarterbacks based on their statistics.",
        "Comparisons made: " + str(state.comparisons),
        Button("Compare Players", "compare_players"),
        Button("View All Players", "players_page"),
        Button("View Leaderboard", "leaderboard_page"),
    ])
    

@route
def compare_players(state: State) -> Page:
    names = []

    for player in state.players:
        names.append(player.name)

    return Page(state, [
        Header("Choose Your Quarterbacks"),
        "Select two quarterbacks to compare.",

        "First Quarterback:",
        SelectBox("player1", names),

        "Second Quarterback:",
        SelectBox("player2", names),

        "Choose a Category:",
        SelectBox("category", [
            "Passing Yards",
            "Passing Touchdowns",
            "Interceptions",
            "Games"
        ]),

        Button("Compare", "results_page"),
        Button("Back to Home", "index")
    ])
@route
def players_page(state: State) -> Page:
    content = []
    
    for player in state.players:
        content.append(Header(player.name, 3))
        content.append("Passing Yards: " + str(player.passing_yards))
        content.append("Passing Touchdowns: " + str(player.passing_touchdowns))
        content.append("Interceptions: " + str(player.interceptions))
        content.append("Games Played: " + str(player.games))
            
    return Page(state, [
        Header("All Quarterbacks"),
        Div(*content),
        Button("Add Player", "add_player_page"),
        Button("Home", "index")
        ])

@route
def results_page(state: State, player1: str,
                 player2: str, category: str) -> Page:

    state.player1 = player1
    state.player2 = player2
    state.category = category

    first = find_player(state.players, player1)
    second = find_player(state.players, player2)

    if first is None or second is None:
        return Page(state, [
            Header("Player Not Found"),
            Button("Try Again", "compare_players")
        ])

    first_stat = get_stat(first, category)
    second_stat = get_stat(second, category)
    
    if first_stat == second_stat:
        winner = "It's a tie!"
    elif category == "Interceptions":
        if first_stat < second_stat:
            winner = first.name
        else:
            winner = second.name
    else:
        if first_stat > second_stat:
            winner = first.name
        else:
            winner = second.name

    state.comparisons += 1

    return Page(state, [
        Header("Comparison Results"),
        Header(category, 2),
    
        first.name + ": " + str(first_stat),
        second.name + ": " + str(second_stat),

        Header("Winner: " + winner, 2),

        Button("Compare Again", "compare_players"),
        Button("Home", "index")
    ])

@route
def add_player_page(state: State) -> Page:
    return Page(state, [
        Header("Add a Quarterback"),

        "Quarterback Name:",
        TextBox("name"),

        "Passing Yards:",
        TextBox("passing_yards"),

        "   Passing Touchdowns:",
        TextBox("passing_touchdowns"),

        "   Interceptions:",
        TextBox("interceptions"),

        "   Games Played:",
        TextBox("games"),

        Button("Save Player", "save_player"),
        Button("Back", "players_page")
    ])

@route
def save_player(state: State, name: str, passing_yards: int,
                passing_touchdowns: int, interceptions: int,
                games: int) -> Page:
    
    new_player = Player(name, passing_yards, passing_touchdowns,
                        interceptions, games)
    
    state.players.append(new_player)
    
    return players_page(state)

@route
def leaderboard_page(state: State) -> Page:
    return Page(state, [
        Header("NFL Quarterback Leaderboard"),

        "Choose a category:",
        SelectBox("category", [
            "Passing Yards",
            "Passing Touchdowns",
            "Interceptions",
            "Games"
        ]),

        Button("Find Leader", "show_leader"),
        Button("Home", "index")
    ])

@route
def show_leader(state: State, category: str) -> Page:
    leader = find_leader(state.players, category)

    if category == "Interceptions":
        heading = "Fewest Interceptions"
    else:
        heading = "Most " + category

    return Page(state, [
        Header("NFL Quarterback Leaderboard"),
        Header(heading, 2),

        "Quarterback: " + leader.name,
        category + ": " + str(get_stat(leader, category)),

        Button("Choose Another Category", "leaderboard_page"),
        Button("Home", "index")
    ])


start_server(State(players, "", "", "", 0))
