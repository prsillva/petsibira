'use strict';

const limparFormulario5 = (endereco5) =>{
    document.getElementById('id_Rua').value = '';
    document.getElementById('id_Bairro').value = '';
    document.getElementById('id_Cidade').value = '';
    document.getElementById('id_Estado').value = '';
}


const preencherFormulario5 = (endereco5) =>{
    document.getElementById('id_Rua').value = endereco5.logradouro;
    document.getElementById('id_Bairro').value = endereco5.bairro;
    document.getElementById('id_Cidade').value = endereco5.localidade;
    document.getElementById('id_Estado').value = endereco5.uf;
}


const eNumero5 = (numero5) => /^[0-9]+$/.test(numero5);

const cepValido5 = (cep5) => cep5.length == 8 && eNumero5(cep5); 

const pesquisarCep5 = async() => {
    limparFormulario5();
    
    const cep5 = document.getElementById('id_Cep').value;
    const url = `https://viacep.com.br/ws/${cep5}/json/`;
    if (cepValido5(cep5)){
        const dados5 = await fetch(url);
        const endereco5 = await dados5.json();
        if (endereco5.hasOwnProperty('erro')){
            document.getElementById('id_Rua').value = 'CEP não encontrado!';
        }else {
            preencherFormulario5(endereco5);
        }
    }else{
        document.getElementById('id_Rua').value = 'CEP incorreto!';
    }
     
}

document.getElementById('id_Cep')
        .addEventListener('focusout',pesquisarCep5);