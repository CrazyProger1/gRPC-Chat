.PHONY: runserver
runserver:
	python -m server

.PHONY: runclient
runclient:
	python -m client

.PHONY: gen
gen:
	python -m grpc_tools.protoc -I protos  --python_out=gen --pyi_out=gen --grpc_python_out=gen protos/*

.PHONY: cleancode
cleancode:
	isort .
	black .
