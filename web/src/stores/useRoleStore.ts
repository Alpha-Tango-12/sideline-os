import { create } from "zustand";
import type { Role } from "@/types";

interface RoleState {
  activeRole: Role | null;
  viewAllRoles: boolean;
  setActiveRole: (role: Role) => void;
  setViewAllRoles: (value: boolean) => void;
}

export const useRoleStore = create<RoleState>((set) => ({
  activeRole: null,
  viewAllRoles: false,
  setActiveRole: (role) => set({ activeRole: role }),
  setViewAllRoles: (value) => set({ viewAllRoles: value }),
}));
