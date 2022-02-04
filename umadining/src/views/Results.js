import { useLocation } from "react-router";
import { Navigate } from "react-router";
import Banner from "../components/Banner";
import "../styles/Results.css"
const Results = function(){

    const location = useLocation();
    if(location.state == null){
        <Navigate to="/"/>
    }

    console.log(location.state.total)

    function foodToRow(food){
        let name = Object.keys(food)[0]
        let nutrients = food[name]
        console.log(name)
        console.log(nutrients)
        return(
            <tr>
                <td>{name}</td><td>{nutrients.calories}</td><td>{nutrients.carbs}</td><td>{nutrients.protein}</td><td>{nutrients.fat}</td><td>{nutrients.cholesterol}</td><td>{nutrients.sodium}</td>
            </tr>
        )
    }

    function eliminateLetters(str){
        return parseFloat(str.replace(/[^0-9.]/, ''));
    }

    function getTotals(total){
        let calories = 0;
        let carbs = 0;
        let protein = 0;
        let fat = 0;
        let cholesterol = 0;
        let sodium = 0;
        for(let i in total){
            let k = Object.keys(total[i])[0];
            let nutrients = total[i][k]
            calories += parseFloat(nutrients.calories);
            carbs += eliminateLetters(nutrients.carbs)
            protein += eliminateLetters(nutrients.protein)
            fat += eliminateLetters(nutrients.fat)
            cholesterol += eliminateLetters(nutrients.cholesterol)
            sodium += eliminateLetters(nutrients.sodium)
        }
        return (<tr>
                    <td>Totals</td><td>{calories.toFixed(1)}</td><td>{carbs.toFixed(1)}g</td><td>{protein.toFixed(1)}g</td><td>{fat.toFixed(1)}g</td><td>{cholesterol.toFixed(1)}mg</td><td>{sodium.toFixed(1)}mg</td>
                </tr>)
    }

    return (
        <div className="container">
            <Banner isHomepage={false}/>
            <h2>Your Results</h2>
            <table id="table">
                <thead>
                    <tr id="header">
                        <th>Food</th><th>Calories</th><th>Carbs</th><th>Protein</th><th>Total Fat</th><th>Cholesterol</th><th>Sodium</th>
                    </tr>
                </thead>
                <tbody>
                    {location.state.total.map(foodToRow)}
                </tbody>
                <tfoot>
                    {getTotals(location.state.total)}
                </tfoot>
            </table>
        </div>
    )
}
export default Results;