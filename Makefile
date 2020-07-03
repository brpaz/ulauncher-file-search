
EXT_NAME:=ulauncher-file-search
EXT_DIR:=$(shell pwd)

.PHONY: help lint format link unlink deps dev setup
.DEFAULT_GOAL := help

setup: ## Setups the project
	pre-commit install

lint: ## Run Lint
	@flake8

format: ## Format code using yapf
	@yapf --in-place --recursive .

link: ## Symlink the project source directory with Ulauncher extensions dir.
	@ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

unlink: ## Unlink extension from Ulauncher
	@rm -r ~/.local/share/ulauncher/extensions/${EXT_NAME}

deps: ## Install Python Dependencies
	@pip3 install -r requirements.txt

dev: ## Runs ulauncher on development mode
	ulauncher -v --dev --no-extensions  |& grep "${EXT_NAME}"

help: ## Show help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
