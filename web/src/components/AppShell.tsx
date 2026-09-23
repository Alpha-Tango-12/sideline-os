import { NavLink, Outlet } from "react-router-dom";
import { CalendarDays, LayoutGrid, ClipboardList, Video, FileText } from "lucide-react";

const NAV_ITEMS = [
  { to: "/weekly", label: "Weekly Cycle", icon: CalendarDays },
  { to: "/daily", label: "Daily View", icon: LayoutGrid },
  { to: "/workflow", label: "Workflow Manager", icon: ClipboardList },
  { to: "/sideline-sheet", label: "Sideline Sheet", icon: FileText },
  { to: "/video-hub", label: "Video Hub", icon: Video },
];

export function AppShell() {
  return (
    <div className="flex min-h-screen bg-[var(--color-base)] text-[var(--color-text-primary)]">
      <aside className="flex w-56 flex-col gap-1 border-r border-[var(--color-border)] bg-[var(--color-surface)] p-3">
        <div className="mb-4 px-2 text-lg font-semibold tracking-tight">Sideline OS</div>
        {NAV_ITEMS.map(({ to, label, icon: Icon }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              `flex items-center gap-3 rounded-md px-3 py-2.5 text-sm transition-colors ${
                isActive
                  ? "bg-[var(--color-accent)] text-white"
                  : "text-[var(--color-text-secondary)] hover:bg-[var(--color-surface-raised)]"
              }`
            }
          >
            <Icon size={18} />
            {label}
          </NavLink>
        ))}
      </aside>
      <main className="flex-1 overflow-y-auto p-6">
        <Outlet />
      </main>
    </div>
  );
}
