class TotalAwayRushEpa:
    """
    Cumulative total rushing EPA for the away team in the game so far.
    """

    header = "total_away_rush_epa"


class Time:
    """
    Time at start of play provided in string format as minutes:seconds remaining in the quarter.
    """

    header = "time"


class PassAttempt:
    """
    Binary indicator for if the play was a pass attempt (includes sacks).
    """

    header = "pass_attempt"


class ScoreDifferentialPost:
    """
    Score differential between the posteam and defteam at the end of the play.
    """

    header = "score_differential_post"


class Week:
    """
    Season week.
    """

    header = "week"


class PosteamScore:
    """
    Score the posteam at the start of the play.
    """

    header = "posteam_score"


class SoloTackle2Team:
    """
    Team of one of the players with a solo tackle.
    """

    header = "solo_tackle_2_team"


class TackleWithAssist2Team:
    """
    Team of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_2_team"


class StadiumId:
    """
    ID of the stadium the game was played in. (Source: Pro-Football-Reference)
    """

    header = "stadium_id"


class NumberOfPassRushers:
    """
    Number of defensive player who rushed the passer.
    """

    header = "number_of_pass_rushers"


class SeasonType:
    """
    'REG' or 'POST' indicating if the game belongs to regular or post season.
    """

    header = "season_type"


class FumbleRecovery2PlayerName:
    """
    String name of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_2_player_name"


class DriveInside20:
    """
    Binary indicator if the offense was able to get inside the opponents 20 yard line.
    """

    header = "drive_inside20"


class FumbleRecovery1PlayerName:
    """
    String name of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_1_player_name"


class RushTouchdown:
    """
    Binary indicator for if the play resulted in a rushing TD.
    """

    header = "rush_touchdown"


class Route:
    """
    No description available.
    """

    header = "route"


class LateralReceiverPlayerName:
    """
    String name for the player that received the last(!) lateral on a pass play. If there were multiple laterals in the same play, this will only be the last player who received a lateral. Please see &lt;https://github.com/mrcaseb/nfl-data/tree/master/data/lateral_yards&gt; for a list of plays where multiple players recorded lateral receiving yards.
    """

    header = "lateral_receiver_player_name"


class IncompletePass:
    """
    Binary indicator for if the pass was incomplete.
    """

    header = "incomplete_pass"


class SoloTackle:
    """
    Binary indicator if the play had a solo tackle (could be multiple due to fumbles).
    """

    header = "solo_tackle"


class QuarterEnd:
    """
    Binary indicator for whether or not the row of the data is marking the end of a quarter.
    """

    header = "quarter_end"


class RushAttempt:
    """
    Binary indicator for if the play was a run.
    """

    header = "rush_attempt"


class TotalAwayRawYacEpa:
    """
    Cumulative total raw yac EPA for the away team in the game so far.
    """

    header = "total_away_raw_yac_epa"


class SafetyPlayerName:
    """
    String name for the player who scored a safety.
    """

    header = "safety_player_name"


class TackleWithAssist:
    """
    Binary indicator for if there has been a tackle with assist.
    """

    header = "tackle_with_assist"


class TotalHomeEpa:
    """
    Cumulative total EPA for the home team in the game so far.
    """

    header = "total_home_epa"


class LateralReceivingYards:
    """
    Numeric yards by the `lateral_receiver_player_name` in pass plays with laterals. Please see the description of `lateral_receiver_player_name` for further information.
    """

    header = "lateral_receiving_yards"


class FumbleLost:
    """
    Binary indicator for if the fumble was lost.
    """

    header = "fumble_lost"


class TotalAwayPassWpa:
    """
    Cumulative total passing WPA for the away team in the game so far.
    """

    header = "total_away_pass_wpa"


class DriveGameClockStart:
    """
    Game time at the beginning of a given drive.
    """

    header = "drive_game_clock_start"


class SafetyProb:
    """
    Predicted probability of the posteam scoring a safety next.
    """

    header = "safety_prob"


class SpecialTeamsPlay:
    """
    Binary indicator for whether play is special teams play from NFL source. Available 2011 and beyond with source "nfl".
    """

    header = "special_teams_play"


class DefensiveExtraPointConv:
    """
    Binary indicator whether or not the defense successfully scored on an extra point attempt.
    """

    header = "defensive_extra_point_conv"


class OffenseFormation:
    """
    Formation the offense lines up in to snap the ball.
    """

    header = "offense_formation"


class Yardline100:
    """
    Numeric distance in the number of yards from the opponent's endzone for the posteam.
    """

    header = "yardline_100"


class PassDefense1PlayerId:
    """
    Unique identifier of one of the players with a pass defense.
    """

    header = "pass_defense_1_player_id"


class Ydsnet:
    """
    Numeric value for total yards gained on the given drive.
    """

    header = "ydsnet"


class TimeoutTeam:
    """
    String abbreviation for which team called the timeout.
    """

    header = "timeout_team"


class FgProb:
    """
    Predicted probability of the posteam scoring a FG next.
    """

    header = "fg_prob"


class AssistTackle1PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.
    """

    header = "assist_tackle_1_player_id"


class NgsAirYards:
    """
    Distance (in yards) that the ball traveled in the air on a given passing play as tracked by NGS
    """

    header = "ngs_air_yards"


class ForcedFumblePlayer2PlayerId:
    """
    Unique identifier of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_2_player_id"


class QbHit1PlayerName:
    """
    String name for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.
    """

    header = "qb_hit_1_player_name"


class OppFgProb:
    """
    Predicted probability of the defteam scoring a FG next.
    """

    header = "opp_fg_prob"


class TackleForLoss1PlayerName:
    """
    String name for one of the potential players with the tackle for loss.
    """

    header = "tackle_for_loss_1_player_name"


class XyacFd:
    """
    Probability play earns a first down based on where the ball was caught.
    """

    header = "xyac_fd"


class PosteamType:
    """
    String indicating whether the posteam team is home or away.
    """

    header = "posteam_type"


class Cp:
    """
    Numeric value indicating the probability for a complete pass based on comparable game situations.
    """

    header = "cp"


class DriveQuarterEnd:
    """
    Numeric value indicating in which quarter the given drive has ended.
    """

    header = "drive_quarter_end"


class LateralKickoffReturnerPlayerId:
    """
    Unique identifier for the player that received the lateral on a kickoff return.
    """

    header = "lateral_kickoff_returner_player_id"


class CompYacWpa:
    """
    The yac_wpa for completions only.
    """

    header = "comp_yac_wpa"


class TimeOfDay:
    """
    Time of day of play in UTC "HH:MM:SS" format. Available 2011 and beyond with source "nfl".
    """

    header = "time_of_day"


class OppTdProb:
    """
    Predicted probability of the defteam scoring a TD next.
    """

    header = "opp_td_prob"


class RushingYards:
    """
    Numeric yards by the rusher_player_name, excluding yards gained in rush plays with laterals. This should equal official rushing statistics but could miss yards gained in rush plays with laterals. Please see the description of `lateral_rusher_player_name` for further information.
    """

    header = "rushing_yards"


class PuntFairCatch:
    """
    Binary indicator for if the punt was caught with a fair catch.
    """

    header = "punt_fair_catch"


class TotalAwayRawAirEpa:
    """
    Cumulative total raw air EPA for the away team in the game so far.
    """

    header = "total_away_raw_air_epa"


class TotalHomeRushWpa:
    """
    Cumulative total rushing WPA for the home team in the game so far.
    """

    header = "total_home_rush_wpa"


class DriveEndTransition:
    """
    String indicating how the offense lost the ball.
    """

    header = "drive_end_transition"


class AwayTimeoutsRemaining:
    """
    Numeric timeouts remaining in the half for the away team.
    """

    header = "away_timeouts_remaining"


class Receiver:
    """
    Name of the receiver including plays with penalties.
    """

    header = "receiver"


class YacWpa:
    """
    WPA from yards after the catch (same logic as yac_epa).
    """

    header = "yac_wpa"


class Sp:
    """
    Binary indicator for whether or not a score occurred on the play.
    """

    header = "sp"


class DefensiveExtraPointAttempt:
    """
    Binary indicator whether or not the defense was able to have an attempt on an extra point attempt, this results following a blocked attempt that the defense recovers the ball.
    """

    header = "defensive_extra_point_attempt"


class NflApiId:
    """
    UUID of the game in the new NFL API.
    """

    header = "nfl_api_id"


class PunterPlayerId:
    """
    Unique identifier for the punter.
    """

    header = "punter_player_id"


class Wp:
    """
    Estimated win probabiity for the posteam given the current situation at the start of the given play.
    """

    header = "wp"


class BlockedPlayerId:
    """
    Unique identifier for the player that blocked the punt or FG.
    """

    header = "blocked_player_id"


class SackPlayerName:
    """
    String name of the player who recorded a solo sack.
    """

    header = "sack_player_name"


class TdProb:
    """
    Predicted probability of the posteam scoring a TD next.
    """

    header = "td_prob"


class PlayersOnPlay:
    """
    A list of every player on the field for the play, by gsis_it_id
    """

    header = "players_on_play"


class PlayTypeNfl:
    """
    Play type as listed in the NFL source. Slightly different to the regular play_type variable.
    """

    header = "play_type_nfl"


class Ydstogo:
    """
    Numeric yards in distance from either the first down marker or the endzone in goal down situations.
    """

    header = "ydstogo"


class PassDefense1PlayerName:
    """
    String name of one of the players with a pass defense.
    """

    header = "pass_defense_1_player_name"


class CompAirWpa:
    """
    The air_wpa for completions only.
    """

    header = "comp_air_wpa"


class InterceptionPlayerId:
    """
    Unique identifier for the player that intercepted the pass.
    """

    header = "interception_player_id"


class AssistTackle2PlayerName:
    """
    String name of one of the players with a tackle assist.
    """

    header = "assist_tackle_2_player_name"


class HomeTeam:
    """
    String abbreviation for the home team.
    """

    header = "home_team"


class Desc:
    """
    Detailed string description for the given play.
    """

    header = "desc"


class FirstDown:
    """
    Binary indicator if the play ended in a first down.
    """

    header = "first_down"


class NOffense:
    """
    Number of offensive players on the field for the play
    """

    header = "n_offense"


class AirEpa:
    """
    EPA from the air yards alone. For completions this represents the actual value provided through the air. For incompletions this represents the hypothetical value that could've been added through the air if the pass was completed.
    """

    header = "air_epa"


class RusherId:
    """
    ID of the player in the 'rusher' column.
    """

    header = "rusher_id"


class TotalHomeRushEpa:
    """
    Cumulative total rushing EPA for the home team in the game so far.
    """

    header = "total_home_rush_epa"


class TackleWithAssist1PlayerName:
    """
    String name of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_1_player_name"


class Sack:
    """
    Binary indicator for if the play ended in a sack.
    """

    header = "sack"


class KickerPlayerName:
    """
    String name for the kicker on FG or kickoff.
    """

    header = "kicker_player_name"


class HalfSack1PlayerId:
    """
    Unique identifier of the first player who recorded half a sack.
    """

    header = "half_sack_1_player_id"


class SpreadLine:
    """
    The closing spread line for the game. A positive number means the home team was favored by that many points, a negative number means the away team was favored by that many points. (Source: Pro-Football-Reference)
    """

    header = "spread_line"


class PuntBlocked:
    """
    Binary indicator for if the punt was blocked.
    """

    header = "punt_blocked"


class DefensiveTwoPointConv:
    """
    Binary indicator whether or not the defense successfully scored on the two point conversion.
    """

    header = "defensive_two_point_conv"


class PenaltyPlayerId:
    """
    Unique identifier for the player with the penalty.
    """

    header = "penalty_player_id"


class AirYards:
    """
    Numeric value for distance in yards perpendicular to the line of scrimmage at where the targeted receiver either caught or didn't catch the ball.
    """

    header = "air_yards"


class Fumbled2PlayerName:
    """
    String name of one of the second player who fumbled on the play.
    """

    header = "fumbled_2_player_name"


class Roof:
    """
    One of 'dome', 'outdoors', 'closed', 'open' indicating indicating the roof status of the stadium the game was played in. (Source: Pro-Football-Reference)
    """

    header = "roof"


class Defteam:
    """
    String abbreviation for the team on defense.
    """

    header = "defteam"


class LateralSackPlayerName:
    """
    String name for the player that received the lateral on a sack.
    """

    header = "lateral_sack_player_name"


class ExtraPointAttempt:
    """
    Binary indicator for extra point attempt.
    """

    header = "extra_point_attempt"


class DriveStartYardLine:
    """
    String indicating where a given drive started consisting of team half and yard line number.
    """

    header = "drive_start_yard_line"


class PuntDowned:
    """
    Binary indicator for if the punt was downed.
    """

    header = "punt_downed"


class AssistTackle3Team:
    """
    Team of one of the players with a tackle assist.
    """

    header = "assist_tackle_3_team"


class Fumbled1Team:
    """
    Team of one of the first player with a fumble.
    """

    header = "fumbled_1_team"


class QbHit1PlayerId:
    """
    Unique identifier for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.
    """

    header = "qb_hit_1_player_id"


class DefteamScorePost:
    """
    Score for the defteam at the end of the play.
    """

    header = "defteam_score_post"


class QbSpike:
    """
    Binary indicator for whether or not the QB spiked the ball.
    """

    header = "qb_spike"


class PassTouchdown:
    """
    Binary indicator for if the play resulted in a passing TD.
    """

    header = "pass_touchdown"


class ReturnTouchdown:
    """
    Binary indicator for if the play resulted in a return TD. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.
    """

    header = "return_touchdown"


class HalfSack1PlayerName:
    """
    String name of the first player who recorded half a sack.
    """

    header = "half_sack_1_player_name"


class TotalAwayEpa:
    """
    Cumulative total EPA for the away team in the game so far.
    """

    header = "total_away_epa"


class KickoffFairCatch:
    """
    Binary indicator for if the kickoff was caught with a fair catch.
    """

    header = "kickoff_fair_catch"


class FumbleRecovery1Team:
    """
    Team of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_1_team"


class EndYardLine:
    """
    String indicating the yardline at the end of the given play consisting of team half and yard line number.
    """

    header = "end_yard_line"


class PlayId:
    """
    Numeric play id that when used with game_id and drive provides the unique identifier for a single play.
    """

    header = "play_id"


class KickoffReturnerPlayerId:
    """
    Unique identifier for the kickoff returner.
    """

    header = "kickoff_returner_player_id"


class HomeWpPost:
    """
    Estimated win probability for the home team at the end of the play.
    """

    header = "home_wp_post"


class TotalHomeRawYacWpa:
    """
    Cumulative total raw yac WPA for the home team in the game so far.
    """

    header = "total_home_raw_yac_wpa"


class DrivePlayCount:
    """
    Numeric value of how many regular plays happened in a given drive.
    """

    header = "drive_play_count"


class Passer:
    """
    Name of the dropback player (scrambles included) including plays with penalties.
    """

    header = "passer"


class DriveFirstDowns:
    """
    Number of forst downs in a given drive.
    """

    header = "drive_first_downs"


class DriveYardsPenalized:
    """
    Numeric value of how many yards the offense gained or lost through penalties in the given drive.
    """

    header = "drive_yards_penalized"


class TotalHomeRawAirEpa:
    """
    Cumulative total raw air EPA for the home team in the game so far.
    """

    header = "total_home_raw_air_epa"


class QbEpa:
    """
    Gives QB credit for EPA for up to the point where a receiver lost a fumble after a completed catch and makes EPA work more like passing yards on plays with fumbles.
    """

    header = "qb_epa"


class DriveEndedWithScore:
    """
    Binary indicator the drive ended with a score.
    """

    header = "drive_ended_with_score"


class DrivePlayIdStarted:
    """
    Play_id of the first play in the given drive.
    """

    header = "drive_play_id_started"


class DefensiveTwoPointAttempt:
    """
    Binary indicator whether or not the defense was able to have an attempt on a two point conversion, this results following a turnover.
    """

    header = "defensive_two_point_attempt"


class KickoffDowned:
    """
    Binary indicator for if the kickoff was downed.
    """

    header = "kickoff_downed"


class Rusher:
    """
    Name of the rusher (no scrambles) including plays with penalties.
    """

    header = "rusher"


class DriveRealStartTime:
    """
    Local day time when the drive started (currently not used by the NFL and therefore mostly 'NA').
    """

    header = "drive_real_start_time"


class HalfSack2PlayerName:
    """
    String name of the second player who recorded half a sack.
    """

    header = "half_sack_2_player_name"


class HomeCoach:
    """
    First and last name of the home team coach. (Source: Pro-Football-Reference)
    """

    header = "home_coach"


class Down:
    """
    The down for the given play.
    """

    header = "down"


class Season:
    """
    4 digit number indicating to which season the game belongs to.
    """

    header = "season"


class DriveQuarterStart:
    """
    Numeric value indicating in which quarter the given drive has started.
    """

    header = "drive_quarter_start"


class TdPlayerId:
    """
    Unique identifier of the player who scored a touchdown.
    """

    header = "td_player_id"


class Result:
    """
    Equals home_score - away_score and means the game outcome from the perspective of the home team.
    """

    header = "result"


class Name:
    """
    Name of the 'passer' if it is not 'NA', or name of the 'rusher' otherwise.
    """

    header = "name"


class QbKneel:
    """
    Binary indicator for whether or not the QB took a knee.
    """

    header = "qb_kneel"


class DefteamTimeoutsRemaining:
    """
    Number of timeouts remaining for the team on defense.
    """

    header = "defteam_timeouts_remaining"


class ReceiverId:
    """
    ID of the player in the 'receiver' column.
    """

    header = "receiver_id"


class Penalty:
    """
    Binary indicator for whether or not a penalty occurred.
    """

    header = "penalty"


class ReturnYards:
    """
    Yards gained by the return team. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.
    """

    header = "return_yards"


class TotalAwayCompAirEpa:
    """
    Cumulative total completions air EPA for the away team in the game so far.
    """

    header = "total_away_comp_air_epa"


class FieldGoalResult:
    """
    String indicator for result of field goal attempt: made, missed, or blocked.
    """

    header = "field_goal_result"


class TwoPointAttempt:
    """
    Binary indicator for two point conversion attempt.
    """

    header = "two_point_attempt"


class XyacMeanYardage:
    """
    Average expected yards after the catch based on where the ball was caught.
    """

    header = "xyac_mean_yardage"


class DriveTimeOfPossession:
    """
    Time of possession in a given drive.
    """

    header = "drive_time_of_possession"


class QbHit2PlayerName:
    """
    String name for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.
    """

    header = "qb_hit_2_player_name"


class Wind:
    """
    The speed of the wind in miles/hour only for 'roof' = 'outdoors' or 'open'. (Source: Pro-Football-Reference)
    """

    header = "wind"


class FumbleForced:
    """
    Binary indicator for if the fumble was forced.
    """

    header = "fumble_forced"


class YacEpa:
    """
    EPA from the yards after catch alone. For completions this represents the actual value provided after the catch. For incompletions this represents the difference between the hypothetical air_epa and the play's raw observed EPA (how much the incomplete pass cost the posteam).
    """

    header = "yac_epa"


class BlockedPlayerName:
    """
    String name for the player that blocked the punt or FG.
    """

    header = "blocked_player_name"


class Safety:
    """
    Binary indicator for whether or not a safety occurred.
    """

    header = "safety"


class FumbleRecovery2Yards:
    """
    Yards gained by one of the players with a fumble recovery.
    """

    header = "fumble_recovery_2_yards"


class TotalHomeRawAirWpa:
    """
    Cumulative total raw air WPA for the home team in the game so far.
    """

    header = "total_home_raw_air_wpa"


class SoloTackle2PlayerName:
    """
    String name of one of the players with a solo tackle.
    """

    header = "solo_tackle_2_player_name"


class TotalAwayCompYacWpa:
    """
    Cumulative total completions yac WPA for the away team in the game so far.
    """

    header = "total_away_comp_yac_wpa"


class DefensePersonnel:
    """
    Number of defensive linemen, linebackers, and defensive backs on the field for the play.
    """

    header = "defense_personnel"


class TackleWithAssist1Team:
    """
    Team of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_1_team"


class SideOfField:
    """
    String abbreviation for which team's side of the field the team with possession is currently on.
    """

    header = "side_of_field"


class PossessionTeam:
    """
    String abbreviation for the team with possession.
    """

    header = "possession_team"


class TdTeam:
    """
    String abbreviation for which team scored the touchdown.
    """

    header = "td_team"


class Qtr:
    """
    Quarter of the game (5 is overtime).
    """

    header = "qtr"


class GoalToGo:
    """
    Binary indicator for whether or not the posteam is in a goal down situation.
    """

    header = "goal_to_go"


class HomeScore:
    """
    Total points scored by the home team.
    """

    header = "home_score"


class ThirdDownFailed:
    """
    Binary indicator for if the posteam failed to convert first down on third down.
    """

    header = "third_down_failed"


class FixedDriveResult:
    """
    Manually created drive result.
    """

    header = "fixed_drive_result"


class FumbleRecovery2PlayerId:
    """
    Unique identifier of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_2_player_id"


class TotalHomeCompYacWpa:
    """
    Cumulative total completions yac WPA for the home team in the game so far.
    """

    header = "total_home_comp_yac_wpa"


class TimeToThrow:
    """
    Duration (in seconds) between the time of the ball being snapped and the time of release of a pass attempt
    """

    header = "time_to_throw"


class TotalHomeRawYacEpa:
    """
    Cumulative total raw yac EPA for the home team in the game so far.
    """

    header = "total_home_raw_yac_epa"


class LateralPuntReturnerPlayerName:
    """
    String name for the player that received the lateral on a punt return.
    """

    header = "lateral_punt_returner_player_name"


class Series:
    """
    Starts at 1, each new first down increments, numbers shared across both teams NA: kickoffs, extra point/two point conversion attempts, non-plays, no posteam
    """

    header = "series"


class Fumbled2Team:
    """
    Team of one of the second player with a fumble.
    """

    header = "fumbled_2_team"


class FourthDownConverted:
    """
    Binary indicator for if the first down was converted on fourth down.
    """

    header = "fourth_down_converted"


class InterceptionPlayerName:
    """
    String name for the player that intercepted the pass.
    """

    header = "interception_player_name"


class YardsGained:
    """
    Numeric yards gained (or lost) by the possessing team, excluding yards gained via fumble recoveries and laterals.
    """

    header = "yards_gained"


class ScoreDifferential:
    """
    Score differential between the posteam and defteam at the start of the play.
    """

    header = "score_differential"


class QbHit2PlayerId:
    """
    Unique identifier for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.
    """

    header = "qb_hit_2_player_id"


class ForcedFumblePlayer2PlayerName:
    """
    String name of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_2_player_name"


class PenaltyPlayerName:
    """
    String name for the player with the penalty.
    """

    header = "penalty_player_name"


class PlayDeleted:
    """
    Binary indicator for deleted plays.
    """

    header = "play_deleted"


class PuntAttempt:
    """
    Binary indicator for punts.
    """

    header = "punt_attempt"


class Fantasy:
    """
    Name of the rusher on rush plays or receiver on pass plays.
    """

    header = "fantasy"


class VegasHomeWp:
    """
    Estimated win probability for the home team incorporating pre-game Vegas line.
    """

    header = "vegas_home_wp"


class TwoPointConvResult:
    """
    String indicator for result of two point conversion attempt: success, failure, safety (touchback in defensive endzone is 1 point apparently), or return.
    """

    header = "two_point_conv_result"


class LateralPuntReturnerPlayerId:
    """
    Unique identifier for the player that received the lateral on a punt return.
    """

    header = "lateral_punt_returner_player_id"


class AssistTackle4Team:
    """
    Team of one of the players with a tackle assist.
    """

    header = "assist_tackle_4_team"


class DefteamScore:
    """
    Score the defteam at the start of the play.
    """

    header = "defteam_score"


class ExtraPointResult:
    """
    String indicator for the result of the extra point attempt: good, failed, blocked, safety (touchback in defensive endzone is 1 point apparently), or aborted.
    """

    header = "extra_point_result"


class TackleForLoss2PlayerId:
    """
    Unique identifier for one of the potential players with the tackle for loss.
    """

    header = "tackle_for_loss_2_player_id"


class StPlayType:
    """
    Type of special teams play from NFL source. Available 2011 and beyond with source "nfl".
    """

    header = "st_play_type"


class QbScramble:
    """
    Binary indicator for whether or not the QB scrambled.
    """

    header = "qb_scramble"


class Weather:
    """
    String describing the weather including temperature, humidity and wind (direction and speed). Doesn't change during the game!
    """

    header = "weather"


class Cpoe:
    """
    For a single pass play this is 1 - cp when the pass was completed or 0 - cp when the pass was incomplete. Analyzed for a whole game or season an indicator for the passer how much over or under expectation his completion percentage was.
    """

    header = "cpoe"


class Stadium:
    """
    Game site name.
    """

    header = "stadium"


class PenaltyYards:
    """
    Yards gained (or lost) by the posteam from the penalty.
    """

    header = "penalty_yards"


class CompletePass:
    """
    Binary indicator for if the pass was completed.
    """

    header = "complete_pass"


class KickoffReturnerPlayerName:
    """
    String name for the kickoff returner.
    """

    header = "kickoff_returner_player_name"


class LateralRushingYards:
    """
    Numeric yards by the `lateral_rusher_player_name` in run plays with laterals. Please see the description of `lateral_rusher_player_name` for further information.
    """

    header = "lateral_rushing_yards"


class CompAirEpa:
    """
    EPA from the air yards alone only for completions.
    """

    header = "comp_air_epa"


class GameId:
    """
    Ten digit identifier for NFL game.
    """

    header = "game_id"


class PasserId:
    """
    ID of the player in the 'passer' column.
    """

    header = "passer_id"


class SackPlayerId:
    """
    Unique identifier of the player who recorded a solo sack.
    """

    header = "sack_player_id"


class Yrdln:
    """
    String indicating the current field position for a given play.
    """

    header = "yrdln"


class Rush:
    """
    Binary indicator if the play was a rushing play.
    """

    header = "rush"


class Special:
    """
    Binary indicator if "play_type" is one of "extra_point", "field_goal", "kickoff", or "punt".
    """

    header = "special"


class AssistTackle3PlayerName:
    """
    String name of one of the players with a tackle assist.
    """

    header = "assist_tackle_3_player_name"


class PunterPlayerName:
    """
    String name for the punter.
    """

    header = "punter_player_name"


class LateralSackPlayerId:
    """
    Unique identifier for the player that received the lateral on a sack.
    """

    header = "lateral_sack_player_id"


class TackledForLoss:
    """
    Binary indicator for whether or not a tackle for loss on a run play occurred.
    """

    header = "tackled_for_loss"


class OwnKickoffRecoveryTd:
    """
    Binary indicator for if the kicking team recovered the kickoff and scored a TD.
    """

    header = "own_kickoff_recovery_td"


class TotalAwayRushWpa:
    """
    Cumulative total rushing WPA for the away team in the game so far.
    """

    header = "total_away_rush_wpa"


class HalfSack2PlayerId:
    """
    Unique identifier of the second player who recorded half a sack.
    """

    header = "half_sack_2_player_id"


class AwayScore:
    """
    Total points scored by the away team.
    """

    header = "away_score"


class OldGameIdY:
    """
    No description available.
    """

    header = "old_game_id_y"


class AssistTackle4PlayerName:
    """
    String name of one of the players with a tackle assist.
    """

    header = "assist_tackle_4_player_name"


class ReturnTeam:
    """
    String abbreviation of the return team. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.
    """

    header = "return_team"


class HomeWp:
    """
    Estimated win probability for the home team.
    """

    header = "home_wp"


class ReceiverPlayerId:
    """
    Unique identifier for the receiver that was targeted on the pass.
    """

    header = "receiver_player_id"


class FumbleRecovery2Team:
    """
    Team of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_2_team"


class Ep:
    """
    Using the scoring event probabilities, the estimated expected points with respect to the possession team for the given play.
    """

    header = "ep"


class Total:
    """
    Equals home_score + away_score and means the total points scored in the given game.
    """

    header = "total"


class FumbleRecovery1PlayerId:
    """
    Unique identifier of one of the players with a fumble recovery.
    """

    header = "fumble_recovery_1_player_id"


class LateralInterceptionPlayerId:
    """
    Unique indentifier for the player that received the lateral on an interception.
    """

    header = "lateral_interception_player_id"


class Temp:
    """
    The temperature at the stadium only for 'roof' = 'outdoors' or 'open'.(Source: Pro-Football-Reference)
    """

    header = "temp"


class PuntOutOfBounds:
    """
    Binary indicator for if the punt went out of bounds.
    """

    header = "punt_out_of_bounds"


class PassOe:
    """
    Dropback percent over expected on a given play scaled from 0 to 100.
    """

    header = "pass_oe"


class DefensePlayers:
    """
    A list of every defensive player on the field for the play, by gsis_id
    """

    header = "defense_players"


class AssistTackle4PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.
    """

    header = "assist_tackle_4_player_id"


class PasserPlayerName:
    """
    String name for the player that attempted the pass.
    """

    header = "passer_player_name"


class DrivePlayIdEnded:
    """
    Play_id of the last play in the given drive.
    """

    header = "drive_play_id_ended"


class PassDefense2PlayerName:
    """
    String name of one of the players with a pass defense.
    """

    header = "pass_defense_2_player_name"


class TotalAwayRawAirWpa:
    """
    Cumulative total raw air WPA for the away team in the game so far.
    """

    header = "total_away_raw_air_wpa"


class GameDate:
    """
    Date of the game.
    """

    header = "game_date"


class SoloTackle1PlayerName:
    """
    String name of one of the players with a solo tackle.
    """

    header = "solo_tackle_1_player_name"


class GameHalf:
    """
    String indicating which half the play is in, either Half1, Half2, or Overtime.
    """

    header = "game_half"


class HomeOpeningKickoff:
    """
    1 if the home team received the opening kickoff, 0 otherwise.
    """

    header = "home_opening_kickoff"


class ExtraPointProb:
    """
    Predicted probability of the posteam scoring an extra point.
    """

    header = "extra_point_prob"


class Surface:
    """
    What type of ground the game was played on. (Source: Pro-Football-Reference)
    """

    header = "surface"


class TackleForLoss1PlayerId:
    """
    Unique identifier for one of the potential players with the tackle for loss.
    """

    header = "tackle_for_loss_1_player_id"


class SeriesResult:
    """
    Possible values: First down, Touchdown, Opp touchdown, Field goal, Missed field goal, Safety, Turnover, Punt, Turnover on downs, QB kneel, End of half
    """

    header = "series_result"


class LateralReceiverPlayerId:
    """
    Unique identifier for the player that received the last(!) lateral on a pass play.
    """

    header = "lateral_receiver_player_id"


class KickerPlayerId:
    """
    Unique identifier for the kicker on FG or kickoff.
    """

    header = "kicker_player_id"


class AirWpa:
    """
    WPA through the air (same logic as air_epa).
    """

    header = "air_wpa"


class OrderSequence:
    """
    Column provided by NFL to fix out-of-order plays. Available 2011 and beyond with source "nfl".
    """

    header = "order_sequence"


class SoloTackle2PlayerId:
    """
    Unique identifier of one of the players with a solo tackle.
    """

    header = "solo_tackle_2_player_id"


class AwayWp:
    """
    Estimated win probability for the away team.
    """

    header = "away_wp"


class KickDistance:
    """
    Numeric distance in yards for kickoffs, field goals, and punts.
    """

    header = "kick_distance"


class QbHit:
    """
    Binary indicator if the QB was hit on the play.
    """

    header = "qb_hit"


class DefendersInBox:
    """
    Number of defensive players lined up in the box at the snap.
    """

    header = "defenders_in_box"


class Id:
    """
    ID of the player in the 'name' column.
    """

    header = "id"


class TotalHomePassEpa:
    """
    Cumulative total passing EPA for the home team in the game so far.
    """

    header = "total_home_pass_epa"


class GameSecondsRemaining:
    """
    Numeric seconds remaining in the game.
    """

    header = "game_seconds_remaining"


class Xpass:
    """
    Probability of dropback scaled from 0 to 1.
    """

    header = "xpass"


class TotalAwayCompYacEpa:
    """
    Cumulative total completions yac EPA for the away team in the game so far.
    """

    header = "total_away_comp_yac_epa"


class TotalHomePassWpa:
    """
    Cumulative total passing WPA for the home team in the game so far.
    """

    header = "total_home_pass_wpa"


class PassLocation:
    """
    String indicator for pass location: left, middle, or right.
    """

    header = "pass_location"


class VegasWpa:
    """
    Win probability added (WPA) for the posteam: spread_adjusted model.
    """

    header = "vegas_wpa"


class FieldGoalAttempt:
    """
    Binary indicator for field goal attempt.
    """

    header = "field_goal_attempt"


class SoloTackle1PlayerId:
    """
    Unique identifier of one of the players with a solo tackle.
    """

    header = "solo_tackle_1_player_id"


class AwayCoach:
    """
    First and last name of the away team coach. (Source: Pro-Football-Reference)
    """

    header = "away_coach"


class PasserPlayerId:
    """
    Unique identifier for the player that attempted the pass.
    """

    header = "passer_player_id"


class DefenseCoverageType:
    """
    A string indicating what type of cover the defense was in on a play
    """

    header = "defense_coverage_type"


class LateralReception:
    """
    Binary indicator for if a lateral occurred on the reception.
    """

    header = "lateral_reception"


class AssistTackle:
    """
    Binary indicator for if an assist tackle occurred.
    """

    header = "assist_tackle"


class LateralReturn:
    """
    Binary indicator for if a lateral occurred on a return. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.
    """

    header = "lateral_return"


class FourthDownFailed:
    """
    Binary indicator for if the posteam failed to convert first down on fourth down.
    """

    header = "fourth_down_failed"


class AssistTackle1PlayerName:
    """
    String name of one of the players with a tackle assist.
    """

    header = "assist_tackle_1_player_name"


class RusherJerseyNumber:
    """
    Jersey number of the rusher.
    """

    header = "rusher_jersey_number"


class Interception:
    """
    Binary indicator for if the pass was intercepted.
    """

    header = "interception"


class FirstDownPass:
    """
    Binary indicator for if a passing play converted the first down.
    """

    header = "first_down_pass"


class TwoPointConversionProb:
    """
    Predicted probability of the posteam scoring the two point conversion.
    """

    header = "two_point_conversion_prob"


class TackleForLoss2PlayerName:
    """
    String name for one of the potential players with the tackle for loss.
    """

    header = "tackle_for_loss_2_player_name"


class TotalHomeCompYacEpa:
    """
    Cumulative total completions yac EPA for the home team in the game so far.
    """

    header = "total_home_comp_yac_epa"


class Fumbled2PlayerId:
    """
    Unique identifier of the second player who fumbled on the play.
    """

    header = "fumbled_2_player_id"


class LateralInterceptionPlayerName:
    """
    String name for the player that received the lateral on an interception.
    """

    header = "lateral_interception_player_name"


class Touchback:
    """
    Binary indicator for if a touchback occurred on the play.
    """

    header = "touchback"


class FantasyPlayerName:
    """
    Name of the rusher on rush plays or receiver on pass plays (from official stats).
    """

    header = "fantasy_player_name"


class DriveEndYardLine:
    """
    String indicating where a given drive ended consisting of team half and yard line number.
    """

    header = "drive_end_yard_line"


class Drive:
    """
    Numeric drive number in the game.
    """

    header = "drive"


class LateralRusherPlayerName:
    """
    String name for the player that received the last(!) lateral on a run play. If there were multiple laterals in the same play, this will only be the last player who received a lateral. Please see &lt;https://github.com/mrcaseb/nfl-data/tree/master/data/lateral_yards&gt; for a list of plays where multiple players recorded lateral rushing yards.
    """

    header = "lateral_rusher_player_name"


class ForcedFumblePlayer2Team:
    """
    Team of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_2_team"


class AwayTeam:
    """
    String abbreviation for the away team.
    """

    header = "away_team"


class OldGameIdX:
    """
    No description available.
    """

    header = "old_game_id_x"


class OwnKickoffRecovery:
    """
    Binary indicator for if the kicking team recovered the kickoff.
    """

    header = "own_kickoff_recovery"


class PlayType:
    """
    String indicating the type of play: pass (includes sacks), run (includes scrambles), punt, field_goal, kickoff, extra_point, qb_kneel, qb_spike, no_play (timeouts and penalties), and missing for rows indicating end of play.
    """

    header = "play_type"


class Shotgun:
    """
    Binary indicator for whether or not the play was in shotgun formation.
    """

    header = "shotgun"


class KickoffInsideTwenty:
    """
    Binary indicator for if the kickoff ended inside the twenty yard line.
    """

    header = "kickoff_inside_twenty"


class ForcedFumblePlayer1Team:
    """
    Team of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_1_team"


class FirstDownRush:
    """
    Binary indicator for if a running play converted the first down.
    """

    header = "first_down_rush"


class PuntReturnerPlayerName:
    """
    String name for the punt returner.
    """

    header = "punt_returner_player_name"


class Wpa:
    """
    Win probability added (WPA) for the posteam.
    """

    header = "wpa"


class Posteam:
    """
    String abbreviation for the team with possession.
    """

    header = "posteam"


class TotalLine:
    """
    The closing total line for the game. (Source: Pro-Football-Reference)
    """

    header = "total_line"


class StartTime:
    """
    Kickoff time in eastern time zone.
    """

    header = "start_time"


class RunLocation:
    """
    String indicator for location of run: left, middle, or right.
    """

    header = "run_location"


class FumbleOutOfBounds:
    """
    Binary indicator for if the fumble went out of bounds.
    """

    header = "fumble_out_of_bounds"


class FirstDownPenalty:
    """
    Binary indicator for if a penalty converted the first down.
    """

    header = "first_down_penalty"


class OppSafetyProb:
    """
    Predicted probability of the defteam scoring a safety next.
    """

    header = "opp_safety_prob"


class Location:
    """
    Either 'Home' o 'Neutral' indicating if the home team played at home or at a neutral site.
    """

    header = "location"


class ReplayOrChallenge:
    """
    Binary indicator for whether or not a replay or challenge.
    """

    header = "replay_or_challenge"


class TotalAwayRawYacWpa:
    """
    Cumulative total raw yac WPA for the away team in the game so far.
    """

    header = "total_away_raw_yac_wpa"


class TdPlayerName:
    """
    String name of the player who scored a touchdown.
    """

    header = "td_player_name"


class TackleWithAssist1PlayerId:
    """
    Unique identifier of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_1_player_id"


class GameStadium:
    """
    Name of the stadium the game was played in. (Source: Pro-Football-Reference)
    """

    header = "game_stadium"


class PenaltyTeam:
    """
    String abbreviation of the team with the penalty.
    """

    header = "penalty_team"


class QuarterSecondsRemaining:
    """
    Numeric seconds remaining in the quarter.
    """

    header = "quarter_seconds_remaining"


class HomeTimeoutsRemaining:
    """
    Numeric timeouts remaining in the half for the home team.
    """

    header = "home_timeouts_remaining"


class SeriesSuccess:
    """
    1: scored touchdown, gained enough yards for first down.
    """

    header = "series_success"


class TotalHomeCompAirWpa:
    """
    Cumulative total completions air WPA for the home team in the game so far.
    """

    header = "total_home_comp_air_wpa"


class FantasyPlayerId:
    """
    ID of the rusher on rush plays or receiver on pass plays (from official stats).
    """

    header = "fantasy_player_id"


class OutOfBounds:
    """
    1 if play description contains ran ob, pushed ob, or sacked ob; 0 otherwise.
    """

    header = "out_of_bounds"


class TotalHomeCompAirEpa:
    """
    Cumulative total completions air EPA for the home team in the game so far.
    """

    header = "total_home_comp_air_epa"


class FantasyId:
    """
    ID of the rusher on rush plays or receiver on pass plays.
    """

    header = "fantasy_id"


class QbDropback:
    """
    Binary indicator for whether or not the QB dropped back on the play (pass attempt, sack, or scrambled).
    """

    header = "qb_dropback"


class FumbleRecovery1Yards:
    """
    Yards gained by one of the players with a fumble recovery.
    """

    header = "fumble_recovery_1_yards"


class AssistTackle2Team:
    """
    Team of one of the players with a tackle assist.
    """

    header = "assist_tackle_2_team"


class ReceiverPlayerName:
    """
    String name for the targeted receiver.
    """

    header = "receiver_player_name"


class LateralRusherPlayerId:
    """
    Unique identifier for the player that received the last(!) lateral on a run play.
    """

    header = "lateral_rusher_player_id"


class EndClockTime:
    """
    Game time at the end of a given play.
    """

    header = "end_clock_time"


class KickoffAttempt:
    """
    Binary indicator for kickoff.
    """

    header = "kickoff_attempt"


class RunGap:
    """
    String indicator for line gap of run: end, guard, or tackle
    """

    header = "run_gap"


class PenaltyType:
    """
    String indicating the penalty type of the first penalty in the given play. Will be `NA` if `desc` is missing the type.
    """

    header = "penalty_type"


class RusherPlayerId:
    """
    Unique identifier for the player that attempted the run.
    """

    header = "rusher_player_id"


class XyacMedianYardage:
    """
    Median expected yards after the catch based on where the ball was caught.
    """

    header = "xyac_median_yardage"


class Timeout:
    """
    Binary indicator for whether or not a timeout was called by either team.
    """

    header = "timeout"


class Pass:
    """
    Binary indicator if the play was a pass play (sacks and scrambles included).
    """

    header = "pass"


class AssistTackle1Team:
    """
    Team of one of the players with a tackle assist.
    """

    header = "assist_tackle_1_team"


class HalfSecondsRemaining:
    """
    Numeric seconds remaining in the half.
    """

    header = "half_seconds_remaining"


class ThirdDownConverted:
    """
    Binary indicator for if the first down was converted on third down.
    """

    header = "third_down_converted"


class Success:
    """
    Binary indicator wheter epa &gt; 0 in the given play.
    """

    header = "success"


class DefenseManZoneType:
    """
    A string indicating whether the defense was in man or zone coverage on a play
    """

    header = "defense_man_zone_type"


class PuntInsideTwenty:
    """
    Binary indicator for if the punt ended inside the twenty yard line.
    """

    header = "punt_inside_twenty"


class CompYacEpa:
    """
    EPA from the yards after catch alone only for completions.
    """

    header = "comp_yac_epa"


class DivGame:
    """
    Binary indicator for if the given game was a division game.
    """

    header = "div_game"


class PuntInEndzone:
    """
    Binary indicator for if the punt was in the endzone.
    """

    header = "punt_in_endzone"


class PosteamScorePost:
    """
    Score for the posteam at the end of the play.
    """

    header = "posteam_score_post"


class TotalAwayScore:
    """
    Score for the away team at the start of the play.
    """

    header = "total_away_score"


class DefWp:
    """
    Estimated win probability for the defteam.
    """

    header = "def_wp"


class XyacSuccess:
    """
    Probability play earns positive EPA (relative to where play started) based on where ball was caught.
    """

    header = "xyac_success"


class ForcedFumblePlayer1PlayerName:
    """
    String name of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_1_player_name"


class YardsAfterCatch:
    """
    Numeric value for distance in yards perpendicular to the yard line where the receiver made the reception to where the play ended.
    """

    header = "yards_after_catch"


class JerseyNumber:
    """
    Jersey number of the player listed in the 'name' column.
    """

    header = "jersey_number"


class AbortedPlay:
    """
    Binary indicator if the play description indicates "Aborted".
    """

    header = "aborted_play"


class KickoffOutOfBounds:
    """
    Binary indicator for if the kickoff went out of bounds.
    """

    header = "kickoff_out_of_bounds"


class NoScoreProb:
    """
    Predicted probability of no score occurring for the rest of the half based on the expected points model.
    """

    header = "no_score_prob"


class PassDefense2PlayerId:
    """
    Unique identifier of one of the players with a pass defense.
    """

    header = "pass_defense_2_player_id"


class TotalHomeScore:
    """
    Score for the home team at the start of the play.
    """

    header = "total_home_score"


class VegasHomeWpa:
    """
    Win probability added (WPA) for the home team: spread_adjusted model.
    """

    header = "vegas_home_wpa"


class DriveStartTransition:
    """
    String indicating how the offense got the ball.
    """

    header = "drive_start_transition"


class WasPressure:
    """
    A boolean indicating whether or not the QB was pressured on a play
    """

    header = "was_pressure"


class TotalAwayPassEpa:
    """
    Cumulative total passing EPA for the away team in the game so far.
    """

    header = "total_away_pass_epa"


class Fumbled1PlayerId:
    """
    Unique identifier of the first player who fumbled on the play.
    """

    header = "fumbled_1_player_id"


class OwnKickoffRecoveryPlayerName:
    """
    String name for the player that recovered their own kickoff.
    """

    header = "own_kickoff_recovery_player_name"


class KickoffInEndzone:
    """
    Binary indicator for if the kickoff was in the endzone.
    """

    header = "kickoff_in_endzone"


class NflverseGameId:
    """
    nflverse identifier for games. Format is season, week, away_team, home_team
    """

    header = "nflverse_game_id"


class OffensePersonnel:
    """
    Number of running backs, tight ends, and wide receivers on the field for the play. If there are more than the standard 5 offensive linemen and 1 quarterback, they will be listed here as well.
    """

    header = "offense_personnel"


class Fumble:
    """
    Binary indicator for if a fumble occurred.
    """

    header = "fumble"


class PosteamTimeoutsRemaining:
    """
    Number of timeouts remaining for the possession team.
    """

    header = "posteam_timeouts_remaining"


class LateralKickoffReturnerPlayerName:
    """
    String name for the player that received the lateral on a kickoff return.
    """

    header = "lateral_kickoff_returner_player_name"


class Fumbled1PlayerName:
    """
    String name of one of the first player who fumbled on the play.
    """

    header = "fumbled_1_player_name"


class NDefense:
    """
    Number of defensive players on the field for the play
    """

    header = "n_defense"


class AwayWpPost:
    """
    Estimated win probability for the away team at the end of the play.
    """

    header = "away_wp_post"


class VegasWp:
    """
    Estimated win probabiity for the posteam given the current situation at the start of the given play, incorporating pre-game Vegas line.
    """

    header = "vegas_wp"


class SoloTackle1Team:
    """
    Team of one of the players with a solo tackle.
    """

    header = "solo_tackle_1_team"


class Touchdown:
    """
    Binary indicator for if the play resulted in a TD.
    """

    header = "touchdown"


class FixedDrive:
    """
    Manually created drive number in a game.
    """

    header = "fixed_drive"


class OwnKickoffRecoveryPlayerId:
    """
    Unique identifier for the player that recovered their own kickoff.
    """

    header = "own_kickoff_recovery_player_id"


class ForcedFumblePlayer1PlayerId:
    """
    Unique identifier of one of the players with a forced fumble.
    """

    header = "forced_fumble_player_1_player_id"


class AssistTackle3PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.
    """

    header = "assist_tackle_3_player_id"


class Epa:
    """
    Expected points added (EPA) by the posteam for the given play.
    """

    header = "epa"


class LateralRecovery:
    """
    Binary indicator for if a lateral occurred on a fumble recovery.
    """

    header = "lateral_recovery"


class TotalAwayCompAirWpa:
    """
    Cumulative total completions air WPA for the away team in the game so far.
    """

    header = "total_away_comp_air_wpa"


class AssistTackle2PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.
    """

    header = "assist_tackle_2_player_id"


class Play:
    """
    Binary indicator: 1 if the play was a 'normal' play (including penalties), 0 otherwise.
    """

    header = "play"


class NoHuddle:
    """
    Binary indicator for whether or not the play was in no_huddle formation.
    """

    header = "no_huddle"


class PuntReturnerPlayerId:
    """
    Unique identifier for the punt returner.
    """

    header = "punt_returner_player_id"


class PassingYards:
    """
    Numeric yards by the passer_player_name, including yards gained in pass plays with laterals. This should equal official passing statistics.
    """

    header = "passing_yards"


class ReceiverJerseyNumber:
    """
    Jersey number of the receiver.
    """

    header = "receiver_jersey_number"


class XyacEpa:
    """
    Expected value of EPA gained after the catch, starting from where the catch was made. Zero yards after the catch would be listed as zero EPA.
    """

    header = "xyac_epa"


class FumbleNotForced:
    """
    Binary indicator for if the fumble was not forced.
    """

    header = "fumble_not_forced"


class OffensePlayers:
    """
    A list of every offensive player on the field for the play, by gsis_id
    """

    header = "offense_players"


class TackleWithAssist2PlayerName:
    """
    String name of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_2_player_name"


class ReplayOrChallengeResult:
    """
    String indicating the result of the replay or challenge.
    """

    header = "replay_or_challenge_result"


class ReceivingYards:
    """
    Numeric yards by the receiver_player_name, excluding yards gained in pass plays with laterals. This should equal official receiving statistics but could miss yards gained in pass plays with laterals. Please see the description of `lateral_receiver_player_name` for further information.
    """

    header = "receiving_yards"


class PassLength:
    """
    String indicator for pass length: short or deep.
    """

    header = "pass_length"


class LateralRush:
    """
    Binary indicator for if a lateral occurred on a run.
    """

    header = "lateral_rush"


class SafetyPlayerId:
    """
    Unique identifier for the player who scored a safety.
    """

    header = "safety_player_id"


class RusherPlayerName:
    """
    String name for the player that attempted the run.
    """

    header = "rusher_player_name"


class DriveGameClockEnd:
    """
    Game time at the end of a given drive.
    """

    header = "drive_game_clock_end"


class TackleWithAssist2PlayerId:
    """
    Unique identifier of one of the players with a tackle with assist.
    """

    header = "tackle_with_assist_2_player_id"


class PlayClock:
    """
    Time on the playclock when the ball was snapped.
    """

    header = "play_clock"


class PasserJerseyNumber:
    """
    Jersey number of the passer.
    """

    header = "passer_jersey_number"
