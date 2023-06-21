let updateBtnn = document.querySelectorAll('a[data-wishlist-product]');
if(updateBtnn.length > 0) {
    for (let i = 0; i < updateBtn.length; i++) {
        updateBtnn[i].addEventListener('click', function(e){
            e.preventDefault();
            let productId = this.getAttribute('data-wishlist-product');


            if(user === 'AnonymousUser'){
                Swal.fire({
                    icon: 'warning',
                    title: 'Oops...',
                    text: 'Please Login',
                    confirmButtonColor: '#f0ad4e'
                })
            }else{
                updateUserWishlist(productId)
            }
        });
    }
}

function updateUserWishlist(productId){
    let url = '/update_wishlist_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId})
    })
    .then((response)=> {
        return response.json();
    })
    .then(()=> {
        location.reload();
    });
}

let deleteBtnss = document.querySelectorAll('a[data-delete-wishlist-product]');

for (let i = 0; i < deleteBtnss.length; i++) {
    deleteBtnss[i].addEventListener('click', function(e){
        e.preventDefault();
        let productId = this.getAttribute('data-delete-wishlist-product');
        if(user === 'AnonymousUser'){
            Swal.fire({
                icon: 'warning',
                title: 'Oops...',
                text: 'Please Login',
                confirmButtonColor: '#f0ad4e'
              })
        } else {
            deleteUserWishlist(productId);
        }
    });
}

function deleteUserWishlist(productId) {
    let url = '/delete_wishlist_item/';

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
