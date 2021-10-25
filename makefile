docs:
	mkdocs build

serve: docs
	mkdocs serve

.PHONY: docs serve
