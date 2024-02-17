# AWS Lambda

Neste projeto iremos trabalhar com algumas funções Lambda utilizando o framework da AWS chamado **Chalice** em um ambiente Linux.
Para mais informações [https://pypi.org/project/chalice/](https://pypi.org/project/chalice/).

Como dependências, teremos a biblioteca virtualenv, acesse o link para mais informações [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/) além da biblioteca pytest para testes [https://pypi.org/project/pytest/](https://pypi.org/project/pytest/).

Pré-requisitos
- Conta na AWS devidamente configurada (usuário no IAM com permissões para a criação de recursos)
- AWS CLI instalado e configurado [How to instal AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Após instalar o AWS CLI, execute o comando abaixo para configurar a sua conta

```sh
aws configure
```

Será solicitado o **Access Key ID**, **Secret Access Key**, **Default region name** e **Default output format**. Preencha com as informações corretas.

Em default region, geralmente utilizamos **us-east-1** e para a saída, **json**.

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

Vamos instalar a lib **pytest** para fazer nossos testes, aproveite e instale o chalice (agora estamos em um virtual env, lembra...?)

```sh
pip install pytest
```

Para fazer o teste, execute o seguinte comando

```sh
py.test scheduled/tests/test_app.py -s
```

O resultado deverá ser similar a este

![Teste](https://i.ibb.co/9YPCVsR/aws-lambdas-chalice-scheduled-test.png)

Pronto, teste efetuado com sucesso, assim sendo, vamos efetuar o **deploy**.

Lembrando de conferir que está dentro do diretório da função Lambda, neste caso, ~/aws-lambdas/scheduled/scheduled.

```sh
chalice deploy
```

Acesse o console de sua conta na AWS veja que sua função estará lá.
![AWS Console](https://i.ibb.co/7R8Bm9J/aws-lambdas-chalice-scheduled-deployed.png)

Além disso, a função será executada a cada 15 minutos, conforme configurado no arquivo **app.py**.

```python
@app.schedule("cron(*/15 * ? * * *)")
def scheduled(event):
    print("Function executed successfully!")
    return True
```

Veja
![Logs](https://i.ibb.co/ch17TDR/aws-lambdas-chalice-scheduled-deployed-logs.png)

## S3 Trigger

Agora, iremos criar uma função que será acionada quando um arquivo for enviado para um **bucket S3**. Vamos chamar essa função de **s3trigger**.

Acesse sua conta na AWS e crie um bucket S3, no meu caso, criei um chamado **aws-lambdas-chalice**.

Crie o diretório **s3trigger** e dentro dele, o diretório **venv** como temos feito nas funções anteriores.
```sh
mkdir s3trigger & mkdir s3trigger/venv 
```

Acesse estao diretório **venv** e execute o comando abaixo para criar o virtualenv

```sh
cd s3trigger/venv
virtualenv s3trigger
```

Ative o virtualenv

```sh
source s3trigger/bin/activate
```

Agora volte para o diretório do projeto ~/aws-lambdas/s3trigger

```sh
cd ..
```

Crei o projeto

```sh
chalice new-project
```

Em project name, digite **s3trigger** para mantermos o mesmo padrão. Após isso, um prompt com alguma opções será exibido, neste caso, utilize o **S3 Event Handler**.
