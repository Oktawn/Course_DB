import { Outlet } from "react-router-dom";
import { Header } from "../components/Header/Header";

export function LoginLayout() {
    return (
        <>
            <Header />
            <Outlet />
            {/* <Footer /> */}
        </>
    )
}