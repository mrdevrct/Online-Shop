// fetch('http://127.0.0.1:8000/data/users', {
//     method: 'GET',
//     headers: {
//         'Content-Type': 'application/json'
//     },
// })
//     .then(response => response.json())
//     .then(response => {
//         let users = response.data;
//         users.forEach(user => {
//             console.log(user);
//         });
//     })
//     .catch(error => {
//         console.log(error);
//     });


function signup() {
    let formData = {
    "nameLastname": nameLastname.value,
    "username": username.value,
    "password": password.value,
    "email": email.value,
    "phoneNumber": phoneNumber.value,
    "city": city.value,
    "address": address.value,
    "nationalCode": nationalCode.value,
    }

    fetch('http://127.0.0.1:8000/add/user', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(formData)
    })
    .then( response => {
    console.log(response)
    })
    .catch(error => {
    console.log(error)
    })
}

function login() {
fetch('http://127.0.0.1:8000/data/users', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
    .then(response => response.json())
    .then(response => {
        let users = response.data;
        users.forEach(user => {
            if  (user.username === loginUsername.value && user.password ===loginPassword.value){
                console.log('ok')
            }
            else{
                console.log('error')
            }
        });
    })
    .catch(error => {
        console.log(error);
    });
}

// function remove() {
//     let formData ={
//         'id' : idUser.value,
//     }
//     fetch('http://127.0.0.1:8000/delete/user', {
//     method: 'DELETE',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(formData)
//     })
//     .then( response => {
//     console.log(response);
//     })
//     .catch(error => {
//     console.log(error);
//     });
// }


// function update() {
//     let formData = {
//         "id" : updateID.value,
//         "username": FirstName.value,
//         "lastname": lastName.value,
//       }
//         fetch('http://127.0.0.1:8000/update/user', {
//         method: 'PUT',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(formData)
//       })
//       .then( response => {
//         console.log(response);
//       })
//       .catch(error => {
//         console.log(error);
//       });
// }

