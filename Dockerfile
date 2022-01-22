# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /casa 

COPY pyproject.toml pyproject.toml

RUN pip3 install poetry

COPY . .