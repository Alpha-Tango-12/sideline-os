export type CyclePhase = "self_scout" | "install" | "practice_script" | "final_prep" | "game";
export type CycleDay = "mon" | "tue" | "wed" | "thu" | "fri" | "sat" | "sun";
export type TaskStatus = "not_started" | "in_progress" | "blocked" | "done";
export type PermissionScope = "full_plan" | "position_group" | "situational" | "video_only";

export interface Role {
  id: string;
  name: string;
  description: string | null;
  permissionScope: PermissionScope;
}

export interface GamePlan {
  id: string;
  opponentName: string;
  season: number;
  weekNumber: number;
  gameDate: string;
  status: "planning" | "practice" | "finalized" | "played" | "archived";
}

export interface WeeklyTask {
  id: string;
  gamePlanId: string;
  roleId: string;
  assignedStaffMemberId: string | null;
  title: string;
  description: string | null;
  cycleDay: CycleDay;
  cyclePhase: CyclePhase;
  status: TaskStatus;
  dueAt: string | null;
  linkedEntityType: string | null;
  linkedEntityId: string | null;
}
