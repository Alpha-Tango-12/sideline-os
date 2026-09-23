import { Routes, Route, Navigate } from "react-router-dom";
import { AppShell } from "@/components/AppShell";
import { WeeklyCyclePage } from "@/pages/WeeklyCyclePage";
import { DailyViewPage } from "@/pages/DailyViewPage";
import { WorkflowManagerPage } from "@/pages/WorkflowManagerPage";
import { SidelineSheetPage } from "@/pages/SidelineSheetPage";
import { VideoHubPage } from "@/pages/VideoHubPage";
import { ScriptCardBuilderPage } from "@/pages/ScriptCardBuilderPage";

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<Navigate to="/weekly" replace />} />
        <Route path="/weekly" element={<WeeklyCyclePage />} />
        <Route path="/daily" element={<DailyViewPage />} />
        <Route path="/workflow" element={<WorkflowManagerPage />} />
        <Route path="/sideline-sheet" element={<SidelineSheetPage />} />
        <Route path="/video-hub" element={<VideoHubPage />} />
        <Route path="/scripts-cards" element={<ScriptCardBuilderPage />} />
      </Route>
    </Routes>
  );
}
