from dataclasses import dataclass


@dataclass
class Player:
    name: str
    passing_yards: int
    passing_touchdowns: int
    interceptions: int
    games: int


# 2025 NFL regular season. One representative late-season QB per team.
# Some teams used additional starters or changed QBs late in the year.
# Sources: https://www.nfl.com/stats/player-stats/category/passing-yards/2025/REG/all/passingyards/desc
#          https://www.fftoday.com/stats/playerstats.php?PosID=10&Season=2025
players = [
    Player("Josh Allen", 3668, 25, 10, 17),  # Buffalo Bills
    Player("Quinn Ewers", 622, 3, 3, 4),  # Miami Dolphins
    Player("Drake Maye", 4394, 31, 8, 17),  # New England Patriots
    Player("Brady Cook", 739, 2, 7, 5),  # New York Jets
    Player("Lamar Jackson", 2549, 21, 7, 13),  # Baltimore Ravens
    Player("Joe Burrow", 1809, 17, 5, 8),  # Cincinnati Bengals
    Player("Shedeur Sanders", 1400, 7, 10, 8),  # Cleveland Browns
    Player("Aaron Rodgers", 3322, 24, 7, 16),  # Pittsburgh Steelers
    Player("C.J. Stroud", 3041, 19, 8, 14),  # Houston Texans
    Player("Philip Rivers", 544, 4, 3, 3),  # Indianapolis Colts
    Player("Trevor Lawrence", 4007, 29, 12, 17),  # Jacksonville Jaguars
    Player("Cam Ward", 3169, 15, 7, 17),  # Tennessee Titans
    Player("Bo Nix", 3931, 25, 11, 17),  # Denver Broncos
    Player("Chris Oladokun", 235, 1, 0, 3),  # Kansas City Chiefs
    Player("Geno Smith", 3025, 19, 17, 15),  # Las Vegas Raiders
    Player("Justin Herbert", 3727, 26, 13, 16),  # Los Angeles Chargers
    Player("Dak Prescott", 4552, 30, 10, 17),  # Dallas Cowboys
    Player("Jaxson Dart", 2272, 15, 5, 14),  # New York Giants
    Player("Jalen Hurts", 3224, 25, 6, 16),  # Philadelphia Eagles
    Player("Marcus Mariota", 1695, 10, 7, 11),  # Washington Commanders
    Player("Caleb Williams", 3942, 27, 7, 17),  # Chicago Bears
    Player("Jared Goff", 4564, 34, 8, 17),  # Detroit Lions
    Player("Jordan Love", 3381, 23, 6, 15),  # Green Bay Packers
    Player("J.J. McCarthy", 1632, 11, 12, 10),  # Minnesota Vikings
    Player("Kirk Cousins", 1721, 10, 5, 10),  # Atlanta Falcons
    Player("Bryce Young", 3011, 23, 11, 16),  # Carolina Panthers
    Player("Tyler Shough", 2384, 10, 6, 11),  # New Orleans Saints
    Player("Baker Mayfield", 3693, 26, 11, 17),  # Tampa Bay Buccaneers
    Player("Jacoby Brissett", 3366, 23, 8, 14),  # Arizona Cardinals
    Player("Matthew Stafford", 4707, 46, 8, 17),  # Los Angeles Rams
    Player("Brock Purdy", 2167, 20, 10, 9),  # San Francisco 49ers
    Player("Sam Darnold", 4048, 25, 14, 17),  # Seattle Seahawks
]
