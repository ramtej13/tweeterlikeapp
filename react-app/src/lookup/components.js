

export function loadTweets(callback) {
    const method = 'GET'
    const url = 'http://127.0.0.1:8000/api/'
    const responseType = "json"
    const xhr = new XMLHttpRequest()
    xhr.responseType = responseType
    xhr.open(method,url)
    xhr.onload = function() {
        callback(xhr.response,xhr.status)
    }
    xhr.onerror= (e) => {
        console.log(e)
        callback({"message":"it is an error"},400)
    }
    xhr.send()
}