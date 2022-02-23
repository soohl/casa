.DEFAULT_GOAL := build

fmt: 
	go fmt ./...
.PHONT:fmt

lint: fmt
	golint ./...
.PHONY:lint

vet: fmt
	go vet ./...
.PHONY: vet

build: vet
	go build -o ./build/hello.go
.PHONY: build