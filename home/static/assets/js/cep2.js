'use strict';

const limparFormulario = (endereco) =>{
    document.getElementById('id_RuaVoluntario').value = '';
    document.getElementById('id_BairroVoluntario').value = '';
    document.getElementById('id_CidadeVoluntario').value = '';
    document.getElementById('id_EstadoVoluntario').value = '';
}


const preencherFormulario = (endereco) =>{
    document.getElementById('id_RuaVoluntario').value = endereco.logradouro;
    document.getElementById('id_BairroVoluntario').value = endereco.bairro;
    document.getElementById('id_CidadeVoluntario').value = endereco.localidade;
    document.getElementById('id_EstadoVoluntario').value = endereco.uf;
}


const eNumero = (numero) => /^[0-9]+$/.test(numero);

const cepValido = (cep) => cep.length == 8 && eNumero(cep); 

const pesquisarCep = async() => {
    limparFormulario();
    
    const cep = document.getElementById('id_CepVoluntario').value;
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    if (cepValido(cep)){
        const dados = await fetch(url);
        const endereco = await dados.json();
        if (endereco.hasOwnProperty('erro')){
            document.getElementById('id_RuaVoluntario').value = 'CEP não encontrado!';
        }else {
            preencherFormulario(endereco);
        }
    }else{
        document.getElementById('id_RuaVoluntario').value = 'CEP incorreto!';
    }
     
}

document.getElementById('cep')
        .addEventListener('focusout',pesquisarCep);