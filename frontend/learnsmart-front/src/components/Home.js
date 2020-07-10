import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Link, withRouter} from "react-router-dom";
import '../styles/App.css';
class Home extends Component {

    render() {
        return (
            
                <div  className="bg-color bodyheigth">
                                
                    <div className="container">
                        <div className="row">
                            <div className="col-lg-12 mt-5">
                                <h2 className="text-white">Learning easily with quizzes </h2>
                            </div>
                            <div className="col-lg-12 mt-5">
                            <Link to="/signup"><button className="btn btn-yellow t-medium text-darkblue" >create a FREE Account</button></Link>
                            
                            </div>
                        </div>
                    </div>
                </div>
            
        );
    }
}
 
export default Home;