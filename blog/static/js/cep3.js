'use strict';

const limparFormulario3 = (endereco3) =>{
    document.getElementById('id_RuaAdotante').value = '';
    document.getElementById('id_BairroAdotante').value = '';
    document.getElementById('id_CidadeAdotante').value = '';
   
   
}


const preencherFormulario3 = (endereco3) =>{
    document.getElementById('id_RuaAdotante').value = endereco3.logradouro;
    document.getElementById('id_BairroAdotante').value = endereco3.bairro;
    document.getElementById('id_CidadeAdotante').value = endereco3.localidade;
   
    
}


const eNumero3 = (numero3) => /^[0-9]+$/.test(numero3);

const cepValido3 = (cep3) => cep3.length == 8 && eNumero3(cep3); 

const pesquisarCep3 = async() => {
    limparFormulario3();
    
    const cep3 = document.getElementById('id_CepAdotante').value;
    const url = `https://viacep.com.br/ws/${cep3}/json/`;
    if (cepValido3(cep3)){
        const dados3 = await fetch(url);
        const endereco3 = await dados3.json();
        if (endereco3.hasOwnProperty('erro')){
            document.getElementById('id_RuaAdotante').value = 'CEP não encontrado!';
        }else {
            preencherFormulario3(endereco3);
        }
    }else{
        document.getElementById('id_RuaAdotante').value = 'CEP incorreto!';
    }
     
}

document.getElementById('id_CepAdotante')
        .addEventListener('focusout',pesquisarCep3);