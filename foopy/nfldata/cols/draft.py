class Season:
    """
    4 digit number indicating to which season the game belongs to.
    """

    header = "season"


class RushTds:
    """
    Career rushing touchdowns
    """

    header = "rush_tds"


class PassYards:
    """
    Number of yards gained on pass plays
    """

    header = "pass_yards"


class Probowls:
    """
    Number of Pro Bowls
    """

    header = "probowls"


class PassAttempts:
    """
    Career pass attempts
    """

    header = "pass_attempts"


class RecTds:
    """
    Career receiving touchdowns
    """

    header = "rec_tds"


class RecYards:
    """
    Career receiving yards
    """

    header = "rec_yards"


class College:
    """
    Official college (usually the last one attended)
    """

    header = "college"


class DefSacks:
    """
    Career sacks
    """

    header = "def_sacks"


class Games:
    """
    Games played in career
    """

    header = "games"


class To:
    """
    Final season played in NFL
    """

    header = "to"


class CfbPlayerId:
    """
    ID from College Football Reference
    """

    header = "cfb_player_id"


class PfrPlayerName:
    """
    Player’s name as recorded by PFR
    """

    header = "pfr_player_name"


class DefSoloTackles:
    """
    Career solo tackles
    """

    header = "def_solo_tackles"


class DefInts:
    """
    Career interceptions
    """

    header = "def_ints"


class RushAtts:
    """
    Career rushing attempts
    """

    header = "rush_atts"


class PassCompletions:
    """
    Career pass completions
    """

    header = "pass_completions"


class RushYards:
    """
    The number of rushing yards gained
    """

    header = "rush_yards"


class DrAv:
    """
    Draft Approximate Value
    """

    header = "dr_av"


class Side:
    """
    O for offense, D for defense, S for special teams
    """

    header = "side"


class GsisId:
    """
    Game Stats and Info Service ID: the primary ID for play-by-play data.
    """

    header = "gsis_id"


class WAv:
    """
    Weighted Approximate Value
    """

    header = "w_av"


class CarAv:
    """
    Career Approximate Value
    """

    header = "car_av"


class PassTds:
    """
    Career pass touchdowns thrown
    """

    header = "pass_tds"


class Allpro:
    """
    Number of AP First Team All-Pro selections as recorded by PFR
    """

    header = "allpro"


class PassInts:
    """
    Career pass interceptions thrown
    """

    header = "pass_ints"


class Receptions:
    """
    The number of receptions for the receiver
    """

    header = "receptions"


class Category:
    """
    Broader category of player positions
    """

    header = "category"


class Age:
    """
    Age as of last pipeline build, rounded to one decimal. Pipeline is built on a weekly basis.
    """

    header = "age"


class Position:
    """
    Primary position as reported by NFL.com
    """

    header = "position"


class Team:
    """
    NFL team. Uses official abbreviations as per NFL.com
    """

    header = "team"


class Hof:
    """
    Whether player has been selected to the Pro Football Hall of Fame
    """

    header = "hof"


class Round:
    """
    Draft round
    """

    header = "round"


class Pick:
    """
    Draft overall pick
    """

    header = "pick"


class PfrPlayerId:
    """
    ID from Pro Football Reference
    """

    header = "pfr_player_id"


class SeasonsStarted:
    """
    Number of seasons recorded as primary starter for position
    """

    header = "seasons_started"


class DraftId:
    """
    FooPy created draft ID. Not guaranteed to be unique.
    """

    header = "draft_id"
