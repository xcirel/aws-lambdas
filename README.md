# AWS Lambda

Vamos trabalhar com algumas funções Lambda utilizando o framework da AWS chamado Chalice em um ambiente Linux.
Para mais informações [https://pypi.org/project/chalice/](https://pypi.org/project/chalice/)

Iremos utilizar também a biblioteca virtualenv, acesse o link para mais informações [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)

Pré-requisitos
- Conta na AWS devidamente configurada (usuário no IAM com permissões para a criação de recursos, Access key e Secret key configurada no AWS CLI) [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Invoke

Vamos criar uma função por invocação, ou seja, ela será chamada por um evento específico, como um endpoint HTTP, por exemplo.

Crie um diretório com o nome **invoke** e dentro dele crie um outro diretório para o *virtualenv*, vamos chamá-lo de **venv**.

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

```sh
source invoke/bin/activate
```

Agora volte para o diretório do projeto ~/aws-lambdas/invoke

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

Fazendo o deploy - para fazer o deploy, é importante observar que temos que estar dentro do diretório da função Lambda, neste caso, ~/aws-lambdas/invoke/invoke.

Digite o comando

```sh
chalice deploy 
```

Você terá uma saída similar a esta abaixo

```sh
Creating deployment package.
Reusing existing deployment package.
Creating IAM role: invoke-dev
Creating lambda function: invoke-dev-invoke
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-1:002603181790:function:invoke-dev-invoke
```

Acesse o console de sua conta na AWS veja que sua função estará lá.
![AWS Console](https://i.ibb.co/F4X47mh/aws-lambdas-chalice-deploy.png)

## Scheduled

Vamos criar uma função com disparo programado, para isso, vamos criar um novo diretório chamado **scheduled** e também o diretório para o *virtualenv* chamado **venv**.

```sh
mkdir scheduled & mkdir scheduled/venv 
```

Acesse esta pasta e digite para criar o virtualenv

```sh
cd scheduled/venv
virtualenv scheduled
```

Para **ativar** o virtualenv digite

```sh
source scheduled/bin/activate
```

Agora volte para o diretório do projeto ~/aws-lambdas/scheduled

```sh
cd ..
```

Verifique se o chalice já está instalado dentro do virtualenv

```sh
chalice --version
```

caso não esteja instalado, instale através do abaixo

```sh
pip install chalice
```

Agora vamos iniciar o nosso projeto, digite

```sh
chalice new-project
```

Em project name, digite scheduled para mantermos o mesmo padrão. Após isso, um prompt com alguma opções será exibido, infelizmente não temos a opção **Scheduled Event** disponível, assim sendo, vamos utilizar o **Lambda Functions only**.