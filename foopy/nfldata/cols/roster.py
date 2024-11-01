class DraftId:
    """
    FooPy created draft ID. Not guaranteed to be unique.
    """

    header = "draft_id"


class PlayerId:
    """
    ID of the player. Use this to join to other sources.
    """

    header = "player_id"


class Weight:
    """
    Official weight, in pounds
    """

    header = "weight"


class EspnId:
    """
    Player ID for ESPN API
    """

    header = "espn_id"


class SleeperId:
    """
    Player ID for Sleeper API
    """

    header = "sleeper_id"


class Height:
    """
    Official height, in inches
    """

    header = "height"


class StatusDescriptionAbbr:
    """
    No description available.
    """

    header = "status_description_abbr"


class EntryYear:
    """
    No description available.
    """

    header = "entry_year"


class FirstName:
    """
    First name as per NFL.com
    """

    header = "first_name"


class DraftNumber:
    """
    No description available.
    """

    header = "draft_number"


class GameType:
    """
    What type of game? One of REG, WC, DIV, CON, SB
    """

    header = "game_type"


class PffId:
    """
    Player ID for Pro Football Focus
    """

    header = "pff_id"


class GsisItId:
    """
    No description available.
    """

    header = "gsis_it_id"


class Position:
    """
    Primary position as reported by NFL.com
    """

    header = "position"


class PlayerName:
    """
    Name of the player
    """

    header = "player_name"


class FantasyDataId:
    """
    Player ID for FantasyData
    """

    header = "fantasy_data_id"


class NgsPosition:
    """
    No description available.
    """

    header = "ngs_position"


class DepthChartPosition:
    """
    Position assigned on depth chart. Not always accurate!
    """

    header = "depth_chart_position"


class Team:
    """
    NFL team. Uses official abbreviations as per NFL.com
    """

    header = "team"


class FootballName:
    """
    No description available.
    """

    header = "football_name"


class JerseyNumber:
    """
    Jersey number of the player listed in the 'name' column.
    """

    header = "jersey_number"


class RookieYear:
    """
    No description available.
    """

    header = "rookie_year"


class DraftClub:
    """
    No description available.
    """

    header = "draft_club"


class College:
    """
    Official college (usually the last one attended)
    """

    header = "college"


class Status:
    """
    Roster status: describes things like Active, Inactive, Injured Reserve, Practice Squad etc
    """

    header = "status"


class YearsExp:
    """
    Years played in league
    """

    header = "years_exp"


class BirthDate:
    """
    Birthdate, as recorded by Sleeper API
    """

    header = "birth_date"


class Week:
    """
    Season week.
    """

    header = "week"


class RotowireId:
    """
    Player ID for Rotowire
    """

    header = "rotowire_id"


class HeadshotUrl:
    """
    A URL string that points to player photos used by NFL.com (or sometimes ESPN)
    """

    header = "headshot_url"


class PfrId:
    """
    Player ID for Pro Football Reference
    """

    header = "pfr_id"


class SportradarId:
    """
    Player ID for Sportradar API
    """

    header = "sportradar_id"


class LastName:
    """
    Last name as per NFL.com
    """

    header = "last_name"


class YahooId:
    """
    Player ID for Yahoo API
    """

    header = "yahoo_id"


class SmartId:
    """
    No description available.
    """

    header = "smart_id"


class Age:
    """
    Age as of last pipeline build, rounded to one decimal. Pipeline is built on a weekly basis.
    """

    header = "age"


class EsbId:
    """
    No description available.
    """

    header = "esb_id"


class Season:
    """
    4 digit number indicating to which season the game belongs to.
    """

    header = "season"
