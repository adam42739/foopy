class Surface:
    """
    What type of ground the game was played on. (Source: Pro-Football-Reference)
    """

    header = "surface"


class Ftn:
    """
    No description available.
    """

    header = "ftn"


class TotalLine:
    """
    The closing total line for the game. (Source: Pro-Football-Reference)
    """

    header = "total_line"


class AwayTeam:
    """
    String abbreviation for the away team.
    """

    header = "away_team"


class AwayQbId:
    """
    GSIS Player ID for away team starting quarterback.
    """

    header = "away_qb_id"


class Referee:
    """
    Name of the game's referee (head official)
    """

    header = "referee"


class Wind:
    """
    The speed of the wind in miles/hour only for 'roof' = 'outdoors' or 'open'. (Source: Pro-Football-Reference)
    """

    header = "wind"


class Roof:
    """
    One of 'dome', 'outdoors', 'closed', 'open' indicating indicating the roof status of the stadium the game was played in. (Source: Pro-Football-Reference)
    """

    header = "roof"


class HomeRest:
    """
    Days of rest that the home team is coming off of.
    """

    header = "home_rest"


class GameType:
    """
    What type of game? One of REG, WC, DIV, CON, SB
    """

    header = "game_type"


class StadiumId:
    """
    ID of the stadium the game was played in. (Source: Pro-Football-Reference)
    """

    header = "stadium_id"


class AwayRest:
    """
    Days of rest that the away team is coming off of.
    """

    header = "away_rest"


class HomeQbName:
    """
    Name of home team starting QB.
    """

    header = "home_qb_name"


class Weekday:
    """
    The day of the week on which the game occcured.
    """

    header = "weekday"


class AwayMoneyline:
    """
    Odds for away team to win the game.
    """

    header = "away_moneyline"


class OverOdds:
    """
    Odds that total score of game would be over the total_ine.
    """

    header = "over_odds"


class HomeTeam:
    """
    String abbreviation for the home team.
    """

    header = "home_team"


class HomeMoneyline:
    """
    Odds for home team to win the game.
    """

    header = "home_moneyline"


class Week:
    """
    Season week.
    """

    header = "week"


class UnderOdds:
    """
    Odds that total score of game would be under the total_line.
    """

    header = "under_odds"


class HomeCoach:
    """
    First and last name of the home team coach. (Source: Pro-Football-Reference)
    """

    header = "home_coach"


class NflDetailId:
    """
    The id of the game issued by NFL Detail.
    """

    header = "nfl_detail_id"


class AwayCoach:
    """
    First and last name of the away team coach. (Source: Pro-Football-Reference)
    """

    header = "away_coach"


class Temp:
    """
    The temperature at the stadium only for 'roof' = 'outdoors' or 'open'.(Source: Pro-Football-Reference)
    """

    header = "temp"


class AwaySpreadOdds:
    """
    Odds for away team to cover the spread.
    """

    header = "away_spread_odds"


class HomeSpreadOdds:
    """
    Odds for home team to cover the spread.
    """

    header = "home_spread_odds"


class HomeScore:
    """
    Total points scored by the home team.
    """

    header = "home_score"


class Location:
    """
    Either 'Home' o 'Neutral' indicating if the home team played at home or at a neutral site.
    """

    header = "location"


class Gameday:
    """
    The date on which the game occurred.
    """

    header = "gameday"


class Total:
    """
    Equals home_score + away_score and means the total points scored in the given game.
    """

    header = "total"


class Pff:
    """
    The id of the game issued by [Pro Football Focus](https://www.pff.com/)
    """

    header = "pff"


class DivGame:
    """
    Binary indicator for if the given game was a division game.
    """

    header = "div_game"


class Gametime:
    """
    The kickoff time of the game. This is represented in 24-hour time and the Eastern time zone, regardless of what time zone the game was being played in.
    """

    header = "gametime"


class Stadium:
    """
    Game site name.
    """

    header = "stadium"


class Result:
    """
    Equals home_score - away_score and means the game outcome from the perspective of the home team.
    """

    header = "result"


class Overtime:
    """
    Binary indicator of whether or not game went to overtime.
    """

    header = "overtime"


class Gsis:
    """
    The id of the game issued by the NFL Game Statistics &amp; Information System.
    """

    header = "gsis"


class AwayScore:
    """
    Total points scored by the away team.
    """

    header = "away_score"


class OldGameId:
    """
    Legacy NFL game ID.
    """

    header = "old_game_id"


class AwayQbName:
    """
    Name of away team starting QB.
    """

    header = "away_qb_name"


class Pfr:
    """
    The id of the game issued by [Pro-Football-Reference](https://www.pro-football-reference.com/)
    """

    header = "pfr"


class SpreadLine:
    """
    The closing spread line for the game. A positive number means the home team was favored by that many points, a negative number means the away team was favored by that many points. (Source: Pro-Football-Reference)
    """

    header = "spread_line"


class HomeQbId:
    """
    GSIS Player ID for home team starting quarterback.
    """

    header = "home_qb_id"


class GameId:
    """
    Ten digit identifier for NFL game.
    """

    header = "game_id"


class Espn:
    """
    The id of the game issued by [ESPN](https://www.espn.com/)
    """

    header = "espn"


class Season:
    """
    4 digit number indicating to which season the game belongs to.
    """

    header = "season"
