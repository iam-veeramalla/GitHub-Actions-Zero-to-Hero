name: End to End CI/CD workflow for Java Applicaton with Maven, Sonar and k8s Intergation

on:
  push:
    branches:
      - main

env:
  KUBECONFIG: ${{ secrets.KUBECONFIG }}
  SONAR_TOKEN: ${{ secrets.SONAR_TKN }}

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Java jdk setup
      uses: actions/setup-java@v1
      with:
        java-version: 12

    - name: maven target # change accordingly
      run: mvn clean install

    - name: Perform analysis on Sonar Qube
      uses: sonarsource/sonarcloud-github-action@v1
      with:
        sonarcloud.organization: <name of your org>
        sonarcloud.projectKey: <key>
        sonarcloud.projectName: <name>
        sonarcloud.token: ${{ env.SONAR_TKN }}
        sonarcloud.scannerVersion: "4.2.0.1873"

  deploy:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Deploy to k8s
      uses: stefanzweifel/k8s-action@v2.0.0
      with:
        args: apply -f kubernetes/
      env:
        KUBECONFIG: ${{ env.KUBECONFIG }}
