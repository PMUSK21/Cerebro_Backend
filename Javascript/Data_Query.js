    
function makeHttpRequest(url, method, data) {
  return new Promise((resolve, reject) => {
    fetch(url, {
      method: method,
      headers: {
        'Content-Type': 'application/json', // You can set the appropriate content type
      },
      body: JSON.stringify(data), // You can send data if needed
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // You can also use .text() or other methods to parse the response
      })
      .then(data => {
        resolve(data); // Resolves with the parsed response data
      })
      .catch(error => {
        reject(error); // Rejects with an error in case of a failure
      });
  });
}