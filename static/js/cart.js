
let updateBtn = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(e){
        e.preventDefault();
        let productId = this.getAttribute('data-product');
        let action = this.getAttribute('data-action');
        console.log('productId:', productId, 'Action:', action);

        console.log('USER:', user);
        if(user === 'AnonymousUser'){
            console.log('Not logged in');
        }else{
            updateUserOrder(productId, action)
        }
    });
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...');
        let url = '/update_item/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })
        .then((response)=> {
                return response.json();
        })
        .then((data)=> {
                console.log('Data:', data);
                location.reload()
        })
}
///Delete Item

let deleteBtns = document.getElementsByClassName('delete-item');

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', function(e){
        e.preventDefault();
        let productId = this.getAttribute('data-product');
        console.log('productId:', productId);

        console.log('USER:', user);
        if(user === 'AnonymousUser'){
            console.log('Not logged in');
        } else {
            deleteUserOrder(productId);
        }
    });
}

function deleteUserOrder(productId) {
    console.log('User is authenticated, sending data...');
    let url = '/delete_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('Data:', data);
        location.reload();
    });
}




