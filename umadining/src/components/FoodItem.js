import React, {useState} from 'react';
import "../styles/FoodItem.css"

function FoodItem({food, setTotal, total}){

    const [num, setNum] = useState(0);
    const name = Object.keys(food)[0];
    const nutrients = food[name];

    function increment(){
        let arr = total;
        arr.push(food);
        setTotal(arr);
        setNum(num+1);
    }
    function decrement(){
        if(num == 0){
            return;
        }
        let arr = total;
        arr = arr.filter( (e, i) => i != arr.indexOf(e));
        setTotal(arr);
        setNum(num - 1);
    }

    return(
        <div className="food-item">
            <div className='food-info'>
                <h2 className='food-name'>{name}</h2>
                <p className='food-serving-size'>Serving Size: {nutrients.servingSize}</p>
                <p className='food-calories'>{nutrients.calories} calories</p>
            </div>
            <div className='counter'>
                <p className='food-count'>{num}</p>
                <p className='food-plus food-select' onClick={increment}>+</p>
                <p className='food-minus food-select' onClick={decrement}>-</p>
            </div>
        </div>
    )
}

export default FoodItem;