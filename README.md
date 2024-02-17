# AWS Lambda

Vamos trabalhar com algumas funções Lambda utilizando o framework da AWS chamado Chalice em um ambiente Linux.
Para mais informações [https://pypi.org/project/chalice/](https://pypi.org/project/chalice/)

Iremos utilizar também a biblioteca virtualenv, acesse o link para mais informações [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)

Pré-requisitos
- Conta na AWS devidamente configurada (usuário no IAM com permissões para a criação de recursos, Access key e Secret key para configurar no terminal via AWS CLI) [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Invoke
Crie um diretório com o nome **invoke** e dentro dela um outro diretório para o virtualenv, vamos chamá-lo de **venv**.

Deverá ficar assim
```sh
~/aws-lambdas/invoke/venv
```
Acesse esta pasta e digite para criar o virtualenv
```sh
cd venv
virtualenv invoke
```

Para **ativar** o virtualenv digite
```
source invoke/bin/activate
```

Agora volte para a pasta "original" ~/aws-lambdas/invoke
```sh
cd ..
```

Agora vamos iniciar o nosso projeto, digite
```sh
chalice new-project
```

Em project name, digite invoke para mantermos o mesmo padrão. Após isso, um prompt com alguma opções será exibido, selecione a opção **Lambda Functions only**. Você receberá uma saída como
```sh
Your project has been generated in ./invoke
```

Vamos instalar a lib **pytest** para fazer nossos testes, aproveite e instale o chalice (agora estamos em um virtual env, lembra...?)
```sh
pip install pytest
```

Para fazer o teste, execute o seguinte comando
```sh
py.test invoke/tests/test_app.py -s
```