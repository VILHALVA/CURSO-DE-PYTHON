# CRUD PYTHON EM JSON
## DESCRIÇÃO:
Este aplicativo de gerenciamento de usuários foi desenvolvido em Python e utiliza JSON para armazenar os dados dos usuários. Ele oferece funcionalidades básicas de um CRUD (Create, Read, Update, Delete) para manipular uma lista de usuários, permitindo adicionar novos usuários, listar todos os usuários cadastrados, atualizar informações de um usuário existente e excluir usuários.

O aplicativo é executado em um loop interativo de menu, onde o usuário pode selecionar diferentes opções através de números. Cada opção corresponde a uma operação específica:

1. **Adicionar Usuário:** Permite ao usuário adicionar um novo usuário fornecendo o nome e a idade.
2. **Listar Usuários:** Mostra na tela a lista de todos os usuários cadastrados, exibindo seus nomes e idades.
3. **Atualizar Usuário:** Permite ao usuário atualizar as informações de um usuário existente, fornecendo o nome do usuário a ser atualizado, o novo nome e a nova idade.
4. **Excluir Usuário:** Permite ao usuário excluir um usuário existente fornecendo o nome do usuário a ser excluído.
5. **Sair:** Encerra o programa.

Os dados dos usuários são armazenados em um arquivo JSON chamado `"usuarios.json"` no mesmo diretório do código. As informações dos usuários são representadas como objetos JSON contendo os campos `"nome"` e `"idade"`. Cada operação de manipulação dos usuários (adicionar, listar, atualizar, excluir) é implementada alterando este arquivo JSON conforme necessário.

Este aplicativo é útil para situações em que é necessário armazenar e gerenciar informações de usuários de forma simples e eficiente, utilizando um formato de armazenamento de dados flexível como o JSON. Ele pode ser facilmente estendido e integrado a outros sistemas que necessitam de funcionalidades de gerenciamento de usuários.