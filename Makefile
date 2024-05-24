.PHONY: runserver
runserver:
	python -m server

.PHONY: runclient
runclient:
	python -m client

.PHONY: gen
gen:
	python -m grpc_tools.protoc -Igen=protos  --python_out=. --pyi_out=. --grpc_python_out=. protos/*.proto

.PHONY: cleancode
cleancode:
	isort .
	black .

