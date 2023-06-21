let updateBtn = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(e){
        e.preventDefault();
        let productId = this.getAttribute('data-product');
        let action = this.getAttribute('data-action');

        if(user === 'AnonymousUser'){
            Swal.fire({
                icon: 'warning',
                title: 'Oops...',
                text: 'Please Login',
                confirmButtonColor: '#f0ad4e'
              })
        }else{
            updateUserOrder(productId, action)
        }
    });
}

function updateUserOrder(productId, action){
    let url = '/update_item/';

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
    .then(()=> {
        location.reload();
    });
}

let deleteBtns = document.getElementsByClassName('delete-item');

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', function(e){
        e.preventDefault();
        let productId = this.getAttribute('data-product');

        if(user === 'AnonymousUser'){
            Swal.fire({
                icon: 'warning',
                title: 'Oops...',
                text: 'Please Login',
                confirmButtonColor: '#f0ad4e'
              })
        } else {
            deleteUserOrder(productId);
        }
    });
}

function deleteUserOrder(productId) {
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
    .then(() => {
        location.reload();
    });
}
