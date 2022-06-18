'use strict';

const limparFormulario2 = (endereco2) =>{
    document.getElementById('id_RuaDoador').value = '';
    document.getElementById('id_BairroDoador').value = '';
    document.getElementById('id_CidadeDoador').value = '';
    document.getElementById('id_EstadoDoador').value = '';
}


const preencherFormulario2 = (endereco2) =>{
    document.getElementById('id_RuaDoador').value = endereco2.logradouro;
    document.getElementById('id_BairroDoador').value = endereco2.bairro;
    document.getElementById('id_CidadeDoador').value = endereco2.localidade;
    document.getElementById('id_EstadoDoador').value = endereco2.uf;
}


const eNumero2 = (numero2) => /^[0-9]+$/.test(numero2);

const cepValido2 = (cep2) => cep2.length == 8 && eNumero2(cep2); 

const pesquisarCep2 = async() => {
    limparFormulario2();
    
    const cep2 = document.getElementById('id_CepDoador').value;
    const url = `https://viacep.com.br/ws/${cep2}/json/`;
    if (cepValido2(cep2)){
        const dados2 = await fetch(url);
        const endereco2 = await dados2.json();
        if (endereco2.hasOwnProperty('erro')){
            document.getElementById('id_RuaDoador').value = 'CEP não encontrado!';
        }else {
            preencherFormulario2(endereco2);
        }
    }else{
        document.getElementById('id_RuaDoador').value = 'CEP incorreto!';
    }
     
}

document.getElementById('id_CepDoador')
        .addEventListener('focusout',pesquisarCep2);