import React, {useEffect, useState} from 'react';
import {loadTweets} from "../lookup";

export  function  TweetComponent(props) {
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newValue = textAreaRef.current.value
        let newTemTweet = [...newValue]
        newTemTweet.unshift({
            content: newValue,
            id:1234,
            likes :0,
        })
        setNewTweets(newTemTweet)
        textAreaRef.current.value = ""
        console.log(newValue, newTweets={newTweets})
    }
    return <div className={props.className}>
                <div className="col-12 mb-3">
                    <form onSubmit={handleSubmit}>
                            <textarea required={true} ref={textAreaRef} className="form-control">
                            </textarea>
                            <button type="submit" className="btn btn-primary my-3">Tweet</button>
                    </form>
                </div>
            <TweetsList />
            </div>
}

export function TweetsList(props) {
    const [tweetInit,setTweetInit] = useState([])
    console.log(props.newTweet)
    useEffect(()=>{
        const myCallback =(response, status) => {
            if (status===200){
                setTweetInit(response)
            } else {
                alert("an error occered")
            }
        }
        loadTweets(myCallback)
    },[])
    return tweetInit.map((item, index)=> {
        return <Tweet tweet={item} className={"my-5 py-5 border bg-white text-dark "} key={`${index}-{item.id}`}/>
    })
}

export function ActionBtn(props) {
    const {tweet, action}= props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [userLike, setUserLike] = useState(tweet.userLike === true ? true :false)
    const className = props.className ? props.className : "btn btn-primary btn-sm"
    const actionDisplay = action.display ? action.display : "action"
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === "like") {
            if (userLike === true) {
                setLikes(likes-1)
                setUserLike(false)
            } else {
                setLikes(likes+1)
                setUserLike(true)
            }
        }
    }
    const display = action.type === "like" ? `${likes} ${actionDisplay}`: actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
}


export function Tweet(props) {
    const {tweet} = props
    const className = props.className ? props.className : "col-10 mx-auto col-md-6"
    return <div className={className}>
        <p>{tweet.id}-{tweet.content}</p>
        <div className="bt btn-group"> <ActionBtn tweet={tweet} action={{type:"like", display:"like"}}/></div>
        <div className="bt btn-group"> <ActionBtn tweet={tweet} action={{type:"unlike", display:"unlike"}}/></div>
        <div className="bt btn-group"> <ActionBtn tweet={tweet} action={{type:"retweet",display:"retweet"}}/></div>
    </div>
}
