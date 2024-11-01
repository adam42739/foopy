class Name:
    """
    Name of the 'passer' if it is not 'NA', or name of the 'rusher' otherwise.
    """

    header = "name"


class FleaflickerId:
    """
    Fleaflicker ID - usual format is an integer with ~4 digits. Fleaflicker API also has sportradar and that’s generally preferred.
    """

    header = "fleaflicker_id"


class College:
    """
    Official college (usually the last one attended)
    """

    header = "college"


class EspnId:
    """
    Player ID for ESPN API
    """

    header = "espn_id"


class FantasyDataId:
    """
    Player ID for FantasyData
    """

    header = "fantasy_data_id"


class DraftRound:
    """
    Round of draft.
    """

    header = "draft_round"


class YahooId:
    """
    Player ID for Yahoo API
    """

    header = "yahoo_id"


class DraftPick:
    """
    Draft pick within round, i.e. 32nd pick of second round.
    """

    header = "draft_pick"


class DraftYear:
    """
    Year of draft. Zero if unknown/undrafted.
    """

    header = "draft_year"


class RotowireId:
    """
    Player ID for Rotowire
    """

    header = "rotowire_id"


class PffId:
    """
    Player ID for Pro Football Focus
    """

    header = "pff_id"


class Weight:
    """
    Official weight, in pounds
    """

    header = "weight"


class SleeperId:
    """
    Player ID for Sleeper API
    """

    header = "sleeper_id"


class StatsGlobalId:
    """
    Stats Global ID - usual format is a six digit integer
    """

    header = "stats_global_id"


class MergeName:
    """
    Name but formatted for name joins via ffscrapr::dp_cleannames() - coerced to lowercase, stripped of punctuation and suffixes, and common substitutions performed.
    """

    header = "merge_name"


class RotoworldId:
    """
    Rotoworld ID - usual format is an integer with ~four digits. Not to be confused with rotowire_id.
    """

    header = "rotoworld_id"


class MflId:
    """
    MyFantasyLeague.com ID - this is the primary key for this table and is unique and complete. Usually an integer of 5 digits.
    """

    header = "mfl_id"


class GsisId:
    """
    Game Stats and Info Service ID: the primary ID for play-by-play data.
    """

    header = "gsis_id"


class KtcId:
    """
    KeepTradeCut ID - usual format is an integer with ~four digits.
    """

    header = "ktc_id"


class FantasyprosId:
    """
    FantasyPros.com ID - usually an integer of 5 digits.
    """

    header = "fantasypros_id"


class NflId:
    """
    NFL.com ID - usual format fullname/integers
    """

    header = "nfl_id"


class CbsId:
    """
    CBS ID - usual format is an integer with ~ 7 digits.
    """

    header = "cbs_id"


class PfrId:
    """
    Player ID for Pro Football Reference
    """

    header = "pfr_id"


class SwishId:
    """
    Player ID for Swish Analytics
    """

    header = "swish_id"


class TwitterUsername:
    """
    Official twitter handle, if known
    """

    header = "twitter_username"


class DbSeason:
    """
    Year of database build. Previous years may also be available via dynastyprocess.
    """

    header = "db_season"


class SportradarId:
    """
    Player ID for Sportradar API
    """

    header = "sportradar_id"


class Height:
    """
    Official height, in inches
    """

    header = "height"


class Birthdate:
    """
    Birthdate
    """

    header = "birthdate"


class DraftOvr:
    """
    Overall draft pick selection. This can be a little bit patchy, since MFL does not report this number.
    """

    header = "draft_ovr"


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


class StatsId:
    """
    Stats ID - usual format is five digit integer
    """

    header = "stats_id"


class CfbrefId:
    """
    College Football Reference ID - usual format is firstname-lastname-integer
    """

    header = "cfbref_id"
