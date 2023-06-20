//Update Cart

let updateBtn = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(){
        let productId = this.getAttribute('data-product');
        let action = this.getAttribute('data-action');
        console.log('productId:', productId, 'Action:', action);
    });
}



