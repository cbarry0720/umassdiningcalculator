import React, {useState, useEffect} from "react"
import Banner from "../components/Banner";
import { useLocation } from "react-router";
import { Navigate, Link} from "react-router-dom"
import FoodItem from "../components/FoodItem";
function FoodSelector(){
    const location = useLocation();
    const [loading, setLoading] = useState(true);
    const [foods, setFoods] = useState({});
    const [total, setTotal] = useState([]);
    const [search, setSearch] = useState("");

    // const cheerio = require('cheerio');
    const axios = require('axios');

    useEffect(function(){
        setLoading(true)
        if(location.state == null){
            return null;
        }

        axios.get("http://45.56.115.124:5000/foods", {params: {loc: location.state.name}}).then(function(x){
            let json = x.data;
            console.log(json)
            setFoods(json);
        });

        setLoading(false);
    }, [location.state.name]);
    if(location.state == null){
        return <Navigate to="/"/>
    }

    function outputFoods(json){
        let arr = []
        let temp = {}
        for(let i in Object.keys(json)){
            let k = Object.keys(json)[i];
            temp[k] = {}
            for(let i in Object.keys(json[k])){
                let key = Object.keys(json[k])[i];
                if(key.toLowerCase().includes(search.toLowerCase())){
                    temp[k][key] = json[k][key]
                }
            }
        }
        Object.keys(temp).forEach((x) =>{
            if(Object.keys(temp[x]).length === 0){
                return;
            }
            arr.push(<div className="location-name" key={x}>{x}</div>);
            let foodarr = []
            Object.keys(temp[x]).forEach((e) => {
                let object = {};
                object[e] = temp[x][e]
                foodarr.push(<FoodItem key = {e + " " + x} food={object} total={total} setTotal={setTotal}/>)
            });
            console.log("foodarr")
            console.log(foodarr)
            arr.push(<div className="foods-container">{foodarr}</div>)
        });
        console.log("arr")
        console.log(arr)
        return arr;
    }

    function handleSearch(e){
        setSearch(e.target.value);
    }
    if(loading){
        return <div>
                    <Banner isHomepage={false} />
                    <img id="loading-image" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.giphy.com%2Fmedia%2Fw7jtVnXxMOq08%2Fgiphy.gif&f=1&nofb=1"/>
                </div>
    }
    return(
        <div>
            <Banner isHomepage={false}/>
            <div id="search-submit" >
                <input type="search" onChange={handleSearch} placeholder="Search Food"/>
                <Link id="submit-button" to="/results" state={{total: total}}>
                    Calculate
                </Link>
            </div>
            {outputFoods(foods)}
        </div>
    )
}
export default FoodSelector;
