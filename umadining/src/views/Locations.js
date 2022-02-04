import { Link } from "react-router-dom";
import { useState } from "react";
import Banner from "../components/Banner";
function Locations({setLocation}){

    // function generateBlueWall(){
    //     let obj = location.urls
    //     return Object.keys(obj).map( (x) => <Link key={x} className="blue-wall-item" to={{pathname: "/foods", state: {name: x, url: location.urls[x]}}}>{x}</Link>)
    // }

    // // if(location.name == "Blue Wall"){
    // //     return(
    // //         <div>
    // //             <Link to="/" id="back-button">Back</Link>
    // //             <Banner setLocation = {setLocation}/>
    // //             <div id="blue-wall-container">
    // //                 {generateBlueWall()}
    // //             </div>
    // //         </div>
    // //     )
    // // }
    return (
        <div>
            <Banner isHomepage={true}/>
        </div>
    )
}
export default Locations;