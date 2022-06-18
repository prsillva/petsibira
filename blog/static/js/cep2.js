'use strict';

const limparFormulario7 = (endereco7) =>{
    document.getElementById('id_RuaVoluntario').value = '';
    document.getElementById('id_BairroVoluntario').value = '';
    document.getElementById('id_CidadeVoluntario').value = '';
   
}


const preencherFormulario7 = (endereco7) =>{
    document.getElementById('id_RuaVoluntario').value = endereco7.logradouro;
    document.getElementById('id_BairroVoluntario').value = endereco7.bairro;
    document.getElementById('id_CidadeVoluntario').value = endereco7.localidade;
    
}


const eNumero7 = (numero7) => /^[0-9]+$/.test(numero7);

const cepValido7 = (cep7) => cep7.length == 8 && eNumero7(cep7); 

const pesquisarCep7 = async() => {
    limparFormulario7();
    
    const cep7 = document.getElementById('id_CepVoluntario').value;
    const url = `https://viacep.com.br/ws/${cep7}/json/`;
    if (cepValido7(cep7)){
        const dados7 = await fetch(url);
        const endereco7 = await dados7.json();
        if (endereco7.hasOwnProperty('erro')){
            document.getElementById('id_RuaVoluntario').value = 'CEP não encontrado!';
        }else {
            preencherFormulario7(endereco7);
        }
    }else{
        document.getElementById('id_RuaVoluntario').value = 'CEP incorreto!';
    }
     
}

document.getElementById('id_CepVoluntario')
        .addEventListener('focusout',pesquisarCep7);