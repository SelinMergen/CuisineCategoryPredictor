import React from 'react'
import ingredients from "./Ingredients.json"

function List(props) {
    const filteredSearch = ingredients.filter((item) => {
        if (props.input === '') {
            return item;
        }
        else {
            return item.text.toLowerCase().includes(props.input)
        }
    })
    return (
        <ul>
            {filteredSearch.map((item) => (
                <li key={item.id}>{item.text}</li>
            ))}
        </ul>
    )
}

export default List