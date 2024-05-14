import { Link } from "react-router-dom";

function PageNotFound() {
    return (
        < div>
            <h2>Page not found</h2>
            <p>
                return to<Link to="/"> main page</Link>
            </p>
        </div>
    )
}

export default PageNotFound;