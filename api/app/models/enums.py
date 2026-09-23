import enum


class GamePlanStatus(str, enum.Enum):
    planning = "planning"
    practice = "practice"
    finalized = "finalized"
    played = "played"
    archived = "archived"


class PermissionScope(str, enum.Enum):
    full_plan = "full_plan"
    position_group = "position_group"
    situational = "situational"
    video_only = "video_only"


class CycleDay(str, enum.Enum):
    mon = "mon"
    tue = "tue"
    wed = "wed"
    thu = "thu"
    fri = "fri"
    sat = "sat"
    sun = "sun"


class CyclePhase(str, enum.Enum):
    self_scout = "self_scout"
    install = "install"
    practice_script = "practice_script"
    final_prep = "final_prep"
    game = "game"


class TaskStatus(str, enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    blocked = "blocked"
    done = "done"


class SideOfBall(str, enum.Enum):
    offense = "offense"
    defense = "defense"
    special_teams = "special_teams"


class PlayType(str, enum.Enum):
    run = "run"
    pass_ = "pass"
    rpo = "rpo"
    screen = "screen"
    special_teams = "special_teams"


class TagCategory(str, enum.Enum):
    situation = "situation"
    down_distance = "down_distance"
    field_zone = "field_zone"
    priority = "priority"
    personnel_note = "personnel_note"


class ClipSource(str, enum.Enum):
    upload = "upload"
    external_url = "external_url"


class DownDistanceBucket(str, enum.Enum):
    first_10 = "1st_10"
    second_short = "2nd_short"
    second_medium = "2nd_medium"
    second_long = "2nd_long"
    third_short = "3rd_short"
    third_medium = "3rd_medium"
    third_long = "3rd_long"
    fourth_down = "4th_down"
    red_zone = "red_zone"
    goal_line = "goal_line"
    two_minute = "two_minute"


class FieldZone(str, enum.Enum):
    own_territory = "own_territory"
    midfield = "midfield"
    opp_territory = "opp_territory"
    red_zone = "red_zone"
    goal_line = "goal_line"


class HashPosition(str, enum.Enum):
    left = "left"
    middle = "middle"
    right = "right"
    any = "any"


class ScriptStatus(str, enum.Enum):
    draft = "draft"
    published = "published"


class Tempo(str, enum.Enum):
    walkthrough = "walkthrough"
    indy = "indy"
    group = "group"
    team = "team"
    live = "live"


class ScoutCardGenerationMode(str, enum.Enum):
    manual_assist = "manual_assist"
    auto_from_tendencies = "auto_from_tendencies"


class PushedEntityType(str, enum.Enum):
    sideline_sheet = "sideline_sheet"
    practice_script = "practice_script"
    scout_card = "scout_card"


class TargetAudience(str, enum.Enum):
    full_team = "full_team"
    offense = "offense"
    defense = "defense"
    special_teams = "special_teams"
    position_group = "position_group"
