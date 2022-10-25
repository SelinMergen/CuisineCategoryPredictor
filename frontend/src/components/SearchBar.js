import React, { useState } from "react";
import TextField from '@mui/material/TextField';
import List from "./List/ListIngredients";
import "../App.css";
import {IconButton, InputAdornment} from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';

function SearchBar() {
    const [searchText, setSearchText] = useState("");
    function inputHandler(e){
        const lowerCase = e.target.value.toLowerCase();
        setSearchText(lowerCase);
    }

    function addItem(e){
        //TODO: Add item to ingredients list
        console.log("Clicked Search Icon");
    }

    return (
        <div className="search-bar">
            <TextField
                className="search"
                id="outlined-basic"
                onChange={inputHandler}
                variant="outlined"
                label="Search"
                InputProps={{
                    endAdornment:
                        <InputAdornment position="end">
                            <IconButton aria-label="search" onClick={addItem}>
                                <SearchIcon />
                            </IconButton>
                        </InputAdornment>,
                }}
            />
            <List input={searchText} />
        </div>
    );
}

export default SearchBar;