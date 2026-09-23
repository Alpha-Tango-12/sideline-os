import { create } from "zustand";
import type { GamePlan } from "@/types";

interface GamePlanState {
  activeGamePlan: GamePlan | null;
  setActiveGamePlan: (gamePlan: GamePlan) => void;
}

export const useGamePlanStore = create<GamePlanState>((set) => ({
  activeGamePlan: null,
  setActiveGamePlan: (gamePlan) => set({ activeGamePlan: gamePlan }),
}));
