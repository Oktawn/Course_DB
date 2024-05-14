import { BrowserRouter, Route, Routes } from "react-router-dom";
import PageNotFound from "./pages/PageNotFound";
import { MainLayout } from "./layouts/MainLayout";
import { LoginLayout } from "./layouts/LoginLayout";


export function Router() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainLayout />}>
                    <Route path="/" element={<Main />} />
                    <Route path="/Schedule" element={<Schedule />} />
                </Route>

                <Route path="/Login" element={<LoginLayout />}>
                    <Route path="/Login" element={<Login />} />
                </Route>

                <Route element={<PageNotFound />} path="*" />
            </Routes>
        </BrowserRouter>
    )
}