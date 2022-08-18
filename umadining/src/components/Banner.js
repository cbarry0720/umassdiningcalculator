import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/Banner.css'

function Banner({isHomepage}){

    return (
        <div className={isHomepage ? "banner-home" : "banner"}>
            <Link to="/" className={isHomepage ? "banner-item-home" : 'banner-item'} id='umass-dining-logo'>
                <img src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F5af9e0c7e17ba3a6ffa3915c%2F1547774497921-1FPJ9W2KB951X1QCE4GF%2Fke17ZwdGBToddI8pDm48kH59gecQ5dOfjNsoDD7m6gkUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYxCRW4BPu10St3TBAUQYVKcTBp4-VbWBCpPkYX5QZK_OBzCGuu7aB5AMcaUBcnVz41BGLuoZ5YH-KDIIeh3_sea%2FUMass%2BDining%2BLogo%2B1%2Bcopy.png&f=1&nofb=1'></img>
            </Link>
            <Link className={isHomepage ? "banner-item-home" : 'banner-item'} to="/foods" state={{name: "Berkshire Dining Commons", url: "https://umassdining.com/locations-menus/berkshire/menu"}}>
                <p>Berkshire</p>
            </Link>
            <Link className={isHomepage ? "banner-item-home" : 'banner-item'} to="/foods" state={{name: "Franklin Dining Commons", url: "https://umassdining.com/locations-menus/franklin/menu"}}>
                <p>Franklin</p>
            </Link>
            <Link className={isHomepage ? "banner-item-home" : 'banner-item'} to="/foods" state={{name: "Hampshire Dining Commons", url: "https://umassdining.com/locations-menus/hampshire/menu"}}>
                <p>Hampshire</p>
            </Link>
            <Link className={isHomepage ? "banner-item-home" : 'banner-item'} to="/foods" state={{name: "Worcester Dining Commons", url: "https://umassdining.com/locations-menus/worcester/menu"}}>
                <p>Worcester</p>
            </Link>
            <Link className={isHomepage ? "banner-item-home" : 'banner-item'} to="/foods" state={{name: "Blue Wall"}}>
                <p>Blue Wall</p>
            </Link>
        </div>
    )
}

export default Banner