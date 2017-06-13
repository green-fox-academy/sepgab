import React from "react";
import { render } from "react-dom";

import { Header } from "./components/Header";
import { Home } from "./components/Home";

class App extends React.Component {

  constructor() {
    super();
    this.state = {
      homeLink: "Home",
      homeMounted: true
    };
  }

  onGreet() {
    alert("Hello!");
  }

  onChangeLinkName(newName) {
    this.setState({
      homeLink: newName
    });
  }

  onChangeHomeMounted() {
    this.setState({
      homeMounted: !this.state.homeMounted
    });
  }

  render() {
    let user = {
      name: "Anna",
      initialAge: 28,
      hobbies: ['sports', 'reading']
    };
    let homeCmp="";
    if (this.state.homeMounted) {
      homeCmp = (
        <Home
          name={"Gabor"}
          initialAge={32}
          user={user}
          greet={this.onGreet}
          changeLink={this.onChangeLinkName.bind(this)}
          initialLinkName={this.state.homeLink}
        >
          <p>This is a paragraph</p>
        </Home>
      )
    }
    return (
      <div className="container">
        <div className="row">
          <div className="col-xs-10 col-xs-offset-1">
            <Header homeLink={this.state.homeLink}/>
          </div>
        </div>
        <div className="row">
          <div className="col-xs-10 col-xs-offset-1">
            {homeCmp}
          </div>
          <div className="col-xs-10 col-xs-offset-1">
            <button onClick={this.onChangeHomeMounted.bind(this)} className="btn btn-primary">(Un)mount home component</button>
          </div>
        </div>
      </div>
    );
  }
}

render(<App/>, window.document.getElementsByClassName('app')[0]);
