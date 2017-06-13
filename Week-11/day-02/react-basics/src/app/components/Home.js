import React from "react";

export class Home extends React.Component {

  constructor(props) {
    super();
    this.state = {
      age: props.initialAge,
      status: 0,
      homeLink: props.initialLinkName
    };
    setTimeout(() => {
      this.setState({
        status: this.state.status +1
      })
    },3000);
    console.log("Constructor");
  }

  componentWillMount() {
    console.log("Component will mount");
  }

  componentDidMount() {
    console.log("Component did mount");
  }

  componentWillReceiveProps(nextProps) {
    console.log("Component will receive props", nextProps);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log("Should component update", nextProps, nextState);
    // if (nextState.status === 1) {
    //   return false
    // }
    return true;
  }

  componentWillUpdate(nextProps, nextState) {
    console.log("Component will update", nextProps, nextState);
  }

  componentDidUpdate(prevProps, prevState) {
    console.log("Component did update", prevProps, prevState);
  }

  componentWillUnmount() {
    console.log("Component will unmount");
  }

  onMakeOlder() {
    // this.age += 3;
    // console.log(this.age);
    this.setState({
      age: this.state.age + 3
    })
  }

  onChangeLink() {
    this.props.changeLink(this.state.homeLink);
  }

  onHandleChange(event) {
    this.setState({
      homeLink: event.target.value
    });
  }

  render() {
    let content = "";
    if (true) {
      content = "Hello!";
    }
    console.log(this.props);
    return (
      <div>
        <p>In a new Component!</p>
        {content}
        <p>Your name is {this.props.name} and your age is {this.state.age}</p>
        <p>Status: {this.state.status}</p>
        <button onClick={this.onMakeOlder.bind(this)} className="btn btn-primary">Make me older!</button>
        <p>User Object => Name: {this.props.user.name}</p>
        <div>
          <h4> Hobbies: </h4>
          <ul>
            {this.props.user.hobbies.map((hobby, i) => <li key={i}>{hobby}</li>)}
          </ul>
        </div>
        <div>{this.props.children}</div>
        <hr/>
        <button onClick={this.props.greet} className="btn btn-primary">Greet</button>
        <hr/>
        <input type="text" value={this.state.homeLink}
          onChange={(event) => this.onHandleChange(event)} />
        <button onClick={this.onChangeLink.bind(this)} className="btn btn-primary">Change header link</button>
      </div>
    );
  }
}

Home.propTypes = {
  name: React.PropTypes.string,
  initialAge: React.PropTypes.number,
  user: React.PropTypes.object,
  children: React.PropTypes.element.isRequired,
  greet: React.PropTypes.func,
  initialLinkName: React.PropTypes.string
};
