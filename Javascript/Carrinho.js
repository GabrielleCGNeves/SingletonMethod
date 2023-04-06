const Carrinho =(function(){
    let instance;

    function createInstance(){
        let produtos = [];

        function addProduto(produto){
            produtos.push(produto);
        }

        function getProduto(){
            return produtos;
        }

        function clearCarrinho(){
            produtos = [];
        }

        return{
            addProduto,
            getProduto,
            clearCarrinho
        };
    }

    return {
        getInstance: () => {
            if(!instance){
                instance = createInstance();
            }
            return instance;
        }
    }
})();

// --------------------------------------------------
//Cliente

const carrinho = Carrinho.getInstance();

carrinho.addProduto({id: 001, nome:"Banana", preco: 4.00});
carrinho.addProduto({id: 002, nome:"Melao", preco: 10.00});
carrinho.addProduto({id: 003, nome:"Amandita", preco: 12.00});
carrinho.addProduto({id: 004, nome:"Bolacha Waffle", preco: 4.69});

console.log(carrinho.getProduto());
